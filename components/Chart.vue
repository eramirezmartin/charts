<script>
import { Pie } from 'vue-chartjs'

const chartColors = {
  red: 'rgb(255, 0, 0)',
  orange: 'rgb(255, 159, 64)',
  yellow: 'rgb(255, 205, 86)',
  green: 'rgb(75, 192, 192)',
  blue: 'rgb(54, 162, 235)',
  purple: 'rgb(153, 102, 255)',
  grey: 'rgb(201, 203, 207)'
}

export default {
  extends: Pie,
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
          display: true,
          position: 'top',
          fullWidth: true,
          labels: {
            fontSize: 16
          }
        },
        title: {
          display: true,
          text: title
        },
        scales: {
          yAxes: [
            {
              ticks: {
                beginAtZero: true
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
            label: 'Income',
            backgroundColor: [
              chartColors.red,
              chartColors.orange,
              chartColors.yellow,
              chartColors.blue,
              chartColors.green,
              chartColors.purple
            ],
            data: data.data
          }
        ]
      }
    }
  }
}
</script>
