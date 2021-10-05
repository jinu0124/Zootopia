import axios from 'axios'

// http://j5a602.p.ssafy.io:8080
// http://localhost:8080
const _axios = axios.create({
    baseURL: "http://j5a602.p.ssafy.io:8080",
    timeout: 20000,
})

export default _axios;