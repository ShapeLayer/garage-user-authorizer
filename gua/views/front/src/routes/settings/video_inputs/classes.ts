export enum ConnType {
  usb = 1,
  ip = 2
}

export type Device = {
  id: number,
  name: string,
  connType: ConnType,
  conn: string
};

export default {};
