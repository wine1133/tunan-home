<template>
  <div class="products">
    <section class="page-hero">
      <div class="page-hero-bg" :style="bg(heroImg, 'rgba(20,16,12,0.55)')"></div>
      <div class="container page-hero-inner">
        <span class="eyebrow">PRODUCTS</span>
        <h1>产品中心</h1>
        <p>全实木 · 全屋空间 · 工厂直供</p>
      </div>
    </section>

    <section class="section list">
      <div class="container">
        <div class="filters">
          <button
            v-for="t in tabs"
            :key="t"
            class="filter"
            :class="{ active: active === t }"
            @click="active = t"
          >
            {{ t }}
          </button>
        </div>

        <div class="product-grid">
          <article v-for="p in filtered" :key="p.name" class="product">
            <div class="product-img" :style="bg(p.img, 'rgba(20,16,12,0.18)')">
              <span class="tag">{{ p.cat }}</span>
            </div>
            <div class="product-info">
              <h3>{{ p.name }}</h3>
              <p class="mat">{{ p.material }}</p>
              <p class="desc">{{ p.desc }}</p>
              <div class="price-row">
                <span class="price">{{ p.price }}</span>
                <a href="contact.html" class="more">咨询底价 →</a>
              </div>
            </div>
          </article>
        </div>
      </div>
    </section>

    <!-- 空间搭配方案 -->
    <section class="section roomsets">
      <div class="container">
        <span class="eyebrow">空间搭配</span>
        <h2 class="section-title">成套购买，风格更统一</h2>
        <div class="roomset-grid">
          <div v-for="r in roomSets" :key="r.name" class="roomset">
            <div class="roomset-img" :style="bg(r.img, 'rgba(20,16,12,0.2)')"></div>
            <div class="roomset-info">
              <h3>{{ r.name }}</h3>
              <p class="items">{{ r.items }}</p>
              <div class="roomset-bottom">
                <span class="rprice">{{ r.price }}</span>
                <a href="contact.html" class="more">咨询 →</a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
    <section class="section materials">
      <div class="container">
        <span class="eyebrow">材质与工艺</span>
        <h2 class="section-title">精选北美硬木，越用越有味道</h2>
        <div class="material-grid">
          <div v-for="m in materials" :key="m.name" class="material">
            <div class="material-img" :style="bg(m.img, 'rgba(20,16,12,0.15)')"></div>
            <h4>{{ m.name }}</h4>
            <p>{{ m.desc }}</p>
          </div>
        </div>
      </div>
    </section>

    <!-- 客户评价 -->
    <section class="section reviews">
      <div class="container">
        <span class="eyebrow">客户评价</span>
        <h2 class="section-title">真实买家反馈</h2>
        <div class="reviews-grid">
          <figure v-for="v in reviews" :key="v.name" class="review">
            <div class="stars">★★★★★</div>
            <blockquote>{{ v.text }}</blockquote>
            <figcaption>{{ v.name }} · {{ v.product }}</figcaption>
          </figure>
        </div>
      </div>
    </section>

    <!-- 售后保障 -->
    <section class="section aftersale">
      <div class="container">
        <span class="eyebrow">售后保障</span>
        <h2 class="section-title">买得放心，用得安心</h2>
        <div class="aftersale-grid">
          <div v-for="a in afterSale" :key="a.t" class="as-item">
            <h4>{{ a.t }}</h4>
            <p>{{ a.d }}</p>
          </div>
        </div>
      </div>
    </section>
    <section class="cta">
      <div class="cta-bg" :style="bg(ctaImg, 'rgba(20,16,12,0.6)')"></div>
      <div class="container cta-inner">
        <h2>没有看到心仪的款式？</h2>
        <p>我们支持来图定制，一个想法也能变成实木成品</p>
        <a href="custom.html" class="btn btn-primary">了解定制服务</a>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

const bg = (url, overlay) => ({
  backgroundImage: `linear-gradient(${overlay}, ${overlay}), url('${url}')`,
  backgroundSize: 'cover',
  backgroundPosition: 'center',
})

const heroImg = 'https://images.unsplash.com/photo-1616486338812-3dadae4b4ace?auto=format&fit=crop&w=1800&q=80'
const ctaImg = 'https://images.unsplash.com/photo-1586023492125-27b2c045efd7?auto=format&fit=crop&w=1800&q=80'

const active = ref('全部')
const tabs = ['全部', '客厅', '卧室', '餐厅', '书房']

const products = [
  { name: '云岭 · 三人位实木沙发', cat: '客厅', material: '北美黑胡桃 · 亚麻布艺', price: '¥ 6,980 起', desc: '低重心宽坐深设计，榫卯框架，久坐不塌。', img: 'https://images.unsplash.com/photo-1555041469-a586c61ea9bc?auto=format&fit=crop&w=900&q=80' },
  { name: '拾光 · 实木茶几', cat: '客厅', material: '北美白橡木 · 岩板台面', price: '¥ 1,980 起', desc: '圆角打磨，嵌入式岩板，防烫耐磨。', img: 'https://images.unsplash.com/photo-1533090161767-e6ffed986c88?auto=format&fit=crop&w=900&q=80' },
  { name: '栖迟 · 实木大床', cat: '卧室', material: '北美黑胡桃 · 实木排骨架', price: '¥ 5,580 起', desc: '1.8 米加宽床头，静音床架，十年质保。', img: 'https://images.unsplash.com/photo-1616594039964-ae9021a400a0?auto=format&fit=crop&w=900&q=80' },
  { name: '流年 · 床头柜', cat: '卧室', material: '白蜡木 · 黄铜拉手', price: '¥ 880 起', desc: '双层抽屉，静音滑轨，收纳有序。', img: 'https://images.unsplash.com/photo-1505693416388-ac5ce068fe85?auto=format&fit=crop&w=900&q=80' },
  { name: '共飨 · 实木餐桌', cat: '餐厅', material: '北美红橡 · 全实木桌面', price: '¥ 3,280 起', desc: '4-6 人位可选，加宽桌腿更稳固。', img: 'https://images.unsplash.com/photo-1617806118233-18e1de247200?auto=format&fit=crop&w=900&q=80' },
  { name: '雅集 · 餐椅', cat: '餐厅', material: '白蜡木 · 头层牛皮坐垫', price: '¥ 780 起', desc: '人体工学靠背弧度，久坐不累。', img: 'https://images.unsplash.com/photo-1595515106969-1ce29566ff1c?auto=format&fit=crop&w=900&q=80' },
  { name: '墨语 · 实木书桌', cat: '书房', material: '北美黑胡桃 · 隐藏走线槽', price: '¥ 2,680 起', desc: '大板面 + 线槽设计，办公学习两相宜。', img: 'https://images.unsplash.com/photo-1497366754035-f200968a6e72?auto=format&fit=crop&w=900&q=80' },
  { name: '藏卷 · 玻璃门书柜', cat: '书房', material: '白橡木 · 钢化玻璃', price: '¥ 4,980 起', desc: '层板可调，防尘玻璃门，陈列收纳兼具。', img: 'https://images.unsplash.com/photo-1594620302200-9a762244a156?auto=format&fit=crop&w=900&q=80' },
]

const filtered = computed(() =>
  active.value === '全部' ? products : products.filter((p) => p.cat === active.value)
)

const roomSets = [
  { name: '客厅整配方案', price: '¥ 12,800 起', items: '沙发 + 茶几 + 电视柜 + 边几', img: 'https://images.unsplash.com/photo-1555041469-a586c61ea9bc?auto=format&fit=crop&w=800&q=80' },
  { name: '卧室整配方案', price: '¥ 9,680 起', items: '大床 + 床头柜 ×2 + 衣柜', img: 'https://images.unsplash.com/photo-1616594039964-ae9021a400a0?auto=format&fit=crop&w=800&q=80' },
  { name: '餐厅整配方案', price: '¥ 5,280 起', items: '餐桌 + 餐椅 ×4 + 餐边柜', img: 'https://images.unsplash.com/photo-1617806118233-18e1de247200?auto=format&fit=crop&w=800&q=80' },
]

const reviews = [
  { name: '杭州 · 王女士', product: '云岭黑胡桃沙发', text: '实物比图片更有质感，坐感扎实，师傅安装也很仔细。' },
  { name: '成都 · 李先生', product: '栖迟实木大床', text: '床架很稳，没有异响，排骨架做工特别实在，值得推荐。' },
  { name: '长沙 · 赵先生', product: '共飨实木餐桌', text: '桌面纹理漂亮，客服耐心，工厂直发还省了不少钱。' },
]

const afterSale = [
  { t: '五年质保', d: '结构类问题五年内免费维修或更换。' },
  { t: '48 小时响应', d: '售后问题 48 小时内响应并给出处理方案。' },
  { t: '全国配送安装', d: '专业物流与安装师傅，送货上门并现场安装。' },
  { t: '终身维护咨询', d: '终身提供保养知识与配件选购建议。' },
]
const materials = [
  { name: '北美黑胡桃', desc: '色泽沉稳、纹理细腻，随时间愈发温润，是高端家具的经典之选。', img: 'https://images.unsplash.com/photo-1519710164239-da123dc03ef4?auto=format&fit=crop&w=600&q=80' },
  { name: '北美白橡木', desc: '山形纹理清晰，硬度高、耐磨损，适合日式与北欧风格。', img: 'https://images.unsplash.com/photo-1504148455328-c376907d081c?auto=format&fit=crop&w=600&q=80' },
  { name: '白蜡木', desc: '纹理通直、韧性出色，浅色系首选，百搭明亮空间。', img: 'https://images.unsplash.com/photo-1586023492125-27b2c045efd7?auto=format&fit=crop&w=600&q=80' },
]
</script>

<style scoped>
.page-hero { position: relative; color: #fff; padding: 190px 0 110px; }
.page-hero-bg { position: absolute; inset: 0; background-size: cover; background-position: center; }
.page-hero-inner { position: relative; }
.page-hero h1 { font-size: clamp(36px, 5vw, 58px); margin: 16px 0 12px; color: #fff; }
.page-hero p { color: rgba(255, 255, 255, 0.8); letter-spacing: 0.2em; }

.filters { display: flex; gap: 14px; flex-wrap: wrap; margin-bottom: 48px; }
.filter {
  padding: 10px 26px;
  border: 1px solid var(--line);
  background: #fff;
  color: var(--ink-soft);
  cursor: pointer;
  letter-spacing: 0.1em;
  transition: all 0.25s ease;
}
.filter.active { background: var(--gold); border-color: var(--gold); color: #fff; }

.product-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 30px; }
.product { background: #fff;  overflow: hidden; border: 1px solid var(--line); transition: box-shadow 0.3s ease, transform 0.3s ease; }
.product:hover { box-shadow: 0 18px 44px rgba(40, 32, 20, 0.12); transform: translateY(-4px); }
.product-img { height: 240px; background-size: cover; background-position: center; position: relative; }
.tag {
  position: absolute;
  left: 14px;
  top: 14px;
  background: rgba(20, 16, 12, 0.6);
  color: #fff;
  font-size: 12px;
  padding: 4px 12px;
  letter-spacing: 0.12em;
}
.product-info { padding: 22px; }
.product-info h3 { font-size: 19px; margin-bottom: 6px; }
.mat { color: var(--gold-deep); font-size: 13px; }
.desc { color: var(--muted); font-size: 13px; margin: 10px 0 16px; }
.price-row { display: flex; justify-content: space-between; align-items: center; }
.price { font-family: var(--serif); font-size: 18px; color: var(--ink); }
.more { font-size: 13px; color: var(--gold-deep); }

.materials { background: var(--bg-soft); }
.material-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 30px; margin-top: 44px; }
.material { background: #fff; padding: 22px;  }
.material-img { height: 190px; background-size: cover; background-position: center;  }
.material h4 { margin: 18px 0 8px; }
.material p { color: var(--muted); font-size: 13px; }

.cta { position: relative; color: #fff; }
.cta-bg { position: absolute; inset: 0; background-size: cover; background-position: center; }
.cta-inner { position: relative; text-align: center; padding: 100px 0; }
.cta-inner h2 { color: #fff; font-size: clamp(24px, 3.4vw, 38px); }
.cta-inner p { color: rgba(255, 255, 255, 0.8); margin: 14px 0 28px; }

.roomsets { background: #fff; }
.roomset-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 28px; margin-top: 44px; }
.roomset { border: 1px solid var(--line); background: #fff; }
.roomset-img { height: 220px; background-size: cover; background-position: center; }
.roomset-info { padding: 22px; }
.roomset-info h3 { font-size: 18px; margin-bottom: 6px; }
.items { color: var(--muted); font-size: 13px; margin-bottom: 14px; }
.roomset-bottom { display: flex; justify-content: space-between; align-items: center; }
.rprice { font-family: var(--serif); font-size: 18px; color: var(--ink); }

.reviews { background: var(--bg-soft); }
.reviews-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 28px; margin-top: 40px; }
.review { border: 1px solid var(--line); background: #fff; padding: 30px; }
.stars { color: var(--gold-deep); letter-spacing: 0.2em; }
.review blockquote { color: var(--ink-soft); font-size: 14px; line-height: 1.9; margin-top: 14px; }
.review figcaption { margin-top: 16px; color: var(--gold-deep); font-size: 13px; }

.aftersale { background: #fff; }
.aftersale-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 24px; margin-top: 40px; }
.as-item { border: 1px solid var(--line); padding: 26px; }
.as-item h4 { color: var(--gold-deep); margin-bottom: 8px; }
.as-item p { color: var(--muted); font-size: 13px; }

@media (max-width: 900px) {
  .roomset-grid, .reviews-grid { grid-template-columns: 1fr; }
  .aftersale-grid { grid-template-columns: 1fr 1fr; }
}
@media (max-width: 560px) {
  .aftersale-grid { grid-template-columns: 1fr; }
}
@media (max-width: 900px) {
  .product-grid { grid-template-columns: repeat(2, 1fr); }
  .material-grid { grid-template-columns: 1fr; }
}
@media (max-width: 560px) {
  .product-grid { grid-template-columns: 1fr; }
}
</style>