<script lang="ts">
  import { onMount } from 'svelte';
  import { PersonData } from './Person';
  import Person from './Person.svelte';
  let id: string = '';
  let fetchDone: boolean = false;
  let personList: Array<PersonData>;

  const fetchPersonList = () => {
    if (id === '') return
    fetch('/api/person_list/get?' + new URLSearchParams({
      id: id
    })).then((response) => response.json())
      .then((data) => {
        if (data['state'] === 'success') {
          data['result']['person_list'].forEach((now) => {
            const nowPersonData: PersonData = new PersonData(
              now['id'], now['name'], now['image_path'], now['probability'], now['organization']['id'], now['organization']['display_name'], ''
            );
            personList.push(nowPersonData);
          })
          // 정확도 높은 순 정렬
          personList.sort((a, b) => -(a.probability - b.probability));
          fetchDone = true;
        }
      });
  }

  const init = () => {
    fetchPersonList();
  }

  onMount(init)
</script>

<div class="person-selector">
  {#if fetchDone}
    {#each personList as person}
      <Person personData={person} />
    {/each}
  {/if}
</div>
