<template>
    <div class="stock_info" style="">
        <p style="font-size: 24px;">긍정 뉴스 <span style="font-size: 16px; color: blue;">Positive</span> </p>
        
        <ul>
            <li :class="i" v-for="(item, i) in link" v-bind:key="item"><a :href="item" target="_blank">{{ positiveNews[i] }}</a></li>
        </ul>
    </div>
</template>

<script>
export default {   
    name: "PositiveNews",
    props:{
        positiveNews: Array,
        link: Array
    },
    data(){
        return{
        }
    },
    methods:{

    },
    watch:{
        positiveNews(){

        },
        link(){

        }
    },
    computed:{
        
    }
}
</script>

<style>
/* .info_title{
    color: rgb(158, 152, 152);
    font-size: 0.6em !important;
}
.info_title ~p a{
    width : 40%;
    text-overflow: ellipsis;
} */

.stock_info{
    padding: 0;
    margin: 0;
    height: 100%;
    overflow-y:scroll;
    font-family: 'Gothic A1', sans-serif;
}

.stock_info>ul{
    padding: 0;
    margin: 0;
    font-size: 1.0em;
    text-align:center;
    
}

.stock_info>ul>li:not(:last-child){
    margin: 0;
    float:center;
    border-bottom:rgb(107, 156, 179) 1px solid;
}

a { 
    text-decoration:none;
 } 

ul{
   list-style:none;
}

li{
    padding: 10px;
}

</style>