export enum DrawType {
  Rectangle,
  Text
}

export type RectangleInfo = {
  x: number,
  y: number,
  w: number,
  h: number
}
export type TextInfo = {
  content: string,
  color: string,
  fontPath: string
}

export class Draw {
  drawType: DrawType;
  drawDetail: RectangleInfo | TextInfo;
  constructor(drawType: DrawType, drawDetail: RectangleInfo | TextInfo) {
    this.drawType = drawType;
    this.drawDetail = drawDetail;
  }
}