import type { User } from "$lib/commons/User";

export class Reservation {
  passenger: User;
  relates: User;
  when: number; // unix timestamp
  description: string;
  constructor(passenger: User, relates: User, when: number, description: string) {
    this.passenger = passenger;
    this.relates = relates;
    this.when = when;
    this.description = description;
  }
}
