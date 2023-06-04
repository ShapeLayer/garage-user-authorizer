<script lang="ts">
  import ASideItem from './ASideItem.svelte';
  import CategoryHeader from './CategoryHeader.svelte';
  import { Home16, SignOut16, Clock16, Pulse16, Link16, People16, DeviceCameraVideo16, Eye16, Gear16 } from 'svelte-octicons';
</script>

<aside>
  <div class="tree-view">
    <div class="aside-item">
      <ASideItem href="/">
        <span class="icon" slot="icon"><Home16 /></span>
        <span class="content">홈</span>
      </ASideItem>
    </div>
    <CategoryHeader>
      <span class="category-header">출입</span>
    </CategoryHeader>
    <div class="aside-item">
      <ASideItem href="/passing/log">
        <span class="icon" slot="icon"><SignOut16 /></span>
        <span class="content">출입 기록</span>
      </ASideItem>
    </div>
    <div class="aside-item">
      <ASideItem href="/passing/reserved">
        <span class="icon" slot="icon"><Clock16 /></span>
        <span class="content">출입 예정자</span>
      </ASideItem>
    </div>
    <CategoryHeader>
      <span class="category-header">실시간 감지</span>
    </CategoryHeader>
    <div class="aside-item">
      <ASideItem href="/watchdog/update">
        <span class="icon" slot="icon"><Pulse16 /></span>
        <span class="content">최근 업데이트</span>
      </ASideItem>
    </div>
    <div class="aside-item">
      <ASideItem href="/watchdog/received"> 
        <span class="icon" slot="icon"><Link16 /></span>
        <span class="content">연결된 기기</span>
      </ASideItem>
    </div>
    <CategoryHeader>
      <span class="category-header">설정</span>
    </CategoryHeader>
    <div class="aside-item">
      <ASideItem href="/settings/registered">
        <span class="icon" slot="icon"><People16 /></span>
        <span class="content">등록 출입자 관리</span>
      </ASideItem>
    </div>
    <div class="aside-item">
      <ASideItem href="/settings/video_inputs">
        <span class="icon" slot="icon"><DeviceCameraVideo16 /></span>
        <span class="content">비디오 입력 관리</span>
      </ASideItem>
    </div>
    <div class="aside-item">
      <ASideItem href="/settings/test_facenet">
        <span class="icon" slot="icon"><Eye16 /></span>
        <span class="content">인원 식별 테스트</span>
      </ASideItem>
    </div>
    <div class="aside-item">
      <ASideItem href="/settings/system">
        <span class="icon" slot="icon"><Gear16 /></span>
        <span class="content">시스템 설정</span>
      </ASideItem>
    </div>
  </div>
</aside>

<style lang="scss">
  aside {
    align-self: start;
    display: flex;
    flex: 0 0 auto;
    flex-direction: column;
    inline-size: 13em;
    inset-block-start: 3.3em;
    max-block-size: calc(100vh - 3.3em);
    writing-mode: horizontal-tb;
    word-break: keep-all;
    margin-top: 3.3em;
    overflow: auto;
    padding-block-start: 1em;
    padding-inline: 1em .3em;
    position: -webkit-sticky;
    position: sticky;
    transition: .25s ease-in-out;
    @media (max-width: 600px) {
      & {
        inline-size: 4.6em;
        transition: .25s ease-in-out;
      }
    }
  }
  .aside-item {
    cursor: pointer;
  }
  .tree-view {
    max-block-size: 100%;
    min-block-size: 0;
  }
  .icon {
    display: flex;
    vertical-align: text-top;
    padding-right: .5em;
  }
  .category-header {
    transition: .25s ease-in-out;
    @media (max-width: 600px) {
      & {
        display: none;
        transition: .25s ease-in-out;
      }
    }
  }
  .content {
    transition: .25s ease-in-out;
    @media (max-width: 600px) {
      & {
        display: none;
        transition: .25s ease-in-out;
      }
    }
  }
</style>
