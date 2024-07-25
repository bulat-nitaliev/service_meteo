import $api from "@/http";

export const prof = {
    state: ()=>({
        res: 0, 
        count: 0,
        isReestr: false

    }),
    getters: ()=>({

    }),
    mutations: ()=>({
        setRes(state,res){
            state.res = res
        }, 
        setCount(state, count){
            state.count6, count
        },
        setReestr(state,bool){
            state.isReestr = bool
        }
    }),
    actions: ()=>({
        async updateReestr(context){
            console.log('реестр');
            const response = await $api.get('/api/reestrprof/')
            context.commit('setRes',response.data.res)
            context.commit('setCount',response.data.count)
            
            

        },
    })

}