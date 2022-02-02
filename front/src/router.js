import Vue from 'vue'
import Router from 'vue-router'

import MainPage from './components/main/MainPage';
import SpecificPage from './components/specific/SpecificPage'
import Configuration from './components/configuration/Configuration'
import ConnectionPage from './components/connection/ConnectionPage'

const routes = [
    {path:'/',name:'geral',component:MainPage},
    {path:'/configuration',name:'configuracao',component:Configuration}, 
    {path:'/:program/:connection',name:'conexao',component:ConnectionPage}, 
    {path:'/:program',name:'especifico',component:SpecificPage} 
]

Vue.use(Router)

export default new Router({
    routes
})