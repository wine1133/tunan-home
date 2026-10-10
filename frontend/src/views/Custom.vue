<template>
  <div class="custom">
    <section class="page-hero">
      <div class="page-hero-bg" :style="bg(heroImg, 'rgba(20,16,12,0.55)')"></div>
      <div class="container page-hero-inner">
        <span class="eyebrow">CUSTOM</span>
        <h1>全屋定制</h1>
        <p>从一张草图，到一件专属实木家具</p>
      </div>
    </section>

    <section class="section steps">
      <div class="container">
        <span class="eyebrow">定制流程</span>
        <h2 class="section-title">五步，把想法变成现实</h2>
        <div class="steps-grid">
          <div v-for="(s, i) in steps" :key="i" class="step">
            <span class="step-no">{{ String(i + 1).padStart(2, '0') }}</span>
            <h3>{{ s.t }}</h3>
            <p>{{ s.d }}</p>
          </div>
        </div>
      </div>
    </section>

    <!-- 定制优势 -->
    <section class="section adv">
      <div class="container">
        <span class="eyebrow">定制优势</span>
        <h2 class="section-title">把空间交给专业的人</h2>
        <div class="adv-grid">
          <div v-for="a in advantages" :key="a.t" class="adv-item">
            <span class="adv-no">{{ a.no }}</span>
            <h3>{{ a.t }}</h3>
            <p>{{ a.d }}</p>
          </div>
        </div>
      </div>
    </section>
    <section class="section options">
      <div class="container options-grid">
        <div class="options-text">
          <span class="eyebrow">可定制项目</span>
          <h2 class="section-title">您的家，由您定义</h2>
          <p>
            尺寸、材质、颜色、五金、软包，每一项都可以按照您的空间与喜好调整。
            我们提供一对一设计顾问，全程陪伴直至安装交付。
          </p>
        </div>
        <div class="options-list">
          <div v-for="o in options" :key="o.t" class="option">
            <h4>{{ o.t }}</h4>
            <p>{{ o.d }}</p>
          </div>
        </div>
      </div>
    </section>

    <!-- 材质色板 -->
    <section class="section palette">
      <div class="container">
        <span class="eyebrow">材质色板</span>
        <h2 class="section-title">六种经典木色，随心而选</h2>
        <div class="palette-grid">
          <div v-for="c in palette" :key="c.name" class="swatch">
            <div class="swatch-color" :style="{ background: c.hex }"></div>
            <span>{{ c.name }}</span>
          </div>
        </div>
      </div>
    </section>

    <!-- 计价说明 -->
    <section class="section pricing">
      <div class="container">
        <span class="eyebrow">计价说明</span>
        <h2 class="section-title">透明报价，没有隐形增项</h2>
        <div class="pricing-grid">
          <div v-for="pr in pricing" :key="pr.t" class="pricing-item">
            <h3>{{ pr.t }}</h3>
            <p>{{ pr.d }}</p>
          </div>
        </div>
      </div>
    </section>
    <section class="section cases">
      <div class="container">
        <span class="eyebrow">定制案例</span>
        <h2 class="section-title">每一件，都是独一无二的</h2>
        <div class="cases-grid">
          <div v-for="c in cases" :key="c.t" class="case">
            <div class="case-img" :style="bg(c.img, 'rgba(20,16,12,0.2)')"></div>
            <h4>{{ c.t }}</h4>
            <p>{{ c.d }}</p>
          </div>
        </div>
      </div>
    </section>

    <section class="section faq">
      <div class="container faq-inner">
        <span class="eyebrow">常见问题</span>
        <h2 class="section-title">定制前，您可能想知道</h2>
        <div class="faq-list">
          <details v-for="f in faqs" :key="f.q">
            <summary>{{ f.q }}</summary>
            <p>{{ f.a }}</p>
          </details>
        </div>
      </div>
    </section>

    <section class="cta">
      <div class="cta-bg" :style="bg(ctaImg, 'rgba(20,16,12,0.6)')"></div>
      <div class="container cta-inner">
        <h2>开启您的专属定制</h2>
        <p>拨打 400-888-1988 或留下联系方式，顾问将在 1 小时内回复</p>
        <a href="/contact/" class="btn btn-primary">立即咨询</a>
      </div>
    </section>
  </div>
</template>

<script setup>
const bg = (url, overlay) => ({
  backgroundImage: `linear-gradient(${overlay}, ${overlay}), url('${url}')`,
  backgroundSize: 'cover',
  backgroundPosition: 'center',
})

const heroImg = 'https://images.unsplash.com/photo-1583847268964-b28dc8f51f92?auto=format&fit=crop&w=1800&q=80'
const ctaImg = 'https://images.unsplash.com/photo-1600210492486-724fe5c67fb0?auto=format&fit=crop&w=1800&q=80'

const steps = [
  { t: '需求沟通', d: '电话或到店，沟通风格、预算与使用需求。' },
  { t: '上门测量', d: '预约量尺，核对户型、管线与采光细节。' },
  { t: '方案设计', d: '出具 3D 效果图与报价清单，可多次修改。' },
  { t: '工厂生产', d: '确认下单后进入产线，全程可视频看厂。' },
  { t: '安装售后', d: '专业师傅送货安装，提供五年质保。' },
]

const options = [
  { t: '尺寸定制', d: '按空间毫米级定制，不规则户型也能充分利用。' },
  { t: '材质定制', d: '黑胡桃、白橡、白蜡、樱桃木等多种硬木可选。' },
  { t: '颜色定制', d: '本色、胡桃色、烟熏色等，支持色板打样确认。' },
  { t: '五金软包', d: '进口静音五金、多色布艺与真皮软包自由搭配。' },
]

const advantages = [
  { no: '01', t: '一对一设计', d: '专属设计顾问全程跟进，需求不落空。' },
  { no: '02', t: '3D 效果图', d: '下单前所见即所得，风格尺寸提前确认。' },
  { no: '03', t: '工厂直造', d: '无中间环节，生产进度可视频随时查看。' },
  { no: '04', t: '全程透明', d: '材质、工艺、价格一价全包，零隐形增项。' },
]

const palette = [
  { name: '黑胡桃色', hex: '#4a3526' },
  { name: '白橡本色', hex: '#d8c6a8' },
  { name: '烟熏色', hex: '#6b5b4a' },
  { name: '樱桃木色', hex: '#8c5a3c' },
  { name: '白蜡本色', hex: '#e5d8bd' },
  { name: '原木色', hex: '#c9a06a' },
]

const pricing = [
  { t: '按材质计价', d: '黑胡桃、白橡、白蜡等不同木种单价不同，先确认材质再报价。' },
  { t: '按尺寸计价', d: '超出标准尺寸部分按延米或平米核算，报价单逐项列明。' },
  { t: '一价全包', d: '确认方案后锁定总价，含生产、配送与安装，中途不加价。' },
]
const cases = [
  { t: '大平层整屋定制', d: '深圳 180㎡ 大平层，客厅、餐厨、卧室整体木作。', img: 'https://images.unsplash.com/photo-1600210492486-724fe5c67fb0?auto=format&fit=crop&w=800&q=80' },
  { t: '小户型收纳方案', d: '广州 68㎡ 两居，定制到顶衣柜与榻榻米收纳。', img: 'https://images.unsplash.com/photo-1616594039964-ae9021a400a0?auto=format&fit=crop&w=800&q=80' },
  { t: '别墅茶室书房', d: '佛山别墅地下室，整木茶室与满墙书柜。', img: 'https://images.unsplash.com/photo-1497366754035-f200968a6e72?auto=format&fit=crop&w=800&q=80' },
]

const faqs = [
  { q: '定制周期一般多久？', a: '标准款约 25 - 35 天，复杂定制 40 - 60 天，具体以方案确认为准。' },
  { q: '如何确定环保是否达标？', a: '我们使用水性漆与低醛板材，可提供第三方环保检测报告。' },
  { q: '外地可以定制吗？', a: '可以，支持全国上门测量、送货与安装，费用按城市单独核算。' },
  { q: '定制的价格怎么算？', a: '按材质、尺寸与工艺综合报价，确认方案后一价全包，无隐形增项。' },
]
</script>

<style scoped>
.page-hero { position: relative; color: #fff; padding: 190px 0 110px; }
.page-hero-bg { position: absolute; inset: 0; background-size: cover; background-position: center; }
.page-hero-inner { position: relative; }
.page-hero h1 { font-size: clamp(36px, 5vw, 58px); margin: 16px 0 12px; color: #fff; }
.page-hero p { color: rgba(255, 255, 255, 0.8); letter-spacing: 0.2em; }

.steps-grid { display: grid; grid-template-columns: repeat(5, 1fr); gap: 20px; margin-top: 48px; }
.step { border: 1px solid var(--line);  padding: 28px 22px; background: #fff; }
.step-no { font-family: var(--serif); font-size: 30px; color: var(--gold); }
.step h3 { margin: 14px 0 8px; font-size: 17px; }
.step p { color: var(--muted); font-size: 13px; }

.options { background: var(--bg-soft); }
.options-grid { display: grid; grid-template-columns: 1fr 1.2fr; gap: 64px; align-items: center; }
.options-text p { color: var(--muted); margin-top: 8px; }
.options-list { display: grid; grid-template-columns: 1fr 1fr; gap: 18px; }
.option { background: #fff;  padding: 24px; }
.option h4 { color: var(--gold-deep); margin-bottom: 8px; }
.option p { color: var(--muted); font-size: 13px; }

.cases { background: #fff; }
.cases-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 28px; margin-top: 44px; }
.case {  overflow: hidden; border: 1px solid var(--line); }
.case-img { height: 220px; background-size: cover; background-position: center; }
.case h4 { margin: 18px 20px 6px; }
.case p { margin: 0 20px 20px; color: var(--muted); font-size: 13px; }

.faq { background: var(--bg); }
.faq-inner { max-width: 820px; }
.faq-list { margin-top: 36px; }
details { border-bottom: 1px solid var(--line); }
summary { cursor: pointer; padding: 22px 8px; font-family: var(--serif); font-size: 17px; list-style: none; display: flex; justify-content: space-between; }
summary::after { content: "+"; color: var(--gold); font-size: 22px; }
details[open] summary::after { content: "−"; }
details p { padding: 0 8px 22px; color: var(--muted); font-size: 14px; }

.cta { position: relative; color: #fff; }
.cta-bg { position: absolute; inset: 0; background-size: cover; background-position: center; }
.cta-inner { position: relative; text-align: center; padding: 100px 0; }
.cta-inner h2 { color: #fff; font-size: clamp(24px, 3.4vw, 38px); }
.cta-inner p { color: rgba(255, 255, 255, 0.8); margin: 14px 0 28px; }

.adv { background: #fff; }
.adv-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 24px; margin-top: 40px; }
.adv-item { border: 1px solid var(--line); padding: 30px 26px; background: #fff; }
.adv-no { font-family: var(--serif); font-size: 26px; color: var(--gold); }
.adv-item h3 { margin: 14px 0 8px; font-size: 18px; }
.adv-item p { color: var(--muted); font-size: 13px; }

.palette { background: var(--bg-soft); }
.palette-grid { display: grid; grid-template-columns: repeat(6, 1fr); gap: 18px; margin-top: 40px; }
.swatch { text-align: center; }
.swatch-color { height: 110px; border: 1px solid var(--line); }
.swatch span { display: block; margin-top: 10px; font-size: 13px; color: var(--ink-soft); }

.pricing { background: #fff; }
.pricing-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 28px; margin-top: 40px; }
.pricing-item { border: 1px solid var(--line); padding: 30px; }
.pricing-item h3 { color: var(--gold-deep); margin-bottom: 10px; }
.pricing-item p { color: var(--muted); font-size: 13px; }

@media (max-width: 900px) {
  .adv-grid { grid-template-columns: 1fr 1fr; }
  .palette-grid { grid-template-columns: repeat(3, 1fr); }
  .pricing-grid { grid-template-columns: 1fr; }
}
@media (max-width: 560px) {
  .adv-grid, .palette-grid { grid-template-columns: 1fr 1fr; }
}
@media (max-width: 900px) {
  .steps-grid { grid-template-columns: repeat(2, 1fr); }
  .options-grid { grid-template-columns: 1fr; }
  .cases-grid { grid-template-columns: 1fr; }
}
@media (max-width: 560px) {
  .steps-grid { grid-template-columns: 1fr; }
}
</style>