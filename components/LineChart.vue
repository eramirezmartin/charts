<script>
import { Line } from 'vue-chartjs'

export default {
  extends: Line,
  props: {
    data: {
      type: Object,
      required: true
    }
  },
  watch: {
    data() {
      this.render()
    }
  },
  mounted() {
    this.render()
  },

  methods: {
    render() {
      if (this.data) {
        this.renderChart(
          this.getChartData(this.data),
          this.getChartOptions(this.data.title)
        )
      }
    },
    getChartOptions(title) {
      return {
        responsive: true,
        legend: {
          display: false
        },
        labels: {
          display: false
        },
        title: {
          display: true,
          text: title
        },
        scales: {
          yAxes: [
            {
              ticks: {
                beginAtZero: false
              }
            }
          ],
          xAxes: [
            {
              ticks: {
                display: false
              }
            }
          ]
        }
      }
    },
    getChartData(data) {
      return {
        labels: data.labels,
        datasets: [
          {
            borderColor: data.color,
            data: data.data
          }
        ]
      }
    }
  }
}
</script>
