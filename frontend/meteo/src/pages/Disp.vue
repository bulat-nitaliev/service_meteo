<template>
    <div class="app">
        <h3>Информационное взаимодействие участников омс проведения диспансерного наблюдения</h3>
        <div class="reestr">
            <label for="btn"><h5>1. Обновить реестр </h5></label> 
            <my-button 
                @click="updateReestr"
                >Обновить реестр</my-button>          
        </div>
        
        
        <div class="reestr" >
            <label ><h5 >2. Выбирите период :  {{ picked.name }}</h5></label>
        </div>    
        <div class="reestr">
            <my-select
            v-model="picked"       
            :options = options></my-select>
        </div>   
        <div class="reestr">
            <label for="update_reestr"><h5>3. Создать файлы для информирования</h5></label>
            <my-button @click="onInfobip(picked.value)">Инфобип</my-button> 
        </div>

        <div class="reestr">
        <label for="update_reestr"><h5>4. Создаем файлы для почты</h5></label>
        <my-button @click="pochtaProf">Почта</my-button>
        </div>
        <div class="reestr">
        <label for="update_reestr"><h5>5. Создаем PDF, docx, xlsx для почты</h5></label>
        <my-button @click="filePost">PDF, docx, xlsx</my-button>
        </div>

        

        <my-dialog v-model:show="isReestr" style="white-space: pre-wrap;">
        <h5 style="color: teal">Успешно время выполнения {{res}} 
             добавленно {{count}} файлов</h5>       
        </my-dialog>

        <my-dialog v-model:show="isInfoBip" style="white-space: pre-wrap;">
        <h5 style="color: teal">{{ text }}  </h5>
        </my-dialog>
        
        <my-loader v-if="isLoader"></my-loader>
        

    </div>
</template>

<script>
import $api from '@/http'
export default {
    data: ()=>{
        return {
        picked: '',
        isInfoBip: false,
        isReestr: false, 
        text: '',
        res: 0,
        count: 0,
        isLoader: false,
        options: [{
            name: "январь",
            value: 1,
        },{
            name: "февраль",
            value: 2,
        },{
            name: "март",
            value: 3,
        },{
            name:  "апрель",
            value: 4,
        },{
            name: "май",
            value: 5,
        },{
            name: "июнь",
            value: 6,
        },{
            name: "июль",
            value: 7,
        },{
            name: "август",
            value: 8,
        },{
            name: "сентябрь",
            value: 9,
        },{
            name: "октябрь",
            value: 10,
        },{
            name: "ноябрь",
            value: 11,
        },{
            name: "декабрь",
            value: 12,
        }]
        }
    },
    methods: {
        async updateReestr(){
            try {
            this.isLoader = true       
            const response = await $api.get('/api/duche')
            this.res = response.data.res      
            this.count = response.data.count  
            this.isLoader = false 
            this.isReestr = true
            } catch (error) {
                this.isLoader = false
                this.text = `Ошибка выполнения - ${error}`
                this.isInfoBip = true
            }                     
        },
        async onInfobip(arg) {
            try {
                if (!arg){
                this.text = 'Выберете период для запроса'
                this.isInfoBip = true
                return
            }
            this.isLoader = true
            const response = await $api.get(`api/dninfobip/?arg=${arg}`)
            
            const res = response.data.res
            const d_count = response.data.d_count
            this.isLoader = false
            this.text = `Успешно время выполнения ${res} минут
                         созданы файлы инфобип
                        duch: email - ${d_count['email']} ,
                                v_1 - ${d_count['v_1']} ,
                                v_2 - ${d_count['v_2']} ,
                                v_3 - ${d_count['v_3']}`
            this.isInfoBip = true
            } catch (error) {
                this.isLoader = false
                this.text = `Ошибка выполнения - ${error}`
                this.isInfoBip = true
            }       
        },
        async pochtaProf(){
            try {
            this.isLoader = true
            const response = await $api.get(`api/postdn`)            
            const res = response.data.res
            const count = response.data.count 
            this.isLoader = false
            this.text = count?`Успешно время выполнения ${res} \n добавлены индексы
                 не удалось добавить ${count} индексов
                 для полного добавления повторите операцию`:`Успешно время выполнения ${res} \n добавлены все индексы`
            this.isInfoBip = true
            } catch (error) {
                this.isLoader = false
                this.text = `Ошибка выполнения - ${error}`
                this.isInfoBip = true
            } 
        },  
        async filePost(){
            try {this.isLoader = true
            const response = await $api.get(`api/multdn`)            
            const res = response.data.res
            const d_c = response.data.d_c
            this.isLoader = false
            this.text = `Успешно время выполнения ${res} 
            duche: pdf - ${d_c['index']},
                    общее кол-во - ${d_c['all_count']}`
            this.isInfoBip = true
            } catch (error) {
                this.isLoader = false
                this.text = `Ошибка выполнения - ${error}`
                this.isInfoBip = true
            } 
        },
    }      
    
}
</script>

<style scoped>
.reestr {
  display: flex;
  align-items: center;
  padding: 10px 20px;
  
}
/* input {
     margin-left: 15px
} */

label {
  color: teal;
  font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
  margin-left: 20px;
}
</style>