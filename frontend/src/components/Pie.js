import { Pie } from "vue-chartjs";

export default {
  name: "Pie",
  extends: Pie,
  data() {
    return {
      stats: [],
      chartdata: {
        labels: [],
        datasets: [
          {
            label: [],
            data: [],
            backgroundColor: [],
          },
        ],
      },
      options: {
        hoverBorderWidth: 20,
        responsive: true,
        maintainAspectRatio: false,
      },
    };
  },
  mounted() {
    this.renderChart(this.chartdata, this.options);
  },
  created() {
    this.stats = this.$store.state.categories;
    const obj = this.chartdata.datasets[0];

    for (const stat of this.stats) {
      this.chartdata.labels.push(stat.title);
      obj.label.push(stat.title);
      obj.data.push(stat.value);
      obj.backgroundColor.push(stat.backgroundColor);
    }
  },
};