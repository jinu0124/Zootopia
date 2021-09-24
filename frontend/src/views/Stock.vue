<template>
    <div>
        <div class="row">
            <Sidebar></Sidebar>
        </div>
        <div class="row">
            <SearchBar v-on:searchStock="searchStock"></SearchBar>
        </div>
        <div class="row">
            <div class="stock_remark_title">주가</div><div class="stock_remark">of {{now}} AM</div>
        </div>
        <div class="row stock_chart">
            <LineChart :options="options" :height="400" class="col-md-8" :chart-data="datacollection"></LineChart>
            <StockInfo ></StockInfo>
        </div>
       
    </div>
</template>

<script>
import Sidebar from "../components/Sidebar.vue"
import SearchBar from "../components/Searchbar.vue"
import stock from "../api/stock"
import LineChart from "../components/LineChart.js"
import StockInfo from "../components/StockInfo.vue"

export default {
    name: "Stock",
    components:{
        Sidebar,
        SearchBar,
        LineChart,
        StockInfo,
    },
    data() {
        return {
            socket: null,
            status: "",

            searchWord: "",
            stockProfile: [],
            
            now: this.$moment(new Date()).format("DD MMM YYYY HH:mm:ss"),

            options:{
                 scales: {
                    yAxes: [
                        {
                            ticks: {
                                beginAtZero: true
                            }
                        }]
                },
                responsive: true,
                maintainAspectRatio: false
            },
            datacollection: {
                labels: ["week 1", "week 2", "week 3", "week 4", "week 5", "week 6", "week 7", "week 8", "week 9", "week 10"],
                datasets: [
                {
                    data: [86, 114, 106, 106, 107, 111, 133, 221, 783, 2478],
                    label: "Africa",
                    borderColor: "#3e95cd",
                    fill: false
                },
                {
                    data: [282, 350, 411, 502, 635, 809, 947, 1402, 3700, 1267],
                    label: "Asia",
                    borderColor: "#8e5ea2",
                    fill: false
                },
                ]
            },
        }
    },
    methods: {
        async searchStock(searchWord){
            this.searchWord = searchWord
            let lastIdx = 0
            await stock.getStockProfile(searchWord)
            .then(({data}) => {
                lastIdx = this.stockProfile.length
                this.stockProfile.push(data)
            })
            this.socketConnect(lastIdx)
        },
        socketConnect(idx){
            this.socket = new WebSocket("ws://localhost:8080/kiwoom/hoga/" + this.stockProfile[idx].symbol)
            this.socket.onopen = () => {
                this.status = "connected";
                this.socket.onmessage = ({data}) => {
                    console.log(data)
                }
            }
        },
    },
    mounted(){
        setInterval(() => {
            this.now = this.$moment(new Date()).format("DD MMM YYYY HH:mm:ss")
        }, 1000)
    }
}
</script>

<style>
.left-pad{
    position:fixed;
    width: 100%;
    top:0px;
    left: 0px;
}

.stock_chart{
    position:relative;
    top: 130px;
    left: 100px;
}

.stock_info{
    padding-top:30px;
    padding-right:100px;
}

.stock_info>ul{
    list-style-type: none;
    margin-left: -40px;
    margin-right:60px;
    color:rgb(29, 83, 85);
}

.stock_remark_title{
    position:relative;
    top:120px;
    padding-left:120px;
    font-size:1.2em;
}

.stock_remark{
    position:relative;
    top:120px;
    padding-left:120px;
    font-size:0.5em;
}
</style>