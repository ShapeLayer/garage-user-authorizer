<script lang="ts">
  import { ListItem } from 'fluent-svelte';
  import type { PersonData } from './Person';
  export let personData: PersonData
</script>

<div class="person-component">
  <ListItem>
    <div class="person-image__wrapper">
      <img class="person-image__image" src="{ personData.imagePath }" />
    </div>
    <div class="person-content">
      <span id="person-name">{ personData.name }</span>
      <span id="person-organization">{ personData.organization }</span>
    </div>
  </ListItem>
</div>

<style lang="scss">
  .person-image {
    width: 3em;
    height: 100%;
  }
  .person-content {
    display: flex;
    flex-direction: column;
  }
</style>
