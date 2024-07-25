<template>
    <div>
        <my-button @click="userList">Получить список пользователей</my-button>
        <div v-for="user in list_users" :key="user.id">
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
          v-for="l in lst"
          :key="l"
          
         class="container">
         <span @click="selectCity">{{ l.name }} - {{ l.country }} - {{ l.admin1 }}</span>
          
          <!-- </v-avtocomlete> -->
        </div>
          
        
        <button @click="showPogoda">show pogoda</button>
       
      </div>
      
    </div>
    </div>
    
</template>

<script>
import $api_search from '@/http'
import axios from 'axios'
export default {
  data(){
    return {
      inp:'',
      lst: [],
      latitude:'',
      longitude:'',
    }
    
  },
  methods:{
    async fetchInput(){
      const val = 'search?name=' + this.inp
      const res = await $api_search.get(val)
      this.lst = res.data['results']
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
    },
    async showPogoda(){
      const  url_drf = 'http://127.0.0.1:8000/'
      const res = await axios.get(url_drf+`api/meteo/?latitude=${this.latitude}&longitude=${this.longitude}`)
      console.log(res);

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