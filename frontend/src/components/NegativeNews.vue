<template>
    <div class="stock_info" style="">
        <p>부정 뉴스</p>
        <p>Negative</p>
        <ul>
            <li><div class="info_title">뉴스1</div>&nbsp;{{negativeNews.First}}&nbsp;</li>
            <li><div class="info_title">뉴스2</div>&nbsp;{{negativeNews.Second}}&nbsp;</li>
            <li><div class="info_title">뉴스3</div>&nbsp;{{negativeNews.Third}}&nbsp;</li>
            <li><div class="info_title">뉴스4</div>&nbsp;{{negativeNews.Fourth}}&nbsp;</li>
        </ul>
    </div>
</template>

<script>
export default {   
    name: "NegativeNews",
    data(){
        return{
            negativeNews: Object
        }
    },
    methods:{

    },
    watch:{
        negativeNews(){

        }
    },
    computed:{
        
    }
}
</script>

<style>
.info_title{
    color: rgb(158, 152, 152);
    font-size: 0.6em !important;
    /* width: 100%; */
}

.stock_info>ul>li:not(:last-child){
    font-size: 1.5em;
    text-align:center;
    float:center;
    padding-bottom: 15px;
    border-bottom:rgb(107, 156, 179) 1px solid;
}
.stock_info>ul>li:not(:first-child){
    padding-top: 10px;
}
.stock_info>ul>li:not(last-child){
    font-size: 1.5em;
    text-align:center;
    float:center;
}


</style>