<template>
    <div class="left-pad">
        <div class="wrapper">
            <div class="search">
            <div name="cse" id="searchbox_demo" class="searchform row" autocomplete="off">
                <div class="col-md-10">
                    <input style="margin-right:0" type="text" placeholder="종목검색" class="searchbox form-control" v-model=searchWord v-on:keyup.enter="onOmit()"/>
                </div>
                <div class="col-md-2">
                    <button style="border: rgb(0, 180, 96) 2px solid;" class="btn" @click="onOmit()">Search</button>
                </div>
            </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "Searchbar",
    data(){
        return{
            searchWord: "",
        }
    },
    methods:{
        onOmit(){
            console.log(this.searchWord)
            this.$emit("searchStock", this.searchWord)
        },
    },
}
</script>

<style>
input{
    height:40px;
    width:150px;
}
button{
  border: rgb(0, 180, 96) 2px solid;
  background:#05a07cee;
  color:#fff;
  border:none;
  position:relative;
  height:40px;
  font-size:1.6em;
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
button.btn{
    width:200px;
}
.left-pad{
    /* position: fixed; */
    width: 100%;
    padding-top:50px;
    padding-left: 100px;
}
</style>