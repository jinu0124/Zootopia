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
        <br>
        <div class="row-featurette">
            <div class="col-img">
                <svg class="bd-placeholder-img bd-placeholder-img-lg featurette-image img-fluid mx-auto" width="500" height="500" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Placeholder: 500x500" preserveAspectRatio="xMidYMid slice" focusable="false"><title>Placeholder</title><rect width="100%" height="100%" fill="#eee"/><text x="50%" y="50%" fill="#aaa" dy=".3em">500x500</text></svg>
                <div class="col">
                <h2 class="featurette-heading">1. 뉴스기사 분석 서비스 <span class="text-muted">  + Word Cloud</span></h2>
                <p class="lead">Some great placeholder content for the first featurette here. Imagine some exciting prose here.</p>
                </div>  
            </div>
        </div>
        <hr class = "hrstyle">

        <div class="row-featurette">
            <div class="col">
                <h2 class="featurette-heading">2. 주식 종목 예측 <span class="text-muted">  + Dart Info</span></h2>
                <p class="lead">Another featurette? Of course. More placeholder content here to give you an idea of how this layout would work with some actual real-world content in place.</p>
            </div>
            <div class="col-md-5 order-md-1">
                <svg class="bd-placeholder-img bd-placeholder-img-lg featurette-image img-fluid mx-auto" width="500" height="500" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Placeholder: 500x500" preserveAspectRatio="xMidYMid slice" focusable="false"><title>Placeholder</title><rect width="100%" height="100%" fill="#eee"/><text x="50%" y="50%" fill="#aaa" dy=".3em">500x500</text></svg>

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
.row-featurette{
  position: relative;
  left: 5%;
}

hr.hrstyle{
    margin-left: 5%;
    border: 2px;
    height: 1px;
    background-image: linear-gradient(to right, rgba(0, 0, 0, 0), rgba(0, 0, 0, 0.75), rgba(0, 0, 0, 0));
}
</style>
