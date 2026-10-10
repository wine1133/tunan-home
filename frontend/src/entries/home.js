import { createApp, h } from 'vue'
import PageShell from '../layout/PageShell.vue'
import Home from '../views/Home.vue'

createApp({
  render: () => h(PageShell, null, { default: () => h(Home) }),
}).mount('#app')