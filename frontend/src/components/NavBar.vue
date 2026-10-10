<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const scrolled = ref(false)
const open = ref(false)
const current = ref('/')

const links = [
  { path: '/', label: '首页' },
  { path: '/products/', label: '产品' },
  { path: '/factory/', label: '工厂' },
  { path: '/custom/', label: '定制' },
  { path: '/contact/', label: '联系' },
]

const isActive = (path) => {
  if (path === '/') return current.value === '/'
  return current.value.startsWith(path)
}

const onScroll = () => { scrolled.value = window.scrollY > 40 }

onMounted(() => {
  current.value = window.location.pathname
  window.addEventListener('scroll', onScroll)
  onScroll()
})
onUnmounted(() => window.removeEventListener('scroll', onScroll))
</script>

<template>
  <header class="nav" :class="{ scrolled: scrolled || open }">
    <div class="nav-inner container">
      <a href="/" class="brand" @click="open = false">
        <svg class="brand-mark" viewBox="0 0 64 64" aria-hidden="true">
          <rect width="64" height="64" fill="#b28a5a"/>
          <rect x="6" y="6" width="52" height="52" fill="none" stroke="#ffffff" stroke-opacity="0.38" stroke-width="1.5"/>
          <text x="32" y="47" text-anchor="middle" font-family="Noto Serif SC, Songti SC, STSong, SimSun, serif" font-size="38" fill="#ffffff">兔</text>
        </svg>
        <span class="brand-text">
          <span class="brand-cn">兔南家居</span>
          <span class="brand-en">TUNAN HOME</span>
        </span>
      </a>

      <nav class="menu" :class="{ open }">
        <a
          v-for="l in links"
          :key="l.path"
          :href="l.path"
          class="menu-link"
          :class="{ active: isActive(l.path) }"
          @click="open = false"
        >
          {{ l.label }}
        </a>
        <a class="menu-tel" href="tel:400-888-1988">400-888-1988</a>
      </nav>

      <button class="burger" :aria-label="open ? '关闭菜单' : '打开菜单'" @click="open = !open">
        <span></span><span></span><span></span>
      </button>
    </div>
  </header>
</template>

<style scoped>
.nav {
  position: fixed;
  inset: 0 0 auto 0;
  z-index: 100;
  transition: background 0.35s ease, box-shadow 0.35s ease;
  background: transparent;
  color: #fff;
}
.nav.scrolled {
  background: rgba(255, 255, 255, 0.96);
  box-shadow: 0 1px 0 var(--line);
  color: var(--ink);
}
.nav-inner {
  height: 82px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.brand { display: flex; flex-direction: row; align-items: center; gap: 12px; line-height: 1.15; }
.brand-mark { width: 40px; height: 40px; flex: none; }
.brand-text { display: flex; flex-direction: column; }
.brand-cn {
  font-family: var(--serif);
  font-size: 22px;
  letter-spacing: 0.14em;
  font-weight: 600;
}
.brand-en { font-size: 10px; letter-spacing: 0.32em; opacity: 0.75; }
.menu { display: flex; align-items: center; gap: 38px; }
.menu-link {
  position: relative;
  font-size: 15px;
  letter-spacing: 0.12em;
  padding: 6px 2px;
}
.menu-link::after {
  content: "";
  position: absolute;
  left: 0;
  bottom: 0;
  width: 0;
  height: 1px;
  background: var(--gold);
  transition: width 0.3s ease;
}
.menu-link:hover::after,
.menu-link.active::after { width: 100%; }
.menu-tel {
  margin-left: 10px;
  padding: 9px 18px;
  border: 1px solid currentColor;
  font-size: 13px;
  letter-spacing: 0.08em;
}
.burger { display: none; background: none; border: 0; cursor: pointer; width: 30px; height: 24px; position: relative; }
.burger span {
  position: absolute;
  left: 0;
  width: 100%;
  height: 2px;
  background: currentColor;
  transition: all 0.3s ease;
}
.burger span:nth-child(1) { top: 2px; }
.burger span:nth-child(2) { top: 11px; }
.burger span:nth-child(3) { top: 20px; }

@media (max-width: 900px) {
  .burger { display: block; color: #fff; }
  .nav.scrolled .burger { color: var(--ink); }
  .menu {
    position: fixed;
    top: 82px;
    left: 0;
    right: 0;
    flex-direction: column;
    align-items: flex-start;
    gap: 0;
    background: #fff;
    color: var(--ink);
    padding: 12px 0 20px;
    box-shadow: 0 12px 30px rgba(0, 0, 0, 0.08);
    transform: translateY(-130%);
    transition: transform 0.3s ease;
  }
  .menu.open { transform: translateY(0); }
  .menu-link { padding: 14px 6vw; font-size: 16px; width: 100%; border-bottom: 1px solid var(--line); }
  .menu-tel { margin: 16px 6vw 0; color: var(--gold-deep); }
}
</style>