<template>
    <div>
        <div class="row">
            <Sidebar></Sidebar>
        </div>
        <div class="lb-wrap">
            <div class="lb-text">
                <h1 style="padding-left:10px; font-size: 100px;">WELCOME</h1>
                <br>
                <h2 style="font-size: 70px;">STOCK INVESTMENT UTOPIA</h2>
            </div>
            <div class="lb-image">
                <img style="width: 100%" src="../business-ga781e90a3_1920.jpg">
            </div>
        </div>
    </div>
</template>
<script>
/* eslint-disable */
import Sidebar from "../components/Sidebar.vue"
import _axios from "../api/default"

export default {
    name: "Home",
    components:{
        Sidebar,
    },
    data(){
        return{
            
        }
    },
    method:{
        
    },
    mounted(){
        setInterval(() => {
            this.now = this.$moment(new Date()).format("DD MMM YYYY HH:mm:ss")
        }, 1000)
    }
}
</script>
<style scoped>
.lb-wrap {
  width: 100%;
  position: relative;
}
.lb-wrap img {
  width: 100%;
}
.lb-text {
  padding: 10px 20px;
  border-radius: 10px;
  text-align: center;
  color:white;
  position: absolute;
  top: 30%;
  left: 50%;
  transform: translate(-50%, -50%);
}
</style>
