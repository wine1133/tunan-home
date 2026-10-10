<template>
  <div class="home">
    <!-- Hero -->
    <section class="hero">
      <div
        v-for="(s, i) in slides"
        :key="i"
        class="hero-bg"
        :class="{ active: i === current }"
        :style="bg(s.img, 'rgba(20,16,12,0.55)')"
      ></div>
      <transition name="fade" mode="out-in">
        <div class="hero-inner container" :key="current">
          <span class="hero-eyebrow">{{ slides[current].eyebrow }}</span>
          <h1>{{ slides[current].title }}</h1>
          <p class="hero-sub">{{ slides[current].sub }}</p>
          <div class="hero-actions">
            <a :href="slides[current].btnLink" class="btn btn-primary">{{ slides[current].btnText }}</a>
            <a :href="slides[current].ghostLink" class="btn btn-ghost">{{ slides[current].ghostText }}</a>
          </div>
        </div>
      </transition>
      <button class="hero-arrow prev" aria-label="上一张" @click="prev">‹</button>
      <button class="hero-arrow next" aria-label="下一张" @click="next">›</button>
      <div class="hero-dots">
        <button v-for="(s, i) in slides" :key="i" class="dot" :class="{ active: i === current }" :aria-label="'第 ' + (i + 1) + ' 张'" @click="go(i)"></button>
      </div>
      <div class="hero-stats container">
        <div class="stat"><strong>18</strong><span>年专注制造</span></div>
        <div class="stat"><strong>3.6 万㎡</strong><span>现代化厂房</span></div>
        <div class="stat"><strong>120+</strong><span>台生产设备</span></div>
        <div class="stat"><strong>500+</strong><span>合作经销商</span></div>
      </div>
    </section>

    <!-- 品牌理念 -->
    <section class="section intro">
      <div class="container intro-grid">
        <div class="intro-media">
          <div class="intro-img main" :style="bg(imgWood, 'rgba(0,0,0,0.12)')"></div>
          <div class="intro-img sub" :style="bg(imgSofa, 'rgba(0,0,0,0.10)')"></div>
        </div>
        <div class="intro-text">
          <span class="eyebrow">品牌理念</span>
          <h2 class="section-title">少一点中间环节，多一点实在品质</h2>
          <p>
            兔南家居深耕家具制造十八年，始终以“工厂直营”为核心。从北美红橡、黑胡桃到优质白蜡木，
            原料直接采购、车间直接生产、成品直接发货，把传统渠道里的层层加价，还给真正需要它的人。
          </p>
          <p>
            我们相信，高端不等于昂贵。所谓轻奢，是恰到好处的用料、克制而耐看的线条，
            以及经得起日常使用的扎实工艺。
          </p>
          <ul class="intro-list">
            <li>严选北美进口硬木，含水率控制在 8% - 12%</li>
            <li>榫卯 + 进口五金双重加固，承重与耐用兼顾</li>
            <li>德国水性漆涂装，环保等级优于国标</li>
          </ul>
        </div>
      </div>
    </section>

    <!-- 产品系列 -->
    <section class="section series">
      <div class="container">
        <div class="series-head">
          <div>
            <span class="eyebrow">产品系列</span>
            <h2 class="section-title">覆盖全屋空间的一站式方案</h2>
          </div>
          <a href="products.html" class="btn btn-line">查看全部</a>
        </div>
        <div class="series-grid">
          <a
            v-for="c in categories"
            :key="c.name"
            href="products.html"
            class="series-card"
          >
            <div class="series-img" :style="bg(c.img, 'rgba(20,16,12,0.25)')">
              <span class="series-name">{{ c.name }}</span>
            </div>
            <p class="series-desc">{{ c.desc }}</p>
          </a>
        </div>
      </div>
    </section>

    <!-- 工厂实力 -->
    <section class="section factory">
      <div class="container factory-grid">
        <div class="factory-img" :style="bg(imgFactory, 'rgba(20,16,12,0.35)')"></div>
        <div class="factory-text">
          <span class="eyebrow">源头工厂</span>
          <h2 class="section-title">看得见的生产，才值得托付</h2>
          <p>
            3.6 万平方米标准化厂房，下料、机加工、打磨、涂装、组装、质检全流程自主完成，
            欢迎您到厂实地考察每一道工序。
          </p>
          <ul class="factory-points">
            <li><span>01</span>数字化开料中心，板材利用率更高</li>
            <li><span>02</span>无尘涂装车间，漆面均匀细腻</li>
            <li><span>03</span>整装出货前 32 道质检工序</li>
            <li><span>04</span>支持小批量与 OEM / ODM 合作</li>
          </ul>
          <a href="factory.html" class="btn btn-primary">了解工厂实力</a>
        </div>
      </div>
    </section>

    <!-- 定制服务 -->
    <section class="section custom">
      <div class="container custom-inner">
        <div class="custom-copy">
          <span class="eyebrow">全屋定制</span>
          <h2 class="section-title">尺寸、材质、颜色，皆可按需定制</h2>
          <p>
            无论是小户型的收纳难题，还是别墅大宅的整体配套，我们都能提供从测量、
            设计到生产安装的一站式定制服务。
          </p>
          <a href="custom.html" class="btn btn-ghost">了解定制流程</a>
        </div>
        <div class="custom-steps">
          <div class="step" v-for="(s, i) in steps" :key="i">
            <span class="step-no">{{ String(i + 1).padStart(2, '0') }}</span>
            <div><h4>{{ s.t }}</h4><p>{{ s.d }}</p></div>
          </div>
        </div>
      </div>
    </section>

    <!-- 为什么选择我们 -->
    <section class="section why">
      <div class="container">
        <div class="why-head">
          <span class="eyebrow">为什么选择兔南</span>
          <h2 class="section-title">工厂直营，省心更省钱</h2>
        </div>
        <div class="why-grid">
          <div v-for="(w, i) in whyItems" :key="i" class="why-item">
            <span class="why-no">{{ String(i + 1).padStart(2, '0') }}</span>
            <h3>{{ w.t }}</h3>
            <p>{{ w.d }}</p>
          </div>
        </div>
      </div>
    </section>
    <!-- 客户口碑 -->
    <section class="section voices">
      <div class="container">
        <span class="eyebrow">客户口碑</span>
        <h2 class="section-title">他们这样说</h2>
        <div class="voices-grid">
          <figure v-for="v in voices" :key="v.name" class="voice">
            <blockquote>{{ v.text }}</blockquote>
            <figcaption>{{ v.name }} · {{ v.role }}</figcaption>
          </figure>
        </div>
      </div>
    </section>

    <!-- 新闻动态 -->
    <section class="section news">
      <div class="container">
        <span class="eyebrow">新闻动态</span>
        <h2 class="section-title">工厂最新资讯</h2>
        <div class="news-grid">
          <article v-for="n in news" :key="n.t" class="news-card">
            <div class="news-date">{{ n.date }}</div>
            <h3>{{ n.t }}</h3>
            <p>{{ n.d }}</p>
            <a href="contact.html" class="news-more">了解更多 →</a>
          </article>
        </div>
      </div>
    </section>
    <!-- 合作品牌 -->
    <section class="brands">
      <div class="container brands-inner">
        <span>长期服务品牌</span>
        <div class="brands-list">
          <em v-for="b in brands" :key="b">{{ b }}</em>
        </div>
      </div>
    </section>

    <!-- CTA -->
    <section class="cta">
      <div class="cta-bg" :style="bg(imgBedroom, 'rgba(20,16,12,0.6)')"></div>
      <div class="container cta-inner">
        <h2>把您理想中的家，交给我们来实现</h2>
        <p>全国热线 400-888-1988，专业顾问一对一为您服务</p>
        <a href="contact.html" class="btn btn-primary">立即联系</a>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const bg = (url, overlay) => ({
  backgroundImage: `linear-gradient(${overlay}, ${overlay}), url('${url}')`,
  backgroundSize: 'cover',
  backgroundPosition: 'center',
})

const slides = [
  {
    img: 'https://images.unsplash.com/photo-1555041469-a586c61ea9bc?auto=format&fit=crop&w=1800&q=80',
    eyebrow: '源自工厂 · 直供万家',
    title: '好家居，从源头开始',
    sub: '自有厂房、自有产线，砍掉层层中间商，让每一件实木家具都经得起岁月与审美的双重推敲。',
    btnText: '浏览产品', btnLink: 'products.html',
    ghostText: '预约工厂参观', ghostLink: 'factory.html',
  },
  {
    img: 'https://images.unsplash.com/photo-1616594039964-ae9021a400a0?auto=format&fit=crop&w=1800&q=80',
    eyebrow: '全屋实木定制',
    title: '一件家具，一室温度',
    sub: '从测量、设计到生产安装，一对一定制，把家的每一寸都安排得刚刚好。',
    btnText: '了解定制', btnLink: 'custom.html',
    ghostText: '查看产品', ghostLink: 'products.html',
  },
  {
    img: 'https://images.unsplash.com/photo-1617806118233-18e1de247200?auto=format&fit=crop&w=1800&q=80',
    eyebrow: '十八年匠心制造',
    title: '把每一寸木纹做到极致',
    sub: '北美进口硬木、榫卯结构、水性环保漆，品质经得起时间与使用的检验。',
    btnText: '走进工厂', btnLink: 'factory.html',
    ghostText: '联系我们', ghostLink: 'contact.html',
  },
  {
    img: 'https://images.unsplash.com/photo-1600210492486-724fe5c67fb0?auto=format&fit=crop&w=1800&q=80',
    eyebrow: '源头工厂 · 直供万家',
    title: '高端轻奢，从源头开始',
    sub: '省去中间环节，让高品质家居回归实在价格，全国发货、上门安装。',
    btnText: '立即咨询', btnLink: 'contact.html',
    ghostText: '浏览产品', ghostLink: 'products.html',
  },
]

const current = ref(0)
let timer = null
const next = () => { current.value = (current.value + 1) % slides.length }
const prev = () => { current.value = (current.value - 1 + slides.length) % slides.length }
const go = (i) => { current.value = i }

onMounted(() => { timer = setInterval(next, 5000) })
onUnmounted(() => { clearInterval(timer) })
const imgWood = 'https://images.unsplash.com/photo-1519710164239-da123dc03ef4?auto=format&fit=crop&w=1000&q=80'
const imgSofa = 'https://images.unsplash.com/photo-1586023492125-27b2c045efd7?auto=format&fit=crop&w=1000&q=80'
const imgFactory = 'https://images.unsplash.com/photo-1504148455328-c376907d081c?auto=format&fit=crop&w=1200&q=80'
const imgBedroom = 'https://images.unsplash.com/photo-1616594039964-ae9021a400a0?auto=format&fit=crop&w=1800&q=80'

const categories = [
  { name: '客厅空间', desc: '沙发、茶几、电视柜，营造待客与团聚的质感', img: 'https://images.unsplash.com/photo-1555041469-a586c61ea9bc?auto=format&fit=crop&w=800&q=80' },
  { name: '卧室空间', desc: '床、衣柜、床头柜，舒适与收纳兼备', img: 'https://images.unsplash.com/photo-1616594039964-ae9021a400a0?auto=format&fit=crop&w=800&q=80' },
  { name: '餐厅空间', desc: '餐桌、餐椅、餐边柜，一日三餐的仪式感', img: 'https://images.unsplash.com/photo-1617806118233-18e1de247200?auto=format&fit=crop&w=800&q=80' },
  { name: '书房空间', desc: '书桌、书柜、收纳柜，安放思考与热爱', img: 'https://images.unsplash.com/photo-1497366754035-f200968a6e72?auto=format&fit=crop&w=800&q=80' },
]

const steps = [
  { t: '需求沟通', d: '了解空间尺寸与生活习惯' },
  { t: '上门测量', d: '专业量尺，复核现场细节' },
  { t: '方案设计', d: '3D 效果图，所见即所得' },
  { t: '生产交付', d: '工厂直产，安装售后无忧' },
]

const voices = [
  { name: '周女士', role: '广州 · 天河', text: '从沟通到安装都很省心，工厂直发确实比商场便宜了三成，做工细节经得起放大看。' },
  { name: '林先生', role: '深圳 · 南山', text: '全屋定制一次搞定，设计师很专业，连过道转角都利用起来了，家里空间感完全不一样。' },
  { name: '陈总', role: '东莞 · 经销商', text: '合作了五年，出货稳定、售后响应快，是我们店里口碑最好的供货工厂之一。' },
]

const whyItems = [
  { t: '源头直供', d: '工厂直营，省去中间加价，同等品质价格更实在。' },
  { t: '真材实料', d: '100% 全实木框架，北美进口硬木，含水率稳定。' },
  { t: '匠心工艺', d: '榫卯结构 + 32 道质检，细节经得起放大看。' },
  { t: '无忧售后', d: '五年质保、48 小时响应、全国上门服务。' },
]

const news = [
  { date: '2026-09-18', t: '兔南家居荣获“绿色家居示范工厂”称号', d: '凭借水性漆工艺与环保管理体系，兔南获评本年度绿色家居示范工厂。' },
  { date: '2026-08-06', t: '新品发布：云岭系列黑胡桃全屋定制正式上市', d: '以北美黑胡桃为主材，覆盖客厅、卧室、书房的一体化定制方案。' },
  { date: '2026-06-22', t: '工厂开放日：百位业主走进兔南制造基地', d: '零距离参观下料、涂装、质检全流程，见证一件实木家具的诞生。' },
]
const brands = ['左右家居', '慕思', '全友', '顾家工艺', '林氏木业', '芝华仕']
</script>

<style scoped>
.hero { position: relative; min-height: 100vh; display: flex; align-items: center; color: #fff; }
.hero-bg { position: absolute; inset: 0; background-size: cover; background-position: center; opacity: 0; transition: opacity 1.2s ease; }
.hero-bg.active { opacity: 1; }
.hero-inner { position: relative; padding-top: 120px; }
.hero-eyebrow { font-size: 13px; letter-spacing: 0.4em; color: #e6d8c2; }
.hero h1 { font-size: clamp(40px, 6vw, 72px); margin: 20px 0 22px; color: #fff; }
.hero-sub { max-width: 560px; font-size: 16px; color: rgba(255, 255, 255, 0.85); }
.hero-actions { margin-top: 36px; display: flex; gap: 16px; flex-wrap: wrap; }
.hero-arrow {
  position: absolute;
  top: 46%;
  transform: translateY(-50%);
  z-index: 5;
  width: 48px;
  height: 48px;
  border: 1px solid rgba(255, 255, 255, 0.5);
  background: rgba(0, 0, 0, 0.18);
  color: #fff;
  font-size: 28px;
  line-height: 1;
  cursor: pointer;
  transition: background 0.25s ease;
}
.hero-arrow:hover { background: rgba(0, 0, 0, 0.35); }
.hero-arrow.prev { left: 28px; }
.hero-arrow.next { right: 28px; }
.hero-dots {
  position: absolute;
  left: 50%;
  bottom: 126px;
  transform: translateX(-50%);
  z-index: 5;
  display: flex;
  gap: 10px;
}
.dot {
  width: 26px;
  height: 3px;
  background: rgba(255, 255, 255, 0.45);
  border: 0;
  cursor: pointer;
  transition: background 0.25s ease;
}
.dot.active { background: #fff; }
.fade-enter-active, .fade-leave-active { transition: opacity 0.5s ease; }
.fade-enter-from, .fade-leave-to { opacity: 0; }
@media (max-width: 900px) {
  .hero-arrow { width: 38px; height: 38px; font-size: 22px; }
  .hero-arrow.prev { left: 12px; }
  .hero-arrow.next { right: 12px; }
  .hero-dots { bottom: 190px; }
}
.hero-stats {
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
  bottom: 0;
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  width: min(1180px, 92vw);
  background: rgba(20, 16, 12, 0.5);
  backdrop-filter: blur(6px);
  border-top: 1px solid rgba(255, 255, 255, 0.15);
}
.stat { padding: 26px 20px; text-align: center; }
.stat strong { display: block; font-family: var(--serif); font-size: 30px; color: #e6d8c2; }
.stat span { font-size: 13px; color: rgba(255, 255, 255, 0.75); letter-spacing: 0.12em; }

.intro-grid { display: grid; grid-template-columns: 1.05fr 1fr; gap: 72px; align-items: center; }
.intro-media { position: relative; height: 520px; }
.intro-img { position: absolute;  background-size: cover; background-position: center; box-shadow: 0 24px 60px rgba(40, 32, 20, 0.18); }
.intro-img.main { inset: 0 80px 80px 0; }
.intro-img.sub { left: 180px; right: 0; bottom: 0; height: 280px; border: 8px solid var(--bg); }
.intro-text p { color: var(--muted); margin-bottom: 16px; }
.intro-list { list-style: none; margin-top: 22px; }
.intro-list li { padding: 10px 0 10px 26px; position: relative; color: var(--ink-soft); }
.intro-list li::before { content: ""; position: absolute; left: 0; top: 18px; width: 10px; height: 10px; border: 1px solid var(--gold);  }

.series { background: #fff; }
.series-head { display: flex; justify-content: space-between; align-items: flex-end; margin-bottom: 48px; }
.series-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 24px; }
.series-card { display: block; }
.series-img {
  height: 260px;
  
  background-size: cover;
  background-position: center;
  display: flex;
  align-items: flex-end;
  padding: 20px;
  transition: transform 0.4s ease;
}
.series-card:hover .series-img { transform: translateY(-6px); }
.series-name { color: #fff; font-family: var(--serif); font-size: 20px; letter-spacing: 0.08em; }
.series-desc { margin-top: 14px; color: var(--muted); font-size: 13px; }

.factory { background: var(--bg-soft); }
.factory-grid { display: grid; grid-template-columns: 1.05fr 1fr; gap: 64px; align-items: center; }
.factory-img { height: 520px;  background-size: cover; background-position: center; box-shadow: 0 24px 60px rgba(40, 32, 20, 0.18); }
.factory-text p { color: var(--muted); margin: 6px 0 22px; }
.factory-points { list-style: none; margin-bottom: 32px; }
.factory-points li { display: flex; align-items: center; gap: 16px; padding: 12px 0; border-bottom: 1px solid var(--line); color: var(--ink-soft); }
.factory-points span { font-family: var(--serif); color: var(--gold-deep); font-size: 15px; }

.custom { background: #211d18; color: #fff; }
.custom-inner { display: grid; grid-template-columns: 1fr 1fr; gap: 72px; align-items: center; }
.custom-copy h2 { color: #fff; }
.custom-copy p { color: #b7ab9a; margin: 8px 0 30px; }
.custom-steps { display: flex; flex-direction: column; gap: 26px; }
.step { display: flex; gap: 22px; align-items: flex-start; }
.step-no { font-family: var(--serif); font-size: 26px; color: var(--gold); }
.step h4 { font-family: var(--sans); font-size: 16px; letter-spacing: 0.1em; margin-bottom: 4px; }
.step p { color: #b7ab9a; font-size: 13px; }

.voices { background: #fff; }
.voices-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 28px; margin-top: 40px; }
.voice { border: 1px solid var(--line);  padding: 32px; }
.voice blockquote { color: var(--ink-soft); font-size: 15px; line-height: 1.9; }
.voice figcaption { margin-top: 20px; color: var(--gold-deep); font-size: 13px; }

.brands { border-top: 1px solid var(--line); background: #fff; }
.brands-inner { display: flex; align-items: center; gap: 40px; padding: 44px 0; }
.brands-inner span { color: var(--muted); font-size: 13px; white-space: nowrap; }
.brands-list { display: flex; gap: 44px; flex-wrap: wrap; }
.brands-list em { font-style: normal; font-family: var(--serif); font-size: 20px; color: #b8ad9d; letter-spacing: 0.12em; }

.cta { position: relative; color: #fff; }
.cta-bg { position: absolute; inset: 0; background-size: cover; background-position: center; }
.cta-inner { position: relative; text-align: center; padding: 110px 0; }
.cta-inner h2 { color: #fff; font-size: clamp(26px, 3.6vw, 40px); }
.cta-inner p { color: rgba(255, 255, 255, 0.8); margin: 16px 0 30px; }

.why { background: #fff; }
.why-head { margin-bottom: 44px; }
.why-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 24px; }
.why-item { border: 1px solid var(--line); padding: 30px 26px; background: #fff; }
.why-no { font-family: var(--serif); font-size: 26px; color: var(--gold); }
.why-item h3 { margin: 14px 0 8px; font-size: 18px; }
.why-item p { color: var(--muted); font-size: 13px; }

.news { background: var(--bg-soft); }
.news-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 28px; margin-top: 40px; }
.news-card { background: #fff; border: 1px solid var(--line); padding: 28px; }
.news-date { font-size: 12px; letter-spacing: 0.15em; color: var(--gold-deep); margin-bottom: 12px; }
.news-card h3 { font-size: 17px; margin-bottom: 10px; line-height: 1.5; }
.news-card p { color: var(--muted); font-size: 13px; }
.news-more { display: inline-block; margin-top: 16px; font-size: 13px; color: var(--gold-deep); }

@media (max-width: 900px) {
  .why-grid { grid-template-columns: 1fr 1fr; }
  .news-grid { grid-template-columns: 1fr; }
}
@media (max-width: 560px) {
  .why-grid { grid-template-columns: 1fr; }
}
@media (max-width: 900px) {
  .hero-stats { grid-template-columns: repeat(2, 1fr); }
  .intro-grid, .factory-grid, .custom-inner { grid-template-columns: 1fr; gap: 40px; }
  .intro-media, .factory-img { height: 380px; }
  .series-grid { grid-template-columns: repeat(2, 1fr); }
  .voices-grid { grid-template-columns: 1fr; }
  .brands-inner { flex-direction: column; align-items: flex-start; gap: 20px; }
}
@media (max-width: 560px) {
  .series-grid { grid-template-columns: 1fr; }
  .stat strong { font-size: 22px; }
}
</style>