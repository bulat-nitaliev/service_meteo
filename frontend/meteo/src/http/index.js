import axios from 'axios'


const url_search = 'https://geocoding-api.open-meteo.com/v1/'
const $api_search = axios.create({
    baseURL: url_search,
})

export default $api_search