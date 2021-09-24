<template>
    <div class="row">
        <div class="col-md-1"></div>
        
        <HogaPrice class="col-md-2" v-bind:Price="bidPrice"></HogaPrice>
        <HogaStandard class="col-md-1"></HogaStandard>
        <HogaVolume class="col-md-2" v-bind:Volume="bidVolume"></HogaVolume>
        
        <HogaPrice class="col-md-2" v-bind:Price="askPrice"></HogaPrice>
        <HogaStandard class="col-md-1"></HogaStandard>
        <HogaVolume class="col-md-2" v-bind:Volume="askVolume"></HogaVolume>
    </div>
</template>

<script>
import HogaStandard from "../components/HogaStandard.vue"
import HogaVolume from "../components/HogaVolume.vue"
import HogaPrice from "../components/HogaPrice.vue"

export default {
    name: "Hoga",
    components:{
        HogaStandard,
        HogaVolume,
        HogaPrice,
    },
    props:{
        bidVolume: Array,
        bidPrice: Array,
        askVolume: Array,
        askPrice: Array,
    },
    data(){
        return{

        }
    },
    methods:{

    },
}
</script>

<style>

</style>