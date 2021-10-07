/* eslint-disable */
import axios from 'axios'
const _axios = axios.create({
    baseURL: "https://j5a602.p.ssafy.io/api",
    timeout: 100000,
})

export default _axios;
