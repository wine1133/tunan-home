import { createApp, h } from 'vue'
import PageShell from '../layout/PageShell.vue'
import Custom from '../views/Custom.vue'

createApp({
  render: () => h(PageShell, null, { default: () => h(Custom) }),
}).mount('#app')