<script lang="ts">
  import { Button, CalendarView, ContentDialog, TextBox } from "fluent-svelte";
  export let open = false;
</script>

<ContentDialog bind:open title='신규 등록'>
  <div class="dialog-content">
    <label for="ne-passenger">
      <h3>통과자</h3>
      <span id="ne-passenger">
        <TextBox search></TextBox>
      </span>
    </label>
    <label for="ne-related">
      <h3>관계자</h3>
      <span id="ne-related">
        <TextBox search></TextBox>
      </span>
    </label>
    <label for="ne-datetime">
      <h3>날짜 선택</h3>
      <span id="ne-datetime">
        <CalendarView />
      </span>
    </label>
    <label for="ne-description">
      <h3>비고</h3>
      <span id="ne-description">
        <TextBox></TextBox>
      </span>
    </label>
  </div>
  <!-- footer -->
  <Button slot="footer" on:click={() => (open = false)}>저장</Button>
</ContentDialog>
