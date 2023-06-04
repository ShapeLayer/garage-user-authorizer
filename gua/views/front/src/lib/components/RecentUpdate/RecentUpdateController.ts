enum EventTypes {
  undefined = 0,
  info = 1,
  warning = 2,
  verified = 3,
  confirmed = 4,
  critical = 5
}

class ActivityEvent {
  eventType: EventTypes;
  summary: string;
  detail: string;
  constructor (eventType: EventTypes, summary: string, detail: string) {
    this.eventType = eventType;
    this.summary = summary;
    this.detail = detail;
  }
}

export {
  EventTypes, ActivityEvent
};
