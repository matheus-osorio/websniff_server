import Vue from 'vue'
import Router from 'vue-router'

import MainPage from './components/main/MainPage';
import SpecificPage from './components/specific/SpecificPage'


const routes = [
    {path:'/',name:'geral',component:MainPage},
    {path:'/:program',name:'especifico',component:SpecificPage} 
]

Vue.use(Router)

export default new Router({
    routes
})