export class User {
  id: string;
  name: string;
  imagePath: string;
  probability: number;
  private _organization: string; // id
  organization: string;
  description: string;
  constructor(id: string, name: string, imagePath: string, probability: number, _organization: string, organization: string, description: string) {
    this.id = id;
    this.name = name;
    this.imagePath = imagePath;
    this.probability = probability;
    this._organization = _organization;
    this.organization = organization;
    this.description = description;
  }

  updateOrganization () {
    fetch('/api/user/get?' + new URLSearchParams({
      id: this._organization
    })).then((response) => response.json())
      .then((data) => {
        if (data['state'] === 'success') {
          this.organization = data['result']['display_name']
        }
      });
  }
}
