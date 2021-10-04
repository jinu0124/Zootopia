<template>
    <div>
        <div class="row">
            <Sidebar></Sidebar>
        </div>
        <div class="row">
            <SearchBar v-on:searchStock="searchStock"></SearchBar>
        </div>    
        <div class="row">
            <div class="stock_remark_title col-md-8">
                <label>탐색 시작일<input type="date" /></label>
                <label>탐색 종료일<input type="date" /></label>
            </div>
        </div>
        <div class="row count">
            <div class="count_box">
                <p>검색된 기사 개수</p>
                <p>60</p>
            </div>
            <div class="count_box">
                <p>분석된 단어 개수</p>
                <p>16</p>
            </div>
            <div class="count_box">
                <p>긍정 기사 개수</p>
                <p>43</p>
            </div>
            <div class="count_box">
                <p>부정 기사 개수</p>
                <p>64</p>
            </div>
        </div>
        <div class="row middle">
            <div class="row">
                <div class="word_cloud col-md-8">Word Cloud</div>
                <div class="word_cloud_remark col-md-7">of {{now}} AM</div>
            </div>
            <div class="row word_cloud_chart">
                <div class="word_cloud_position">
                    WordCloud 자리
                    <WordCloud v-on:update="wordClickHandler"
                        :data="defaultWords"
                        nameKey="name"
                        valueKey="value"
                        :color="myColors"
                        :showTooltip="true"
                        >
                    </WordCloud>
                </div>
                <div class="chart_score_positon">
                    <div class="pie_chart_box">
                        <article id="pieChart">
                        <h3 class="text-left text-bold">{{ msg }}</h3>
                            <div class="flex flex-col">
                                <!-- <Pie></Pie> -->
                            </div>
                        </article>
                    </div>
                    <div class="score_box">
                        <div class="score">Score</div>
                        <div class="grade">80점</div>
                    </div>
                </div>
            </div>
        </div>
        <div class="row PnN_news">
            <div class="row news">
                <div class="news_list">
                    <PositiveNews :positiveNews="positiveNews"></PositiveNews>
                </div>
                <div class="news_list">
                    <NegativeNews :negativeNews="negativeNews"></NegativeNews>
                </div>
            </div>
        </div>
    </div>
</template>


<script>
import Sidebar from "../components/Sidebar.vue"
import SearchBar from "../components/Searchbar.vue"
import stock from "../api/stock"
import WordCloud from "../components/WordCloud.js"
// import Pie from "../components/Pie.js"
import PositiveNews from "../components/PositiveNews.vue"
import NegativeNews from "../components/NegativeNews.vue"

export default {
    name: "News",
    components:{
        Sidebar,
        SearchBar,
        WordCloud,
        // Pie,
        PositiveNews,
        NegativeNews
    },
    data(){
        return{

            searchWord: "삼성전자",

            // 임시 테스트
            myColors: ['#1f77b4', '#629fc9', '#94bedb', '#c9e0ef'],
            defaultWords: [{
            "name": "Cat",
            "value": 26
          },
          {
            "name": "fish",
            "value": 19
          },
          {
            "name": "things",
            "value": 18
          },
          {
            "name": "look",
            "value": 16
          },
          {
            "name": "two",
            "value": 15
          },
          {
            "name": "fun",
            "value": 9
          },
          {
            "name": "know",
            "value": 9
          },
          {
            "name": "good",
            "value": 9
          },
          {
            "name": "play",
            "value": 6
          }
        ],

            positiveNews: {},
            negativeNews: {},

            now: this.$moment(new Date()).format("DD MMM YYYY HH:mm:ss"),
            msg: "pie chart 자리",
        }
    },
    methods:{
        async getStockProfile(searchWord){
            const res = await stock.getStockProfile(searchWord)
            return res.data;
        },
        async searchStock(searchWord){
            let data = await this.getStockProfile(searchWord)
            this.searchWord = data.NAME
        },
        // wordClickHandler(name, value, vm) {
        //     this.$emit(console.log('wordClickHandler', name, value, vm));
        // }
    },
    watch:{

    },
    created(){
    },
    mounted(){
        setInterval(() => {
            this.now = this.$moment(new Date()).format("DD MMM YYYY HH:mm:ss")
        }, 1000)
    }
}
</script>

<style>
.stock_remark_title{
    position:relative;
    top:120px;
    padding-left:120px;
    font-size:1.4em;
}

label {
    /* display: inline-block; */
    font: 1rem 'Fira Sans', sans-serif;
    margin-right:10px;
}

input {
    margin-left: 10px;
}

.count{
    width: 90%;
    position: relative;
    top: 150px;
    left: 120px;
}

.count_box{
    display: inline;
    width: 24%;
    border: 1px solid;
    text-align: center;
    margin: 0 5px;
    background-color: rgb(245, 250, 248);
    /* border-radius: 0 15% 15% 0; */
    border: white 1px solid;
}

.middle{
    margin-top: 180px;
    background-color: rgb(245, 250, 248);
    border-radius: 0 15% 15% 0;
    border: white 1px solid;
    padding-top: 20px;
    padding-bottom: 20px;
}

.word_cloud{
    position:relative;
    /* top:180px; */
    padding-left:120px;
    font-size:1.4em;
}

.word_cloud_remark{
    position:relative;
    /* top:180px; */
    padding-left:120px;
    font-size:0.5em;
}

.word_cloud_chart{
    position:relative;
    /* top:180px; */
    left:120px;   
}

.word_cloud_position{
    width: 60%;
    border: 1px solid;
}

.chart_score_positon{
    width: 30%;
}

.pie_chart_box{
    position: relative;
    height: 60%;
    border: 1px solid;
}

.score_box{
    position: relative;
    height: 40%;
    border: 1px solid;
    text-align: center;
    display: flex;
    flex-direction: column;
}

.score{
    margin: 0;
    height: 50%;
    vertical-align: middle;
    /* padding: 5%; */
}

.grade{
    margin: 0;
    height: 50%;
    vertical-align: middle;
    /* padding: 5%; */
}

.PnN_news{
    margin-top: 40px;
    background-color: rgb(245, 250, 248);
    border-radius: 0 15% 15% 0;
    border: white 1px solid;
    padding-top: 20px;
    padding-bottom: 20px;
}

.news{
    width: 90%;
    position:relative;
    /* top:210px; */
    left:120px;
}

.news_list{
    display: inline;
    width : 49%;
    border: 1px solid;
    margin: 0 5px;
}


</style>
