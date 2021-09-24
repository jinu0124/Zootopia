import _axios from "./default"

export default {
    getStockProfile(stockName) {
        return _axios({
            url: `/stock/symbol`,
            method: 'get',
            params: {
                name: stockName
            },
        })
    },
}