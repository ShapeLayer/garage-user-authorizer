export class FaceDetectEvent {
  id: string;
  invoked: number;
  constructor(id: string, invoked: number) {
    this.id = id;
    this.invoked = invoked;
  }
  get invokedDateTime() {
    return new Date(this.invoked * 1000);
  }

  public toString = (): string => {
    return `FaceDetectEvent; id: ${this.id}, invoked: ${this.invoked}`;
  }
}

export type Organization = {
  id: string;
  displayName: string;
}

export class DetectedObjectDetails {
  id: string;
  name: string;
  probability: number;
  imagePath: string;
  description: string;
  organization: Organization;
  constructor(id: string, name: string, probability: number, imagePath: string, description: string, organization: Organization) {
    this.id = id;
    this.name = name;
    this.probability = probability;
    this.imagePath = imagePath;
    this.description = description;
    this.organization = organization;
  }
}

export class FaceDetectEventDetails {
  id: string;
  related: Array<DetectedObjectDetails>;
  constructor(id: string, related: Array<DetectedObjectDetails>) {
    this.id = id;
    this.related = related;
  }
  public toString = (): string => {
    return `FaceDetectEventDetails; id: ${this.id}, relates: ${this.related.length}`;
  }
}
