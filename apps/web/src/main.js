import { createApp } from 'vue'
import router from './router';
import App from './app/App.vue'
import './app/main.css'

createApp(App).use(router).mount('#app')
