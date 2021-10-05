/* eslint-disable */
import _axios from "./default"
export default {
    getSearchNewsInfo(stockName) {
        return _axios({
            url: `/news`,
            method: 'get',
            params: {
                search_word: stockName
            },
        })
    },
}