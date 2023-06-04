<script lang="ts">
  export let title: string = '';
  export let disabled: boolean = false;
  export let loading: boolean = false;

  const scssCardStyleClasses__default = ['card'];
  let scssCardBackgroundColor: string = '';
  let scssCardStyleClasses: Array<string> = scssCardStyleClasses__default.slice();
  
  const renderScssCardStyleClasses = () => {
    scssCardStyleClasses = scssCardStyleClasses__default.slice();
    if (disabled === true) scssCardStyleClasses = scssCardStyleClasses.concat('disabled');
    else if (loading === true) scssCardStyleClasses = scssCardStyleClasses.concat('loading');
    return scssCardStyleClasses;
  }
</script>

<div class="{renderScssCardStyleClasses().join(' ')}">
  {#if title != ''}<div class="card-head"><h5>{ title }</h5></div>{/if}
  <slot />
</div>

<style lang="scss">
  .card {
    -webkit-backdrop-filter: blur(60px) saturate(125%);
    backdrop-filter: blur(60px) saturate(125%);
    background-clip: padding-box;
    background-color: var(--fds-card-background-default);
    border: 1px solid var(--fds-card-stroke-default);
    border-radius: var(--fds-overlay-corner-radius);
    box-shadow: var(--fds-card-shadow);
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
    font-family: var(--fds-font-family-text);
    font-size: var(--fds-body-font-size);
    font-weight: 400;
    line-height: 20px;
    padding: 12px;
    position: relative;
    transition: var(--fds-control-normal-duration) var(--fds-control-fast-out-slow-in-easing);
    -webkit-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
    user-select: none;
    &:hover {
      box-shadow: var(--fds-flyout-shadow);
      transform: translateY(-4px);
    }
    &.disabled,
    &.loading {
      background-color: var(--fds-card-background-secondary);
    }
    .card-head {
      display: flex;
      justify-content: space-between;
      margin-bottom: 12px;
      h5 {
        font-weight: 700;
        font-size: 1.1em;
      }
    }
  }
</style>
