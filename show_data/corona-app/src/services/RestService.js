import APIKeys from '../APIKeys.ignore.js';
import axios from 'axios';

const geocodeURL = "https://maps.googleapis.com/maps/api/geocode/json?result_type=administrative_area_level_1|country|locality&latlng="

class RestService {
  constructor(){
    this.url = '127.0.0.1:8000/get_data';
  }

  async retrieveArticlesForState(state) {
    let response = await axios.post(this.url,{state});
    return response.city;
  }

  async retrieveArticlesForCity(city) {
    let response = await axios.post(this.url, {city});
    return response.state;
  }

  async retrieveArticlesFromLocation(lat, lng) {
    let url = geocodeURL & lat & "," & lng & "key=" & APIKeys.getGoogleMapsKey();
    let retArr = [];
    let state = undefined;
    let city = undefined;

    let response = await axios.get(url);
    let firstResult = response.results[0].address_components;
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
  }
}

export default RestService;
