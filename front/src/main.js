import Vue from 'vue'
import App from './App.vue'
import router from './router'

import 'bootstrap/dist/css/bootstrap.min.css'
import '@fortawesome/fontawesome-free/css/all.min.css'

import VueECharts from "vue-echarts";
import "@vue/composition-api";
import "echarts";
import 'echarts/dist/echarts.js';
import 'echarts/lib/chart/line'
import 'echarts/lib/chart/bar'
import 'echarts/lib/component/tooltip'
import 'echarts/lib/component/title'
import 'echarts/lib/component/legend'

Vue.config.productionTip = false

Vue.component("e-chart", VueECharts);


Vue.config.productionTip = false

new Vue({
  router,
  VueECharts,
  render: h => h(App),
}).$mount('#app')
