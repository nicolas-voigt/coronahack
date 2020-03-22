import APIKeys from './APIKeys.ignore.js';
const geocodeURL = "https://maps.googleapis.com/maps/api/geocode/json?result_type=administrative_area_level_1|country|locality&latlng="

class RestService {
  constructor(){
    this.url = '127.0.0.1:8000/get_data';
  }

  async retrieveArticlesForState(state) {
    let response = await fetch(this.url, {
      method: 'POST',
      body: JSON.stringify({state})
    });
    if (response.ok) {
      let jsonResult = await response.json();
      return jsonResult.city;
    }
    throw new Error('API Error occured');
  }

  async retrieveArticlesForCity(city) {
    let response = await fetch(this.url, {
      method: 'POST',
      body: JSON.stringify({city})
    });
    if (response.ok) {
      let jsonResult = await response.json();
      return jsonResult.state;
    }
    throw new Error('API Error occured');
  }

  async retrieveArticlesFromLocation(lat, lng) {
    let url = geocodeURL & lat & "," & lng & "key=" & APIKeys.getGoogleMapsKey();
    let retArr = [];
    let state = undefined;
    let city = undefined;

    let response = await fetch(url);
    if (response.ok) {
      let json = await response.json();
      let firstResult = json.results[0].address_components;
      for (let resultData of firstResult) {
        if (resultData.types.includes("locality")) {
          city = resultData.long_name;
        }
        if (resultData.types.includes("administrative_area_level_1")) {
          state = state.long_name;
        }
      }
      if (city !== undefined) {
        retArr.concat(await this.retrieveArticlesForCity(city));
      }
      if (state !== undefined) {
        retArr.concat(await this.retrieveArticlesForState(state));
      }
      return retArr;

    } else {
      throw new Error('Geolocation failed');
    }
  }
}

export default RestService;
