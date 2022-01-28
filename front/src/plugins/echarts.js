import Vue from 'vue';
import Echarts from 'vue-echarts';
import 'echarts/dist/echarts.js';
import 'echarts/lib/chart/line'
import 'echarts/lib/chart/bar'
import 'echarts/lib/component/tooltip'
import 'echarts/lib/component/title'
import 'echarts/lib/component/legend'

Vue.component('e-chart', Echarts);