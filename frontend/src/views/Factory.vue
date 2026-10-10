<template>
  <div class="factory">
    <section class="page-hero">
      <div class="page-hero-bg" :style="bg(heroImg, 'rgba(20,16,12,0.55)')"></div>
      <div class="container page-hero-inner">
        <span class="eyebrow">FACTORY</span>
        <h1>源头工厂</h1>
        <p>3.6 万㎡ 现代化制造基地 · 全流程自主生产</p>
      </div>
    </section>

    <section class="section overview">
      <div class="container overview-grid">
        <div class="overview-text">
          <span class="eyebrow">工厂概况</span>
          <h2 class="section-title">十八年，只做好一件实木家具</h2>
          <p>
            兔南家居制造基地位于“中国家具商贸之都”广东顺德，占地 3.6 万平方米，
            集研发设计、木工加工、涂装、软包、仓储物流于一体，年产能可满足
            数十万件实木家具的交付。
          </p>
          <p>
            工厂引入意大利数控开料机、德国全自动砂光与水性漆喷涂线，
            在保证精度的同时，将环保标准置于产能之前。
          </p>
        </div>
        <div class="overview-nums">
          <div class="num"><strong>36,000</strong><span>㎡ 厂房面积</span></div>
          <div class="num"><strong>260+</strong><span>名产业工人</span></div>
          <div class="num"><strong>120+</strong><span>台自动化设备</span></div>
          <div class="num"><strong>32</strong><span>道出厂质检</span></div>
        </div>
      </div>
    </section>

    <section class="section process">
      <div class="container">
        <span class="eyebrow">生产流程</span>
        <h2 class="section-title">六道工序，环环可追溯</h2>
        <div class="process-list">
          <div v-for="(s, i) in process" :key="i" class="process-item">
            <div class="process-img" :style="bg(s.img, 'rgba(20,16,12,0.25)')"></div>
            <div class="process-txt">
              <span class="no">{{ String(i + 1).padStart(2, '0') }}</span>
              <h3>{{ s.t }}</h3>
              <p>{{ s.d }}</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 车间实景 -->
    <section class="section workshop">
      <div class="container">
        <span class="eyebrow">车间实景</span>
        <h2 class="section-title">一镜到底，走进生产现场</h2>
        <div class="workshop-grid">
          <div v-for="(g, i) in gallery" :key="i" class="ws-img" :style="bg(g, 'rgba(20,16,12,0.15)')"></div>
        </div>
      </div>
    </section>
    <section class="section equipment">
      <div class="container equipment-grid">
        <div class="equipment-item" v-for="e in equipment" :key="e.t">
          <div class="equipment-img" :style="bg(e.img, 'rgba(20,16,12,0.2)')"></div>
          <h3>{{ e.t }}</h3>
          <p>{{ e.d }}</p>
        </div>
      </div>
    </section>

    <!-- 资质荣誉 -->
    <section class="section honors">
      <div class="container honors-inner">
        <div class="honors-copy">
          <span class="eyebrow">资质荣誉</span>
          <h2 class="section-title">权威认证，实力背书</h2>
          <p>多年沉淀与标准化管理，让每一件出厂家具都有迹可循、有据可依。</p>
        </div>
        <div class="honors-list">
          <div v-for="h in honors" :key="h.t" class="honor">
            <span class="honor-icon">✓</span>
            <div><h4>{{ h.t }}</h4><p>{{ h.d }}</p></div>
          </div>
        </div>
      </div>
    </section>

    <!-- 参观指南 -->
    <section class="section visit">
      <div class="container">
        <span class="eyebrow">参观指南</span>
        <h2 class="section-title">欢迎您到厂实地考察</h2>
        <div class="visit-grid">
          <div v-for="(v, i) in visitSteps" :key="i" class="visit-step">
            <span class="vno">{{ String(i + 1).padStart(2, '0') }}</span>
            <h3>{{ v.t }}</h3>
            <p>{{ v.d }}</p>
          </div>
        </div>
      </div>
    </section>
    <section class="section standard">
      <div class="container standard-inner">
        <span class="eyebrow">品质标准</span>
        <h2 class="section-title">每一件出厂，都有据可查</h2>
        <div class="standard-grid">
          <div v-for="s in standards" :key="s.t" class="standard-item">
            <h4>{{ s.t }}</h4>
            <p>{{ s.d }}</p>
          </div>
        </div>
        <a href="/contact/" class="btn btn-primary">预约到厂参观</a>
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

const heroImg = 'https://images.unsplash.com/photo-1565610222536-ef125c59da2e?auto=format&fit=crop&w=1800&q=80'

const process = [
  { t: '选材烘干', d: '北美进口原木，自然养生与蒸汽烘干，含水率稳定在 8% - 12%。', img: 'https://images.unsplash.com/photo-1519710164239-da123dc03ef4?auto=format&fit=crop&w=800&q=80' },
  { t: '开料裁切', d: '数控开料，依据纹理走向排料，减少结疤与色差。', img: 'https://images.unsplash.com/photo-1504148455328-c376907d081c?auto=format&fit=crop&w=800&q=80' },
  { t: '木工加工', d: '榫卯结构 + 精细打磨，圆角与线条一气呵成。', img: 'https://images.unsplash.com/photo-1565610222536-ef125c59da2e?auto=format&fit=crop&w=800&q=80' },
  { t: '水性涂装', d: '德国水性漆，无尘车间喷涂，漆面通透环保。', img: 'https://images.unsplash.com/photo-1565610222536-ef125c59da2e?auto=format&fit=crop&w=800&q=80' },
  { t: '软包组装', d: '高回弹海绵 + 品牌五金，整装与拆装两条产线并行。', img: 'https://images.unsplash.com/photo-1555041469-a586c61ea9bc?auto=format&fit=crop&w=800&q=80' },
  { t: '质检入库', d: '结构、漆面、五金、环保 32 道质检，合格方可出厂。', img: 'https://images.unsplash.com/photo-1586023492125-27b2c045efd7?auto=format&fit=crop&w=800&q=80' },
]

const equipment = [
  { t: '数控开料中心', d: '意大利进口设备，误差控制在 ±0.1mm', img: 'https://images.unsplash.com/photo-1504148455328-c376907d081c?auto=format&fit=crop&w=600&q=80' },
  { t: '自动砂光线', d: '多道砂光，表面细腻无毛刺', img: 'https://images.unsplash.com/photo-1519710164239-da123dc03ef4?auto=format&fit=crop&w=600&q=80' },
  { t: '无尘涂装车间', d: '恒温恒湿，水性漆环保喷涂', img: 'https://images.unsplash.com/photo-1565610222536-ef125c59da2e?auto=format&fit=crop&w=600&q=80' },
]

const gallery = [
  'https://images.unsplash.com/photo-1555041469-a586c61ea9bc?auto=format&fit=crop&w=700&q=80',
  'https://images.unsplash.com/photo-1519710164239-da123dc03ef4?auto=format&fit=crop&w=700&q=80',
  'https://images.unsplash.com/photo-1504148455328-c376907d081c?auto=format&fit=crop&w=700&q=80',
  'https://images.unsplash.com/photo-1565610222536-ef125c59da2e?auto=format&fit=crop&w=700&q=80',
  'https://images.unsplash.com/photo-1616594039964-ae9021a400a0?auto=format&fit=crop&w=700&q=80',
  'https://images.unsplash.com/photo-1586023492125-27b2c045efd7?auto=format&fit=crop&w=700&q=80',
]

const honors = [
  { t: 'ISO9001 质量管理体系认证', d: '生产、质检、交付全流程标准化管理。' },
  { t: '中国环境标志产品认证', d: '低醛水性漆工艺，环保指标达标。' },
  { t: '广东省守合同重信用企业', d: '多年诚信经营，履约零投诉。' },
  { t: '家具行业十大制造品牌', d: '行业协会推荐，经销商口碑之选。' },
]

const visitSteps = [
  { t: '电话预约', d: '拨打 400-888-1988，约定到厂时间。' },
  { t: '到厂接待', d: '专人引导，参观下料、涂装、质检车间。' },
  { t: '展厅体验', d: '2000㎡ 展厅，亲手感受材质与工艺。' },
]
const standards = [
  { t: '结构耐用', d: '榫卯结合与五金加固双重工艺，承重测试高于行业标准。' },
  { t: '环保健康', d: '水性漆与低醛板材，甲醛释放量优于国标 E0 级。' },
  { t: '防潮抗变形', d: '木材充分烘干养生，适应南方潮湿与北方干燥环境。' },
  { t: '细节零容忍', d: '边角打磨、五金顺滑度、漆面均匀度逐件人工复检。' },
]
</script>

<style scoped>
.page-hero { position: relative; color: #fff; padding: 190px 0 110px; }
.page-hero-bg { position: absolute; inset: 0; background-size: cover; background-position: center; }
.page-hero-inner { position: relative; }
.page-hero h1 { font-size: clamp(36px, 5vw, 58px); margin: 16px 0 12px; color: #fff; }
.page-hero p { color: rgba(255, 255, 255, 0.8); letter-spacing: 0.2em; }

.overview-grid { display: grid; grid-template-columns: 1.1fr 1fr; gap: 64px; align-items: center; }
.overview-text p { color: var(--muted); margin-bottom: 16px; }
.overview-nums { display: grid; grid-template-columns: 1fr 1fr; gap: 1px; background: var(--line); border: 1px solid var(--line); }
.num { background: var(--bg); padding: 34px 24px; text-align: center; }
.num strong { display: block; font-family: var(--serif); font-size: 30px; color: var(--gold-deep); }
.num span { font-size: 13px; color: var(--muted); letter-spacing: 0.1em; }

.process { background: #fff; }
.process-list { display: grid; grid-template-columns: repeat(3, 1fr); gap: 28px; margin-top: 44px; }
.process-item { background: var(--bg);  overflow: hidden; }
.process-img { height: 180px; background-size: cover; background-position: center; }
.process-txt { padding: 22px; }
.no { font-family: var(--serif); color: var(--gold-deep); font-size: 15px; }
.process-txt h3 { margin: 8px 0; font-size: 18px; }
.process-txt p { color: var(--muted); font-size: 13px; }

.equipment { background: var(--bg-soft); }
.equipment-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 30px; }
.equipment-item { background: #fff;  overflow: hidden; }
.equipment-img { height: 220px; background-size: cover; background-position: center; }
.equipment-item h3 { margin: 18px 22px 6px; }
.equipment-item p { margin: 0 22px 22px; color: var(--muted); font-size: 13px; }

.standard { background: #211d18; color: #fff; }
.standard-inner { text-align: center; }
.standard-inner h2 { color: #fff; }
.standard-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 24px; margin: 44px 0; text-align: left; }
.standard-item { border: 1px solid rgba(255, 255, 255, 0.12); padding: 28px;  }
.standard-item h4 { color: var(--gold); margin-bottom: 10px; }
.standard-item p { color: #b7ab9a; font-size: 13px; }

.workshop { background: #fff; }
.workshop-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 18px; margin-top: 40px; }
.ws-img { height: 240px; background-size: cover; background-position: center; }

.honors { background: var(--bg-soft); }
.honors-inner { display: grid; grid-template-columns: 1fr 1.2fr; gap: 64px; align-items: center; }
.honors-copy p { color: var(--muted); margin-top: 8px; }
.honors-list { display: grid; grid-template-columns: 1fr 1fr; gap: 18px; }
.honor { display: flex; gap: 14px; background: #fff; border: 1px solid var(--line); padding: 20px; }
.honor-icon { color: var(--gold-deep); font-weight: 700; }
.honor h4 { font-size: 15px; margin-bottom: 4px; }
.honor p { color: var(--muted); font-size: 12px; }

.visit { background: #fff; }
.visit-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 28px; margin-top: 40px; }
.visit-step { border: 1px solid var(--line); padding: 30px; background: var(--bg); }
.vno { font-family: var(--serif); font-size: 26px; color: var(--gold); }
.visit-step h3 { margin: 12px 0 8px; font-size: 17px; }
.visit-step p { color: var(--muted); font-size: 13px; }

@media (max-width: 900px) {
  .workshop-grid { grid-template-columns: 1fr 1fr; }
  .honors-inner { grid-template-columns: 1fr; }
  .visit-grid { grid-template-columns: 1fr; }
}
@media (max-width: 560px) {
  .workshop-grid, .honors-list { grid-template-columns: 1fr; }
}
@media (max-width: 900px) {
  .overview-grid { grid-template-columns: 1fr; }
  .process-list, .equipment-grid { grid-template-columns: 1fr 1fr; }
  .standard-grid { grid-template-columns: 1fr 1fr; }
}
@media (max-width: 560px) {
  .process-list, .equipment-grid, .standard-grid { grid-template-columns: 1fr; }
}
</style>