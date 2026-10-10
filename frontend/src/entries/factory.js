import { createApp, h } from 'vue'
import PageShell from '../layout/PageShell.vue'
import Factory from '../views/Factory.vue'

createApp({
  render: () => h(PageShell, null, { default: () => h(Factory) }),
}).mount('#app')