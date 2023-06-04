<script lang="ts">
  import ArticleHeader from '$lib/components/Article/ArticleHeader.svelte';
  import Card from '$lib/components/Card/Card.svelte';
  import RecentUpdate from '$lib/components/RecentUpdate/RecentUpdate.svelte';
</script>

<ArticleHeader>홈</ArticleHeader>
<div class="content">
  <Card title="최근 업데이트">
    <RecentUpdate />
  </Card>
  <Card title="실시간 감지">
    #_VIDEO_#
  </Card>
</div>

<style lang="scss">
  .content {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    grid-gap: 1em;
    grid-auto-rows: minmax(3em, auto);
    @media (max-width: 700px) {
      grid-template-columns: repeat(1, 1fr);
    }
  }
</style>
