<script lang="ts">
  import { onMount } from 'svelte';
  import { ListItem } from 'fluent-svelte';
  import ArticleHeader from '$lib/components/Article/ArticleHeader.svelte';
  import { FaceDetectEvent } from '$lib/components/FaceDetectEvent/FaceDetectEvent';
  import PersonSelector from '$lib/components/PersonSelector/PersonSelector.svelte';

  $: eventList = fetch('/api/person_list/index')
    .then((response) => response.json())
    .then((data) => {
      let eventList = new Array<FaceDetectEvent>;
      data['result'].forEach((event) => {
        eventList.push(new FaceDetectEvent(event['id'], event['invoked']));
      })
      return eventList;
    });

  const init = () => {
  }

  onMount(init);
</script>

<ArticleHeader>최근 업데이트</ArticleHeader>
<div class="event-update-list">
  {#await eventList}
    로드 중..
  {:then eventList}
    {#each eventList as event, i}
      <ListItem href="/watchdog/update/log?id={event.id}">
        <span class="event-id" id={ event.id }>{ event.invokedDateTime.toTimeString() } 처리됨</span>
      </ListItem>
    {/each}
  {/await}
</div>
<!--WIP 인물 검증(선택) 페이지 임시 위치-->
<!--<PersonSelector />-->
