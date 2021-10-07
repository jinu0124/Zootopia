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
                <h2 class="featurette-heading" style="font-size: 70px" >주투피아</h2>
                <h3 class="featurette-heading-info" style="font-size: 50px; color: rgba(25, 228, 167, 0.877);" >: 주식 TO UTOPIA ! </h3>
                <br>
                <p class="lead" style="font-size: 30px" >모든 사람이 현명한 투자를 하는 그날까지, <br> 이상향을 위한 주식 데이터 분석 플랫폼 
                <a style="font-weight: bolder; font-size: 34px">'주투피아'</a>를 시작해보세요.  <br></p>
                <p style="font-size: 24px">Enjoy Stock Investment Utopia, Study Stock Investment Together !</p>
            </div> 
            <br>
        </div>
        <br><br><br>
        <hr class = "hrstyle">

        <div class="row featurette">
            <div class="col-md-4">
                <div class="hover_effect_box hover_effect_5">
                    <div class="content_bg">
                        <img src="../news_view.png" class="img2" />
                    </div>
                    <div class="caption">
                        <div class="caption_desc">
                        NEWS Text<br>
                        Analysis
                        </div>
                        <button @click=moveToNews() class="caption_button"> Go! </button> 
                    </div>
                </div>
            </div>
            <div class="col-md-8" style="margin-top: 100px;">
                <h2 class="featurette-heading"><a style="font-size: 95px">1 </a> <a style="font-size: 50px">뉴스기사 분석 서비스</a> <span class="text-muted"> +Word Cloud</span></h2>
                <p class="lead" style="font-size: 26px; margin-left: 30px"><a style="font-weight: bolder; font-size: 31px;"> What is the most important to investment? &nbsp; &nbsp;</a>
                        <a style="font-weight: bold; font-size: 30px;">Information <a style="font-weight: normal;">and</a> <a style="font-weight: bold; font-size: 30px;">Accuracy</a></a> <br>
                        뉴스 데이터 분석 시스템은 실시간으로 가장 정확한 뉴스 정보를 신속히 제공하여 투자를 위한 분석 시간을 단축시켜줍니다. <br>
                        또한, 자연어 감정 분석을 통해 시각적으로 보다 쉽게 데이터를 이해할 수 있도록 돕습니다.</p>
            </div>  
        </div>
        <hr class = "hrstyle">

        <div class="row featurette">
            <div class="col-md-8" style="text-align:right; margin-top: 100px;  ">
                <h2 class="featurette-heading"> <span class="text-muted">  Dart Info+ &nbsp; </span> <a style="font-size: 50px">주식 종목 예측&nbsp; </a> <a style="font-size: 95px"> 2</a> </h2>
                <p class="lead" style="font-size: 26px"> <a style="font-weight: bolder; font-size: 29px;">그래도 투자가 망설여지시나요? 뉴스 분석만으로는 부족하다고 느껴지시나요?</a> <br>
                        증권사와 연계된 주식 종목 실시간 거래와 기업 분석 데이터를 통해 기업 정보를 얻고,<br>
                        복합 데이터 기반 미래 주가 예측 시스템의 도움을 받아 보다 안정적으로 미래를 위한 투자에 임해보세요!</p>
            </div>
            <div class="col-md-4">
                <div class="hover_effect_box hover_effect_5">
                    <div class="content_bg">
                        <img src="../stock_view.jpg" class="img2"/>
                    </div>
                    <div class="caption">
                        <div class="caption_desc">
                        STOCK Chart<br>
                        Analysis
                        </div>
                        <button @click=moveToStock() class="caption_button"> Go! </button> 
                    </div>
                </div>
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
            this.$router.push({name: "News"}).catch(() => {})
        },
        moveToStock(){
            this.$router.push({name: "Stock"}).catch(() => {})
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
img.img2{
    filter: drop-shadow(5px 5px 5px #0a4437e5); }

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
.hover_effect_box {
    margin: 10px;
    border: 10px solid #f3f3f3;
    overflow: hidden;
    position: relative;
    text-align: center;
    -webkit-box-shadow: 1px 1px 2px #e6e6e6;
    -moz-box-shadow: 1px 1px 2px #e6e6e6;
    box-shadow: 1px 1px 2px #e6e6e6;
    cursor: default;
    background: #fff;
    box-sizing: initial;
 }
 .hover_effect_box * {
    box-sizing: initial;
 }

 .hover_effect_box .caption
 , .hover_effect_box .mask  {
    width: 100%;
    height: 100%;
    position: absolute;
    overflow: hidden;
    top: 0;
    left: 0;
 }
 .hover_effect_box .content_bg {
    display: block;
    position: relative;
 }
 .hover_effect_box .caption_title {
    text-transform: uppercase;
    color: #fff;
    text-align: center;
    position: relative;
    font-size: 17px;
    padding: 10px;
    background: rgba(0, 0, 0, 0.8);
    margin: 20px 0 0 0;
 }
 .hover_effect_box .caption_desc {
    margin-top: 60px;
    font-size: 40px;
    line-height: 1.5;
    position: relative;
    color: #fff;
    padding: 30px 20px 40px;
    text-align: center;
 }
 .hover_effect_box .caption_button {
    display: inline-block;
    text-decoration: none;
    padding: 7px 14px;
    background: #000;
    color: #fff;
    text-transform: uppercase;
    -webkit-box-shadow: 0 0 1px #000;
    -moz-box-shadow: 0 0 1px #000;
    box-shadow: 0 0 1px #000;
 }
 .hover_effect_box .caption_link:hover {
    -webkit-box-shadow: 0 0 5px #000;
    -moz-box-shadow: 0 0 5px #000;
    box-shadow: 0 0 5px #000;
 }

.hover_effect_5 .content_bg {
    -webkit-transition: all 0.3s ease-in-out;
    -moz-transition: all 0.3s ease-in-out;
    -o-transition: all 0.3s ease-in-out;
    -ms-transition: all 0.3s ease-in-out;
    transition: all 0.3s ease-in-out;
 }
 .hover_effect_5 .caption {
    background-color: rgba(53, 82, 80, 0.452);
    -webkit-transform: translateX(-500px);
    -moz-transform: translateX(-500px);
    -o-transform: translateX(-500px);
    -ms-transform: translateX(-500px);
    transform: translateX(-500px);
    -ms-filter: "progid: DXImageTransform.Microsoft.Alpha(Opacity=100)";
    filter: alpha(opacity=100);
    opacity: 1;
    -webkit-transition: all 0.3s ease-in-out;
    -moz-transition: all 0.3s ease-in-out;
    -o-transition: all 0.3s ease-in-out;
    -ms-transition: all 0.3s ease-in-out;
    transition: all 0.3s ease-in-out;
 }

 .hover_effect_5:hover .caption {
    -webkit-transform: translateX(0px);
    -moz-transform: translateX(0px);
    -o-transform: translateX(0px);
    -ms-transform: translateX(0px);
    transform: translateX(0px);
 }

 .hover_effect_5:hover .caption_desc {
    -ms-filter: "progid: DXImageTransform.Microsoft.Alpha(Opacity=100)";
    filter: alpha(opacity=100);
    opacity: 1;
 }

 .content_bg{
    position: relative;
    width: 100%;
    height: 0;
    padding-bottom: 100%;
    overflow: hidden;
 }

 .content_bg .img2{
     position: absolute;
     top: 0;
     left: 0;
     width: 100%;
     height: 100%;
 }
</style>
