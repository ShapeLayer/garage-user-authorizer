<script lang="ts">
  import { onMount } from 'svelte';
  import ArticleHeader from '$lib/components/Article/ArticleHeader.svelte';
  import Card from '$lib/components/Card/Card.svelte';
  import { ProgressRing, Expander } from 'fluent-svelte';
  import Device from './classes';
  import ConnType from './classes';

  let deviceCardIsLoading: boolean = true;
  let deviceList: Array<Device> = [
    { id: 1, name: '로컬 카메라 1', connType: 1, conn: 'COM0' },
    { id: 2, name: 'IP카메라 1', connType: 2, conn: '172.0.0.1' }
  ];

  const connTypeToString = (val: ConnType) => {
    switch(val) {
      case ConnType.usb:
        return 'usb';
      case ConnType.ip:
        return 'ip';
      default:
        return 'unknown';
    };
  }

  const onMountHandler = () => {
    deviceCardIsLoading = false;
  }

  onMount(onMountHandler);
</script>

<ArticleHeader>비디오 입력 관리</ArticleHeader>
<h2>등록된 입력 장치 목록</h2>
<div class="devices">
  <Card loading={deviceCardIsLoading}>
    {#if deviceCardIsLoading == true}
      <div class="loading-dialog">
        <ProgressRing />
        <span class="state-comment">정보를 불러오는 중입니다..</span>
      </div>
    {:else}
      <div class="device-list">
        {#each deviceList as device}
          <Expander>
            {device.name}
            <svelte:fragment slot="content">
              [{connTypeToString(device.connType)}] {device.conn}와 연결됨
            </svelte:fragment>
          </Expander>
        {/each}
      </div>
    {/if}
  </Card>
</div>

<style lang="scss">
  h2 {
    font-size: 1.3em;
    font-weight: 500;
    margin: 1em 0;
  }
  .loading-dialog {
    align-items: center;
    display: flex;
    gap: 1em;
    justify-content: center;
  }
  .device-list {
    display: flex;
    flex-direction: column;
    gap: 1em;
  }
</style>

