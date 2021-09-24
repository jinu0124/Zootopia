<template>
    <div class="col-md-4 stock_info" style="">
        <ul>
            <li><div class="info_title">현재가</div>76200</li>
            <li><div class="info_title">시가</div>76000</li>
            <li><div class="info_title">고가</div>76800</li>
            <li><div class="info_title">저가</div>75600</li>
            <li><div class="info_title">거래량(주)</div>1157648</li>
        </ul>
    </div>
</template>

<script>
export default {   
    name: "StockInfo",
    data(){
        return{

        }
    },
    methods:{

    },
}
</script>

<style>
.stock_info>ul>li:not(:last-child){
    font-size: 1.5em;
    text-align:center;
    float:center;
    padding-bottom: 15px;
    border-bottom:rgb(185, 178, 178) 1px solid;
}
.stock_info>ul>li:not(:first-child){
    padding-top: 10px;
}
.stock_info>ul>li:not(last-child){
    font-size: 1.5em;
    text-align:center;
    float:center;
}

.info_title{
    color: rgb(158, 152, 152);
    font-size: 0.6em;
}
</style>