<script lang="ts">
  import 'fluent-svelte/theme.css'
  import ASide from '$lib/components/ASide/ASide.svelte'
  import Article from '$lib/components/Article/Article.svelte'
  import NavBar from '$lib/components/NavBar/NavBar.svelte'
</script>

<div class="app">
  <NavBar />
  <div class="app-inner">
    <ASide />
    <Article>
      <slot />
    </Article>
  </div>
</div>

<style lang="scss">
  .app, .app-inner {
    position: relative;
  }
  .app-inner {
    display: flex;
  }
</style>
