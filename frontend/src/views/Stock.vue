<template>
    <div>
        <div class="row">
            <Sidebar></Sidebar>
        </div>
        <div class="row">
            <SearchBar v-on:searchStock="searchStock"></SearchBar>
        </div>
        <div class="row">
            <div class="stock_remark_title col-md-8">주가</div>
            <div class="stock_remark col-md-7">of {{now}} AM</div>
            <div class="stock_remark col-md-3" style="padding-left:50px;">
                <button class="duration_button" @click="setDuration(0)">1년</button>
                <button class="duration_button" @click="setDuration(1)">3개월</button>
                <button class="duration_button" @click="setDuration(2)">1달</button>
                <button class="duration_button" @click="setDuration(3)">2주</button>
            </div>
        </div>
        <div class="row stock_chart">
            <LineChart :height="400" class="col-md-8" :chart-data="datacollection"></LineChart>
            <StockInfo v-bind:stockToday="stockToday"></StockInfo>
        </div>
        <div class="row hoga_stage">
            <PieChart class="col-md-3" :height="300" :width="250" :data="chartData"></PieChart>
            <Hoga class="col-md-9" v-bind:askPrice="askPrice" :bidPrice="bidPrice" 
            :askVolume="askVolume" :bidVolume="bidVolume"></Hoga>
        </div>
    </div>
</template>

<script>
import Sidebar from "../components/Sidebar.vue"
import SearchBar from "../components/Searchbar.vue"
import stock from "../api/stock"
import LineChart from "../components/LineChart.js"
import StockInfo from "../components/StockInfo.vue"
import PieChart from "../components/PieChart.js"
import Hoga from "../components/Hoga.vue"

export default {
    name: "Stock",
    components:{
        Sidebar,
        SearchBar,
        LineChart,
        StockInfo,
        PieChart,
        Hoga,
    },
    data() {
        return {
            socket: null,
            status: "",

            searchWord: "",
            stockProfile: [],

            duration: 1,            // 0: 1년, 1: 3개월, 2: 1개월, 3: 2주

            stockToday: {},
            
            now: this.$moment(new Date()).format("DD MMM YYYY HH:mm:ss"),

            askPrice: [],
            askVolume: [],
            bidPrice: [],
            bidVolume: [],
            
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

            chartData: {
                hoverBackgroundColor: "red",
                hoverBorderWidth: 10,
                labels: ["Green", "Red", "Blue"],
                datasets: [
                {
                    label: "Data One",
                    backgroundColor: ["#41B883", "#E46651", "#00D8FF"],
                    data: [1, 10, 5]
                }
                ]
            },


        }
    },
    methods: {
        async getStockProfile(searchWord){
            const res = await stock.getStockProfile(searchWord)
            return res.data;
        },
        async searchStock(searchWord){
            this.searchWord = searchWord

            let data = await this.getStockProfile(searchWord)
            let lastIdx = this.stockProfile.length
            this.stockProfile.push(data)

            this.socketConnect(lastIdx)
        },
        socketConnect(idx){
            console.log(this.stockProfile[idx].symbol)
            this.socket = new WebSocket("ws://localhost:8080/kiwoom/hoga/" + this.stockProfile[idx].symbol)
            this.socket.onopen = () => {
                this.status = "connected";
                let cnt = 0
                this.socket.onmessage = ({data}) => {
                    cnt = 1 - cnt
                    if(cnt % 2 != 0) this.getToday(this.stockProfile[idx].symbol)

                    data = {
                        price: ["+77300", "+77400", "+77500", "+77600", "+77300", "+77400", "+77500", "+77600", "+77500", "+77600"],
                        volume: [468435,8643,6843,1580, 468435,8643,6843,158, 6843,158]
                        }
                    
                    this.askPrice = []
                    this.askVolume = []
                    this.bidPrice = []
                    this.bidVolume = []

                    if(data.price[0][0] == "+"){
                        console.log("+")
                        data.price.forEach(e => {
                            this.askPrice[this.askPrice.length] = e.substring(1,e.length)
                            
                        });
                        data.volume.forEach(e => {
                            this.askVolume[this.askVolume.length] = e
                        });
                        console.log(this.askPrice, this.askVolume)
                    }
                    data = {
                        price: ["-77300", "-77400", "-77500", "-77600", "-77300", "-77400", "-77500", "-77600", "-77500", "-77600"],
                        volume: [468435,8643,6843,1580, 468435,8643,6843,158, 6843,158]
                        }
                    if(data.price[0][0] == "-"){                    // else
                        console.log("-")
                        data.price.forEach(e => {
                            this.bidPrice[this.bidPrice.length] = e.substring(1,e.length)
                        });
                        data.volume.forEach(e => {
                            this.bidVolume[this.bidVolume.length] = e
                        });
                    }
                }
            }
        },
        async getToday(symbol){
            let res = await stock.getStockToday(symbol)
            console.log(res)
            
            this.stockToday = res.data
            console.log(this.stockToday)
        },
        setDuration(dur){
            this.duration = dur
        }
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
    position: absolute;
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
    font-size:1.4em;
}

.stock_remark{
    position:relative;
    top:120px;
    padding-left:120px;
    font-size:0.5em;
}


.duration_button:hover {
  background-color: #52a5e9; /* Green */
  color: white;
}

.duration_button {
  transition-duration: 0.4s;
  background-color: white;
  color: black;
  border: 2px solid #bcc9c7b7;
  border-radius: 4px;
}

.hoga_stage{
    position: relative;
    padding-left: 120px;
    top: 180px;
}


</style>