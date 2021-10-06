<template>
    <div class="stock_info" style="">
        <p style="font-size: 24px;">부정 뉴스 <span style="font-size: 16px; color: red;">Negative</span> </p>
        
        <ul>
            <li :class="i" v-for="(item, i) in link" v-bind:key="item"><a v-bind:style="styleObject" :href="item" target="_blank">{{ negativeNews[i] }}</a></li>
        </ul>
    </div>
</template>

<script>
export default {   
    name: "NegativeNews",
    props:{
        negativeNews: Array,
        link: Array
    },
    data(){
        return{
            styleObject: {
                color: 'red'
            }
        }
    },
    methods:{

    },
    watch:{
        negativeNews(){

        },
        link(){

        }
    },
    computed:{
        
    }
}
</script>

<style scoped>
a {
    color : red !important;
}


</style>