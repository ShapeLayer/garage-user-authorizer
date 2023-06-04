<script lang="ts">
  import { onMount } from 'svelte';
  import { page } from '$app/stores';
  import ArticleHeader from '$lib/components/Article/ArticleHeader.svelte';
  import { FaceDetectEvent, DetectedObjectDetails, FaceDetectEventDetails } from '$lib/components/FaceDetectEvent/FaceDetectEvent';
  import Card from '$lib/components/Card/Card.svelte';
  import { Button, Flyout } from 'fluent-svelte';

  let eventID: string = '';
  let queryState: string = 'await';
  /* 'await', 'idParsed', 'querystart', 'queried', 'done' */
  let faceDetectEvent: FaceDetectEvent;
  let faceDetectEventDetails: FaceDetectEventDetails;
  let flyoutControls: Array<boolean>;
  $: flyoutControls;

  const getPageParams = (query: Location, _default: string = ''): string => {
    const urlSearchParams = new URLSearchParams(query.search);
    return urlSearchParams.has('id') ? urlSearchParams.get('id')! : _default
  }

  const fetchSuccessHandler = (data: any): FaceDetectEventDetails => {
    let relates: Array<DetectedObjectDetails> = new Array<DetectedObjectDetails>();
    data['related'].forEach((each: any) => {
      relates.push(new DetectedObjectDetails(
        each['id'], each['name'], each['probability'], each['image_path'], each['description'], each['organization']
      ))
    });
    return new FaceDetectEventDetails(data['event_id'], relates);
  }

  const fetchPageData = async (): Promise<any> => {
    // await으로 떨어지는 성능 잡으면서 코드가 undefined일때 변수 콜 하는 문제 잡을 방법 생각해보기
    await fetch('/api/person_list/index?' + new URLSearchParams({
      id: eventID
    })).then((response) => response.json())
    .then((data) => {
      switch (data['state']) {
        case 'success':
          let event = data['result'][0];
          faceDetectEvent = new FaceDetectEvent(event['id'], event['invoked']);
          break;
        case 'error':
        default:
          break;
      }
    })

    await fetch('/api/person_list/get?' + new URLSearchParams({
      id: eventID
    })).then((response) => response.json())
    .then((data) => {
      switch (data['state']) {
        case 'success':
          faceDetectEventDetails = fetchSuccessHandler(data['result']);
          let length = faceDetectEventDetails.related.length;
          flyoutControls = new Array<boolean>(length);
          for (let i = 0; i < length; i++) flyoutControls[i] = false;
          break;
        case 'error':
          break;
        default:
          break;
      }
      return;
    })
  }

  const flyoutOnClickHandler = (index: number) => {
    flyoutControls[index] = true;
  }

  const init = () => {
    eventID = getPageParams($page.url);
    queryState = 'idParsed';
  }

  onMount(init);
</script>

<ArticleHeader>최근 업데이트</ArticleHeader>
{#if queryState === 'idParsed'}
  {#await fetchPageData()}
    로드 중
  {:then}
    <div class="header">
      <h3>{faceDetectEvent.invokedDateTime.toTimeString()}에 발생한 이벤트</h3> <!--Date 데이터 포매팅 필요-->
      <p>시스템이 감지된 얼굴로 {faceDetectEventDetails.related.length}명의 인물을 검색했습니다.</p>
    </div>
    {#each faceDetectEventDetails.related as related, i}
      <div class="content">
        <Card title="{related.name}">
          <div class="card-wrapper">
            <div class="image-wrapper">
              <img class="profile-image" src="/api/userstatic/{related.imagePath}" />
            </div>
            <div class="card-content">
              <p><span class="label">이름</span>: <span class="value">{related.name}</span></p>
              <p><span class="label">소속</span>: <span class="value">{related.organization.displayName}</span></p>
              <p>이 인물이 실제 감지된 인물과 동일인일 확률은 {related.probability}%입니다.</p>
            </div>
            <div class="controls">
              <Flyout>
                <Button accent={true} on:click={() => {flyoutOnClickHandler(i)}}>{flyoutControls[i] ? '확인' : '확정'}</Button>
                <svelte:fragment slot='flyout'>시스템에 감지된 인물이 이 인물이라고 기록합니다.</svelte:fragment>
              </Flyout>
            </div>
          </div>
        </Card>
      </div>
    {/each}
  {/await}
{/if}

<style lang="scss">
  .header {
    margin-bottom: .5em;
  }
  .content {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    grid-gap: 1em;
    grid-auto-rows: minmax(2em, auto);
    @media (max-width: 700px) {
      grid-template-columns: repeat(1, 1fr);
    }
  }
  .profile-image {
    border-radius: .5em;
    margin: 1em;
    max-width: 20em;
  }
  .card-wrapper {
    .image-wrapper {
      display: flex;
      justify-content: center;
      align-items: center;
    }
  }
</style>
