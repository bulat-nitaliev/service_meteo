import $api from "@/http";
import {getApi} from '@/axios-api'

export default class AuthService {
    static async login(username, password){
        return $api.post('/api/token/', {username, password})
    }

    static async register(username, password, email, first_name, last_name){
        return $api.post('/api/users/', {username, password, email, first_name, last_name})
        // return getApi.post('/api/users/', {username, password, email, first_name, last_name})
    }
}