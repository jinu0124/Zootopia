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
            <div class="lb-button" >
                <button @click=moveToNews() >주투피아 시작하기</button>
            </div>
            <div class="lb-image">
                <img style="width: 100%" src="../business-ga781e90a3_1920.jpg">
            </div>
        </div>
        <br>
        <br>
        <div class="row">
            <div style="text-align:center; width:100%" class="col col-md-8">
                <h2 class="featurette-heading" >주투피아 <span class="text-muted">  : 주식 투자 유토피아</span></h2>
                <br>
                <p class="lead">주저리 주저리 설명 <br> Some great placeholder content for the first featurette here. Imagine some exciting prose here.</p>
            </div>  
            <br>
        </div>
        <br><br><br>
        <hr class = "hrstyle">

        <div class="row featurette">
            <div class="col-img col-md-4">
                <img src="../news_view.jpg" class="bd-placeholder-img bd-placeholder-img-lg featurette-image img-fluid mx-auto" width="500" height="500"/>
            </div>
            <div class="col col-md-8">
                <h2 class="featurette-heading">1. 뉴스기사 분석 서비스 <span class="text-muted">  + Word Cloud</span></h2>
                <p class="lead">Some great placeholder content for the first featurette here. Imagine some exciting prose here.</p>
            </div>  
        </div>
        <hr class = "hrstyle">

        <div class="row featurette">
            <div class="col-md-8">
                <h2 class="featurette-heading">2. 주식 종목 예측 <span class="text-muted">  + Dart Info</span></h2>
                <p class="lead">Another featurette? Of course. More placeholder content here to give you an idea of how this layout would work with some actual real-world content in place.</p>
            </div>
            <div class="col-md-4">
                <svg class="bd-placeholder-img bd-placeholder-img-lg featurette-image img-fluid mx-auto" width="500" height="500" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Placeholder: 500x500" preserveAspectRatio="xMidYMid slice" focusable="false"><title>Placeholder</title><rect width="100%" height="100%" fill="#eee"/><text x="50%" y="50%" fill="#aaa" dy=".3em">500x500</text></svg>

            </div>
        </div>
        <hr class = "hrstyle">
        <footer>
            <p style="float:right; margin-right:20px" ><a href="#">Back to top ▲</a></p>
            <p style="margin-left:5%" >&copy; 2021.09 – 2021.10 주투피아</p>
        </footer>
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
    methods:{
        moveToNews(){
            console.log("잘 눌렀니?")
            this.$router.push({name: "News"}).catch(() => {})
        },
    },
    mounted(){
        setInterval(() => {
            this.now = this.$moment(new Date()).format("DD MMM YYYY HH:mm:ss")
        }, 1000)
    }
}
</script>
<style scoped>
button{
  background:#0ee0afc0;
  color:#fff;
  border:none;
  position:relative;
  height:60px;
  font-size:1.6em;
  padding:0 2em;
  cursor:pointer;
  transition:800ms ease all;
  outline:none;
  font-weight: bold;
}
button:hover{
  background:#fff;
  color:#1AAB8A;
}
button:before,button:after{
  content:'';
  position:absolute;
  top:0;
  right:0;
  height:2px;
  width:0;
  background: #1AAB8A;
  transition:400ms ease all;
}
button:after{
  right:inherit;
  top:inherit;
  left:0;
  bottom:0;
}
button:hover:before,button:hover:after{
  width:100%;
  transition:800ms ease all;
}
.lb-wrap {
  width: 100%;
  position: relative;
}
.lb-wrap img {
  width: 100%;
}
.lb-text {
  width: 100%;
  padding: 10px 20px;
  border-radius: 10px;
  text-align: center;
  color:white;
  position: absolute;
  top: 30%;
  left: 50%;
  transform: translate(-50%, -50%);
}
.lb-button {
  width: 100%;
  padding: 10px 20px;
  border-radius: 10px;
  text-align: center;
  color:white;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.featurette{
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
