<template>
  <div class="contact">
    <section class="page-hero">
      <div class="page-hero-bg" :style="bg(heroImg, 'rgba(20,16,12,0.55)')"></div>
      <div class="container page-hero-inner">
        <span class="eyebrow">CONTACT</span>
        <h1>联系我们</h1>
        <p>欢迎到厂参观 · 全国热线 400-888-1988</p>
      </div>
    </section>

    <section class="section main">
      <div class="container contact-grid">
        <div class="info">
          <span class="eyebrow">联系方式</span>
          <h2 class="section-title">期待与您见面</h2>

          <div class="info-item">
            <span class="label">全国服务热线</span>
            <a class="value big" href="tel:400-888-1988">400-888-1988</a>
          </div>
          <div class="info-item">
            <span class="label">业务咨询</span>
            <a class="value" href="tel:13800001988">138-0000-1988</a>
          </div>
          <div class="info-item">
            <span class="label">电子邮箱</span>
            <a class="value" href="mailto:service@tunan-home.cn">service@tunan-home.cn</a>
          </div>
          <div class="info-item">
            <span class="label">工厂地址</span>
            <span class="value">广东省佛山市顺德区乐从镇工业大道 88 号</span>
          </div>
          <div class="info-item">
            <span class="label">服务时间</span>
            <span class="value">周一至周六 8:30 - 18:00（展厅可预约参观）</span>
          </div>
        </div>

        <div class="form-wrap">
          <h3>在线咨询</h3>
          <p class="form-tip">填写以下信息，专属顾问将在 1 个工作日内与您联系。</p>
          <form v-if="!sent" class="form" @submit.prevent="submit">
            <label>
              <span>联系人</span>
              <input v-model="form.name" type="text" placeholder="怎么称呼您" required />
            </label>
            <label>
              <span>联系电话</span>
              <input v-model="form.phone" type="tel" placeholder="方便联系的手机号" required />
            </label>
            <label>
              <span>公司 / 品牌</span>
              <input v-model="form.company" type="text" placeholder="公司或个人品牌名称" />
            </label>
            <label>
              <span>项目类型</span>
              <select v-model="form.project">
                <option>成品采购</option>
                <option>全屋定制</option>
                <option>OEM / ODM 合作</option>
                <option>工程配套</option>
                <option>到厂参观</option>
              </select>
            </label>
            <label>
              <span>预计数量</span>
              <select v-model="form.qty">
                <option>10 件以内</option>
                <option>10 - 50 件</option>
                <option>50 - 200 件</option>
                <option>200 件以上</option>
              </select>
            </label>
            <label>
              <span>交付城市</span>
              <input v-model="form.city" type="text" placeholder="例如：广州 / 深圳" />
            </label>
            <label>
              <span>预算区间</span>
              <select v-model="form.budget">
                <option>1 万以内</option>
                <option>1 - 5 万</option>
                <option>5 - 20 万</option>
                <option>20 万以上</option>
                <option>面议</option>
              </select>
            </label>
            <label class="full">
              <span>需求说明</span>
              <textarea v-model="form.message" rows="4" placeholder="例如：需要一张 2 米长的黑胡桃餐桌，预算 5000 左右，期望 30 天内交付"></textarea>
            </label>
            <p v-if="errorMsg" class="form-error">{{ errorMsg }}</p>            <button type="submit" class="btn btn-primary" :disabled="submitting">{{ submitting ? '提交中…' : '提交需求' }}</button>
          </form>
          <div v-else class="sent">
            <div class="sent-icon">✓</div>
            <h4>提交成功</h4>
            <p>感谢您的留言，我们的顾问会尽快与您联系。</p>
          </div>
        </div>
      </div>
    </section>

    <section class="section transport">
      <div class="container">
        <span class="eyebrow">到厂交通</span>
        <h2 class="section-title">如何到达工厂</h2>
        <div class="transport-grid">
          <div v-for="t in transport" :key="t.mode" class="transport-item">
            <h4>{{ t.mode }}</h4>
            <p>{{ t.d }}</p>
          </div>
        </div>
      </div>
    </section>

    <section class="section business">
      <div class="container business-inner">
        <div class="business-copy">
          <span class="eyebrow">商务合作</span>
          <h2 class="section-title">诚邀经销商与品牌方合作</h2>
          <p>
            面向全国招募区域经销商，并提供 OEM / ODM 定制生产服务，
            支持小批量试单、来图打样与联合开发。
          </p>
          <ul class="business-list">
            <li>区域独家授权 · 阶梯供货价</li>
            <li>OEM / ODM 来图来样定制</li>
            <li>工程单、酒店会所批量配套</li>
            <li>新品样册与销售培训支持</li>
          </ul>
        </div>
        <div class="business-img" :style="bg(bizImg, 'rgba(20,16,12,0.2)')"></div>
      </div>
    </section>

    <section class="map">
      <div class="map-inner">
        <div class="map-bg" :style="bg(mapImg, 'rgba(20,16,12,0.25)')">
          <div class="map-pin">
            <span>兔南家居 · 源头工厂</span>
            <em>佛山市顺德区乐从镇工业大道 88 号</em>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { reactive, ref } from 'vue'
import axios from 'axios'

const bg = (url, overlay) => ({
  backgroundImage: `linear-gradient(${overlay}, ${overlay}), url('${url}')`,
  backgroundSize: 'cover',
  backgroundPosition: 'center',
})

const heroImg = 'https://images.unsplash.com/photo-1616486338812-3dadae4b4ace?auto=format&fit=crop&w=1800&q=80'
const mapImg = 'https://images.unsplash.com/photo-1524661135-423995f22d0b?auto=format&fit=crop&w=1800&q=80'
const bizImg = 'https://images.unsplash.com/photo-1497366754035-f200968a6e72?auto=format&fit=crop&w=1000&q=80'

const form = reactive({
  name: '',
  phone: '',
  company: '',
  project: '成品采购',
  qty: '10 件以内',
  city: '',
  budget: '1 万以内',
  message: '',
})
const sent = ref(false)
const submitting = ref(false)
const errorMsg = ref('')

const submit = async () => {
  submitting.value = true
  errorMsg.value = ''
  try {
    await axios.post((import.meta.env.VITE_API_BASE || '') + '/api/contract/', {
      contact: form.name,
      phone: form.phone,
      company: form.company,
      project_type: form.project,
      quantity: form.qty,
      city: form.city,
      budget: form.budget,
      message: form.message,
    })
    sent.value = true
  } catch (e) {
    errorMsg.value = '提交失败，请稍后重试，或直接拨打 400-888-1988。'
  } finally {
    submitting.value = false
  }
}

const transport = [
  { mode: '地铁', d: '广佛线「乐从站」D 出口，步行约 10 分钟到达厂区。' },
  { mode: '自驾', d: '导航搜索“兔南家居制造基地”，厂区提供免费停车位。' },
  { mode: '高铁 / 机场', d: '广州南站、佛山沙堤机场车程约 30 分钟，可预约接站。' },
]
</script>

<style scoped>
.page-hero { position: relative; color: #fff; padding: 190px 0 110px; }
.page-hero-bg { position: absolute; inset: 0; background-size: cover; background-position: center; }
.page-hero-inner { position: relative; }
.page-hero h1 { font-size: clamp(36px, 5vw, 58px); margin: 16px 0 12px; color: #fff; }
.page-hero p { color: rgba(255, 255, 255, 0.8); letter-spacing: 0.2em; }

.contact-grid { display: grid; grid-template-columns: 1fr 1.15fr; gap: 72px; align-items: start; }
.info-item { padding: 22px 0; border-bottom: 1px solid var(--line); }
.label { display: block; font-size: 12px; letter-spacing: 0.2em; color: var(--muted); margin-bottom: 8px; }
.value { color: var(--ink-soft); font-size: 15px; }
.value.big { font-family: var(--serif); font-size: 28px; color: var(--gold-deep); }

.form-wrap { background: #fff; border: 1px solid var(--line); padding: 38px; }
.form-wrap h3 { font-size: 22px; margin-bottom: 6px; }
.form-tip { color: var(--muted); font-size: 13px; margin-bottom: 24px; }
.form { display: grid; grid-template-columns: 1fr 1fr; gap: 18px; }
.form label { display: flex; flex-direction: column; gap: 8px; }
.form label.full { grid-column: 1 / -1; }
.form label span { font-size: 13px; color: var(--ink-soft); }
.form input, .form select, .form textarea {
  border: 1px solid var(--line);
  background: var(--bg);
  padding: 12px 14px;
  font: inherit;
  color: var(--ink);
  outline: none;
}
.form input:focus, .form select:focus, .form textarea:focus { border-color: var(--gold); }
.form button { grid-column: 1 / -1; justify-self: start; }
.form-error { grid-column: 1 / -1; color: #dc2626; font-size: 13px; margin: 0; }
.btn:disabled { opacity: 0.6; cursor: not-allowed; }
.sent { text-align: center; padding: 40px 0; }
.sent-icon {
  width: 58px; height: 58px; margin: 0 auto 20px;
  background: var(--gold);
  color: #fff;
  display: flex; align-items: center; justify-content: center;
  font-size: 26px;
}
.sent h4 { font-size: 20px; margin-bottom: 8px; }
.sent p { color: var(--muted); font-size: 14px; }

.transport { background: var(--bg-soft); }
.transport-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 28px; margin-top: 40px; }
.transport-item { background: #fff; border: 1px solid var(--line); padding: 30px; }
.transport-item h4 { color: var(--gold-deep); margin-bottom: 10px; }
.transport-item p { color: var(--muted); font-size: 14px; }

.business { background: #fff; }
.business-inner { display: grid; grid-template-columns: 1.1fr 1fr; gap: 64px; align-items: center; }
.business-copy p { color: var(--muted); margin: 8px 0 20px; }
.business-list { list-style: none; }
.business-list li { padding: 10px 0 10px 26px; position: relative; color: var(--ink-soft); }
.business-list li::before { content: ""; position: absolute; left: 0; top: 18px; width: 10px; height: 10px; border: 1px solid var(--gold); }
.business-img { height: 420px; background-size: cover; background-position: center; }

.map { padding-bottom: 96px; }
.map-inner { width: min(1180px, 92vw); margin: 0 auto; }
.map-bg { position: relative; height: 380px; background-size: cover; background-position: center; }
.map-pin {
  position: absolute; left: 50%; top: 50%; transform: translate(-50%, -50%);
  background: #fff; color: var(--ink);
  padding: 18px 26px; text-align: center;
  box-shadow: 0 14px 40px rgba(0, 0, 0, 0.2);
}
.map-pin span { font-family: var(--serif); font-size: 17px; display: block; }
.map-pin em { font-style: normal; font-size: 12px; color: var(--muted); }

@media (max-width: 900px) {
  .contact-grid, .business-inner { grid-template-columns: 1fr; }
  .transport-grid { grid-template-columns: 1fr; }
  .business-img { height: 300px; }
}
@media (max-width: 560px) {
  .form { grid-template-columns: 1fr; }
}
</style>