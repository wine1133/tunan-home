import { createApp, h } from 'vue'
import PageShell from '../layout/PageShell.vue'
import Contact from '../views/Contact.vue'

createApp({
  render: () => h(PageShell, null, { default: () => h(Contact) }),
}).mount('#app')