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
    getStockToday(symbol) {
        return _axios({
            url: `/stock/today`,
            method: 'get',
            params: {
                symbol: symbol
            },
        })
    },
}