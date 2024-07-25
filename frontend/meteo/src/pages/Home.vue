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
          v-for="l in lst"
          :key="l"
          class="container">
            {{ l.name }}
        </div> -->
        <input 
          @input="fetchInput"
          v-model="inp"
          type="text"
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
          
        
        <button @click="showPogoda">show pogoda</button>
       
      </div>
      
    </div>
    </div>
    
</template>

<script>
import $api from '@/http'
import axios from 'axios'
export default {
  data(){
    return {
      inp:'',
      lst: [],
      latitude:'',
      longitude:'',
      list_citys:[],
      isSelect: false,
      city_name: ''
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
      console.log(e.target.outerText);
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
        console.log(res);
        console.log(res_city);
      } catch (error) {
        console.log(error);
      }
      

    },
    async userCity(){
      const res_city = await $api.get(`api/city`)
      console.log(res_city);
    }
  },
//   mounted () {
//     M.AutoInit()
    
// },
}
</script>

<style scoped>
.container{
  display: flex;
  flex-direction: column;
}
</style>