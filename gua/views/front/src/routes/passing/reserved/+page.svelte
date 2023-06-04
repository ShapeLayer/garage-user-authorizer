<script lang="ts">
  import { Button, ListItem } from 'fluent-svelte';
  import ArticleHeader from '$lib/components/Article/ArticleHeader.svelte';
  import Dialog from '$lib/components/PassageReservation/Dialog.svelte';
  let listLoaded: boolean = false;
  let reservedList;
  let openAddDialog: boolean = false;

  const addButtonOnClickHandler = () => {
    openAddDialog = true;
  }
</script>

<ArticleHeader>출입 예정자</ArticleHeader>
<div>
  <Button variant="accent" on:click={addButtonOnClickHandler}>추가</Button>
  <Dialog open={openAddDialog} />
</div>
<div>
{#if listLoaded}
{/if}
</div>
