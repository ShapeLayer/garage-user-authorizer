<script lang="ts">
  export let href: string = '';
  export let selected: boolean = false;
  import { ListItem } from 'fluent-svelte';
  import { onMount } from 'svelte';
  import { page } from '$app/stores';

  const checkSelected = () => {
    let nowPath = $page.url.pathname.split('/').join('/');
    let thisPath = href.split('/').join('/');
    if (nowPath === thisPath) selected = true;
    else selected = false;
  }
  const onClickHandler = () => { checkSelected(); }
  const init = () => { checkSelected(); }
  page.subscribe(() => { checkSelected(); })
  onMount(init);
</script>

<ListItem 
  href={href}
  selected={selected}
  on:click={onClickHandler}
>
  <slot name="icon" slot="icon"/>
  <slot />
</ListItem>
