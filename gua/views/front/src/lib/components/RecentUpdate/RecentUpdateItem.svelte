<script lang="ts">
  import { Expander } from 'fluent-svelte';
  import { EventTypes } from './RecentUpdateController';
  import { Info16, Alert16, CheckCircle16, XCircle16 } from 'svelte-octicons';
  
  export let type: EventTypes = 0;
  export let summary: string;
  export let detail: string;
  export let datetime: string;
  
</script>

<Expander>
  <span class="icon" slot="icon">
    {#if type == EventTypes.info} <Info16 />
    {:else if type == EventTypes.warning}<Alert16 />
    {:else if type == EventTypes.verified}<CheckCircle16 />
    {:else if type == EventTypes.confirmed}<CheckCircle16 />
    {:else if type == EventTypes.critical}<XCircle16 />
    {:else}<Info16 />
    {/if}
  </span>
  <span class="datetime">{datetime}</span><br>
  <span class="summary">{summary}</span>
  <svelte:fragment slot="content">
    {detail}
  </svelte:fragment>
</Expander>

<style lang="scss">
  /*.icon {
    vertical-align: text-top;
    padding-right: .25em;
  }*/
</style>
