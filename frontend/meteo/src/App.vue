<template>
  <nav>
    <div class="meteo">
      <div class="forms">
        <label >введите город</label>
        <input 
          v-model="modelValue"
          type="text"
          >
        <button type="submit">show pogoda</button>
        {{inp}}
      </div>
      
    </div>

  </nav>
  <!-- <router-view/> -->
</template>

<script>
export default {
  data: ()=>{
    inp:''
  },
  props:{
        modelValue: [String, Number]
    },
}
</script>

<style>


</style>
