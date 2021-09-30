import wordcloud from "vue-wordcloud"

export default {
    name: 'WordCloud',
    components: {
      wordcloud
    },
    methods: {
      wordClickHandler(name, value, vm) {
        console.log('wordClickHandler', name, value, vm);
      }
    },
    data() {
      return {
        myColors: ['#1f77b4', '#629fc9', '#94bedb', '#c9e0ef'],
        defaultWords: [{
            "name": "Cat",
            "value": 26
          },
          {
            "name": "fish",
            "value": 19
          },
          {
            "name": "things",
            "value": 18
          },
          {
            "name": "look",
            "value": 16
          },
          {
            "name": "two",
            "value": 15
          },
          {
            "name": "fun",
            "value": 9
          },
          {
            "name": "know",
            "value": 9
          },
          {
            "name": "good",
            "value": 9
          },
          {
            "name": "play",
            "value": 6
          }
        ]
      }
    }
  }