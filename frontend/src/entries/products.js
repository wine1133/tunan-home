import { createApp, h } from 'vue'
import PageShell from '../layout/PageShell.vue'
import Products from '../views/Products.vue'

createApp({
  render: () => h(PageShell, null, { default: () => h(Products) }),
}).mount('#app')