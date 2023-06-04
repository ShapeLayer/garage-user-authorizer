<script lang="ts">
  import { onMount } from 'svelte';
  import { Button } from 'fluent-svelte';
  import ArticleHeader from '$lib/components/Article/ArticleHeader.svelte';
  import ImageSvgOverlay from '$lib/components/ImageSvgOverlay/ImageSvgOverlay.svelte';
  import { Draw, DrawType } from '$lib/components/ImageSvgOverlay/Draw';

  const rmImageFileEndPoint = '/api/receive_media/image_file'

  enum NowState {
    ready = 1,
    formReady,
    requested,
    resultReceived,
    resultRendered
  };

  let isDragOver: boolean = false;
  let buttonFileInput: HTMLInputElement | null = null;
  let nowState: NowState = NowState.ready;
  let queried: Promise<any>;
  $: queried;

  const sendFileToServer = async (formData: FormData): Promise<any> => {
    return fetch(rmImageFileEndPoint, {
      method: 'POST',
      body: formData
    }).then((response) => response.json())
      .then((data) => { 
        nowState = NowState.resultReceived; 
        console.log(data);
        return data;
      })
      .catch((err) => { console.error(err); return null; });
  }
  const sendFileToServerWrapper = (formData: FormData) => {
    queried = sendFileToServer(formData);
  }
  const wrapFilesToFormData = (files: Array<File>) => {
    const formData = new FormData();
    files.forEach((file, i) => {
      formData.append('file', file);
    });
    nowState = NowState.formReady;
    return formData;
  }
  
  /* Event Handlers */
  const onDropHandler = (e) => {
    e.preventDefault();
    if (e.dataTransfer.items) {
      let files = new Array();
      [...e.dataTransfer.items].forEach((item, i) => {
        if (item.kind === 'file') {
          const file = item.getAsFile();
          files.push(file);
        }
      });
      sendFileToServerWrapper(
        wrapFilesToFormData(files)
      );
    } else {
      let files = Array.from([...e.dataTransfer.items]);
      sendFileToServerWrapper(
        wrapFilesToFormData(files)
      );
    }
    nowState = NowState.requested;
  }
  const onButtonClickHandler = (e) => {
    if (buttonFileInput !== null)
      buttonFileInput.click();
  }
  const onFileInputChangeHandler = (e) => {
    let files = Array.from(buttonFileInput.files);
    sendFileToServerWrapper(
      wrapFilesToFormData(files)
    );
  }
  const onDragOverHandler = (e) => {
    e.preventDefault();
  }
  const onDragEnterHandler = (e) => { 
    e.preventDefault();
    isDragOver = true;
  }
  const onDragLeaveHandler = (e) => {
    e.preventDefault();
    isDragOver = false;
  }
  const onDragExitHandler = (e) => {
    e.preventDefault();
    isDragOver = false;
  }
  const onMountHandler = () => {
    buttonFileInput = document.createElement('input');
    buttonFileInput.type = 'file';
    buttonFileInput.addEventListener('change', onFileInputChangeHandler);
  }

  onMount(onMountHandler)
</script>

<ArticleHeader>인원 식별 테스트</ArticleHeader>
<div class="description">
  <p>Gua 시스템이 학습한 등록 출입자를 제대로 인식할 수 있는지 확인할 수 있습니다.</p>
  <p>이미지 파일을 업로드하면 Gua 시스템이 등록 출입자 목록에서 비슷한 인물을 검색합니다.</p>
</div>
{#if nowState == NowState.ready}
<div class="upload-box {isDragOver ? 'drag-over' : ''}">
  <div class="upload-box__inner"
    on:drop={onDropHandler}
    on:dragover={onDragOverHandler}
    on:dragenter={onDragEnterHandler}
    on:dragleave={onDragLeaveHandler}
  >
    <span class="button-wrapper">
      <Button on:click={onButtonClickHandler}>파일 선택</Button>
    </span>
    <span class="drag-dialog">또는 이곳에 파일 드래그</span>
  </div>
</div>
{:else}
  <div class="query-result">
    {#if nowState >= NowState.resultReceived}
      {#await queried}
        시스템이 전송된 이미지를 분석하고 있습니다...
      {:then queried}
        <ImageSvgOverlay src='/api/userstatic/{queried['filename']}' draws={
          [new Draw(
            DrawType.Rectangle,
            {
              x: queried['predict']['face']['x'],
              y: queried['predict']['face']['y'],
              w: queried['predict']['face']['w'],
              h: queried['predict']['face']['h']
            }
          )]
        } />
        <p class="result_inner">label: {queried['predict']['label']}</p>
        <p class="result_inner">prob: {queried['predict']['prob']}</p>
      {/await}
    {:else}
      로드 중
    {/if}
  </div>
{/if}

<style lang="scss">
  .upload-box {
    box-sizing: content-box;
    border-radius: .5em;
    background-color: var(--fds-control-alt-fill-secondary);
    margin: 2em 0;
    transition: .5s ease;
    &.drag-over {
      border: 2px solid var(--fds-accent-secondary);
      background-color: var(--fds-control-alt-fill-tertiary);
      transition: .5s ease;
    }
    .upload-box__inner {
      display: flex;
      min-height: 70vh;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      gap: 1em;
    }
  }
</style>
