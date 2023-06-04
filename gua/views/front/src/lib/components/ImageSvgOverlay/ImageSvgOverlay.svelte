<script lang="ts">
  import { onMount } from 'svelte';
  import type { Draw, RectangleInfo } from '$lib/components/ImageSvgOverlay/Draw';
  export let src: string = '';
  export let draws: Array<Draw> = [];
  let clientWidth: number;
  let clientHeight: number;
  let svgElement: SVGElement;
  let boxWrapper: SVGGElement;
  let imgElement: HTMLImageElement;

  const reDraw = (draws: Array<Draw>) => {
    boxWrapper.innerHTML = '';
    draws.forEach((draw) => {
      boxWrapper.appendChild(createRect(draw));
    });
  }
  const createRect = (draw: Draw) => {
    const rect = new SVGRectElement();
    const rectInfo: RectangleInfo = draw.drawDetail as RectangleInfo;
    rect.setAttributeNS(null, 'x', `${rectInfo.x}`);
    rect.setAttributeNS(null, 'y', `${rectInfo.y}`);
    rect.setAttributeNS(null, 'width', `${rectInfo.w}`);
    rect.setAttributeNS(null, 'height', `${rectInfo.h}`);
    return rect;
  }

  const init = () => {
    console.log(imgElement);
    clientWidth = imgElement.clientWidth;
    clientHeight = imgElement.clientHeight;
    if (draws !== null)
      reDraw(draws);
  }

  onMount(init);
</script>

<div class="image-svg-overlay">
  <img src={src} bind:this={imgElement} />
  <svg width={clientWidth} height={clientHeight} viewBox="0 0 {clientWidth} {clientHeight}" bind:this={svgElement}>
    <g class="boxes" bind:this={boxWrapper}></g>
  </svg>
</div>
