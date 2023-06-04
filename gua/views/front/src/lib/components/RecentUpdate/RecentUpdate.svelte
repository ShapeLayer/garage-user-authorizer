<script lang="ts">
  import RecentUpdateItem from "./RecentUpdateItem.svelte";
  import { EventTypes } from './RecentUpdateController';
</script>

<div class="recent-update">
  <RecentUpdateItem 
    type={EventTypes.confirmed}
    datetime="2023-03-14 02:47"
    summary="새 인물 승인 및 등록됨"
    detail="ShapeLayer가 감지된 새로운 인물의 통과를 승인하고 DB에 등록했습니다."
  />
  <RecentUpdateItem 
    type={EventTypes.warning}
    datetime="2023-03-14 02:46"
    summary="새 인물 감지됨"
    detail="Gua 시스템이 DB에 없는 새로운 인물을 감지했습니다."
  />
  <RecentUpdateItem
    type={EventTypes.verified}
    datetime="2023-03-14 01:34"
    summary="등록 출입자 확인됨"
    detail="ShapeLayer가 감지된 인물이 Gua 시스템이 추정한 인물과 동일인을 확인했습니다: 박세현(203928490)"
  />
  <RecentUpdateItem
    type={EventTypes.info}
    datetime="2023-03-14 01:33"
    summary="등록 출입자 감지됨"
    detail="Gua 시스템이 DB에 있는 인물을 감지했습니다: 박세현(203928490)"
  />
</div>

<style lang="scss">
  .recent-update {
    display: flex;
    flex-direction: column;
    gap: .3em;
  }
</style>