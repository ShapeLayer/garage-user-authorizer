<script lang="ts">
  import { MarkGithub16 } from 'svelte-octicons';
</script>

<nav class="navbar">
  <div class="navbar-inner">
    <a class="logo" href="/">Gua</a>
    <span class="right-wrapper">
      <a class="repo" href="https://github.com/ShapeLayer/garage-user-authorizer" target="_blank" rel="noreferrer">
        <span class="icon-wrapper"><MarkGithub16 fill="#003e94" /></span>
        <span class="text-wrapper">Repo</span>
      </a>
    </span>
  </div>
</nav>

<style lang="scss">
  .navbar {
    backdrop-filter: blur(60);
    background-clip: padding-box;
    background-color: var(--fds-layer-background-default);
    border-bottom: 1px solid var(--fds-surface-stroke-flyout);
    box-sizing: border-box;
    inset-block-start: 0;
    inset-inline-start: 0;
    justify-content: center;
    min-block-size: 3.3em;
    position: fixed;
    z-index: 1000;
    a {
      text-decoration: none;
    }
  }
  .navbar-inner {
    margin: 0 auto;
    max-inline-size: 1440px;
    padding-inline: 18px 12px;
  }
  .navbar, .navbar-inner {
    align-items: center;
    display: flex;
    inline-size: 100%;
    .right-wrapper {
      display: flex;
      flex: 1 1 auto;
      gap: 1em;
      justify-content: flex-end;
      padding: 0 1em;
    }
  }
  .logo {
    flex: 0 0 auto;
    align-items: center;
    color: var(--fds-text-primary);
    display: flex;
    font-size: 1.2em;
    font-weight: 600;
    justify-content: center;
    position: relative;
  }
  .repo {
    align-items: center;
    display: flex;
    justify-content: center;
    padding: 0 1em;
    position: relative;
    color: var(--fds-accent-text-primary);
    background-color: var(--fds-subtle-fill-secondary);
  }
  .icon-wrapper {
    display: flex;
    padding: .5em;
  }
  .text-wrapper {
    padding-right: .5em;
  }
</style>
