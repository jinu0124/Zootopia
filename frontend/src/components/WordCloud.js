import wordcloud from 'vue-wordcloud'

export default {
    name: 'WordCloud',
    props:{
        data: [],
        color: [],
        wordClick: Function,
    },
    components: {
      wordcloud
    },
    
    methods: {
        wordClickHandler(name, value, vm) {
          this.$emit(console.log('wordClickHandler', name, value, vm));
        }
      
    },
    data() {
      return {
        
      }
    }
  }