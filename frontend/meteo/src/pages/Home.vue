<template>
    <div>
        <my-button @click="userCity">Получить список просмотренных городов</my-button>
        <div v-for="user in list_citys" :key="user.id">
            <div>{{ user.first_name}}</div>
            <div>{{ user.last_name}}</div>
            <div>{{user.email}}</div>
            <br>
        </div>
        <div class="meteo">
      <div class="forms">
        <!-- <label >введите город</label> -->
        <!-- <div 
          "res": {
        "latitude": 51.5625,
        "longitude": 46.0,
        "generationtime_ms": 0.11396408081054688,
        "utc_offset_seconds": 0,
        "timezone": "GMT",
        "timezone_abbreviation": "GMT",
        "elevation": 76.0,
        "current_units": {
            "time": "iso8601",
            "interval": "seconds",
            "temperature_2m": "°C",
            "relative_humidity_2m": "%",
            "is_day": "",
            "wind_speed_10m": "km/h"
        },
        "current": {
            "time": "2024-07-26T05:00",
            "interval": 900,
            "temperature_2m": 19.4,
            "relative_humidity_2m": 50,
            "is_day": 1,
            "wind_speed_10m": 10.8
        },
        "daily_units": {
            "time": "iso8601",
            "temperature_2m_max": "°C",
            "temperature_2m_min": "°C",
            "wind_speed_10m_max": "km/h"
        },
        "daily": {
            "time": [
                "2024-07-26",
                "2024-07-27",
                "2024-07-28",
                "2024-07-29",
                "2024-07-30",
                "2024-07-31",
                "2024-08-01"
            ],
            "temperature_2m_max": [
                25.4,
                27.0,
                30.7,
                26.3,
                28.1,
                25.1,
                24.8
            ],
            "temperature_2m_min": [
                15.5,
                15.4,
                19.0,
                20.7,
                16.5,
                16.1,
                16.8
            ],
            "wind_speed_10m_max": [
                13.1,
                12.4,
                14.3,
                14.2,
                16.2,
                14.4,
                17.2

                 {
        "id": 1,
        "name": "Saratov - Russia - Saratovskaya Oblast",
        "longitude": "46.00861",
        "latitude": "51.54056",
        "count": 1,
        "user": 1
    }
        </div> -->
        <input 
          @input="fetchInput"
          v-model="inp"
          type="text"
          placeholder="введите город"
          >
        
        <div 
          v-if="isSelect"
          class="autocoplite">
          <div
          v-for="l in lst"
          :key="l"
         class="container">
         <span @click="selectCity">{{ l.name }} - {{ l.country }} - {{ l.admin1 }}</span>
        </div>
        </div>
          
        
        <my-button @click="showPogoda">show pogoda</my-button>

        <div 
          v-if="isFlag"
          class="title">
          <div class="row">
            <div class="col s12 m6">
              <div class="card blue-grey darken-1">
                <div class="card-content white-text">
                  <span class="card-title">{{dic_res['current']['time']}} - {{dic_res['current']['is_day']? 'День' :'Ночь'}}</span>
                  <p>Температура {{ dic_res['current']['temperature_2m'] }} <br>
                    Влажность {{ dic_res['current']['relative_humidity_2m'] }} <br>
                    Скорость ветра {{ dic_res['current']['wind_speed_10m'] }} </p>
                </div>
                
              </div>
            </div>
          </div>
          <div 
          v-for="(val, index) in dic_res['daily']['time']" :key="index"
            class="row">
            <div class="col s12 m6">
              <div class="card blue-grey darken-1">
                <div class="card-content white-text">
                  <span class="card-title">{{ val }}</span>
                  <p>Температура днем {{ dic_res['daily']['temperature_2m_max'][index] }} <br>
                    Температура ночью {{ dic_res['daily']['temperature_2m_min'][index] }} <br>
                    Скорость ветра {{ dic_res['daily']['wind_speed_10m_max'][index] }} </p>
                </div>
                
              </div>
            </div>
          </div>
        </div>
        <div 
        @click="selectVal"
        v-if="isCity"
        class="citys">
          <div 
          v-for="val in list_citys" :key="val.id"
            class="row">
            <div 
            
            class="col s12 m6">
              <div class="card blue-grey darken-1">
                <div class="card-content white-text">
                  <span  class="card-title">
                    <p>{{ val.name }}</p>
                    
                  </span>
                  Колличество раз - {{ val.count_city }}
                </div>
                
              </div>
            </div>
          </div>
        </div>
      

       
      </div>
      
    </div>
    </div>
    
</template>

<script>
import $api from '@/http'
import axios from 'axios'
import MyButton from '../components/UI/MyButton.vue'
export default {
  components: { MyButton },
  data(){
    return {
      inp:'',
      lst: [],
      latitude:'',
      longitude:'',
      list_citys:[],
      isSelect: false,
      city_name: '',
      isFlag: false,
      isCity: false,
      dic_res: Object
    }
    
  },
  methods:{
    async fetchInput(){
      const val = 'https://geocoding-api.open-meteo.com/v1/search?name=' + this.inp
      const res = await axios.get(val)
      this.lst = res.data['results']
      this.isSelect = true
    },
    selectCity(e){
      console.log(e);
      const [name,country, admin1] = e.target.outerText.split(' - ')
      
      const val = JSON.parse(JSON.stringify(this.lst.filter(elem=>
        elem.name == name && elem.country == country && elem.admin1 == admin1
      )))
      this.inp = e.target.outerText
      this.longitude =  val[0].longitude
      this.latitude =  val[0].latitude
      this.isSelect = false
      this.city_name = e.target.outerText
    },
    async showPogoda(){
      try {
        const res = await $api.get(`api/meteo/?latitude=${this.latitude}&longitude=${this.longitude}`)
        const res_city = await $api.post(`api/city`, {'name': this.city_name, 'latitude': this.latitude, 'longitude': this.longitude})
        this.dic_res = res.data.res
        this.isFlag = true
        console.log(res);
        console.log(res_city);
      } catch (error) {
        console.log(error);
      }
      

    },
    async userCity(){
      const res_city = await $api.get(`api/city`)
      this.list_citys = res_city.data
      this.isFlag = false
      this.isCity = true
    },
    selectVal(e){
      console.log(e.target.outerText);

    }
  },
}
</script>

<style scoped>
.container{
  display: flex;
  flex-direction: column;
}
</style>