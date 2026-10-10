<template>
  <footer class="footer">
    <div class="container footer-grid">
      <div class="f-brand">
        <div class="f-logo-wrap">
          <svg class="f-mark" viewBox="0 0 64 64" aria-hidden="true">
            <rect width="64" height="64" fill="#b28a5a"/>
            <rect x="6" y="6" width="52" height="52" fill="none" stroke="#ffffff" stroke-opacity="0.38" stroke-width="1.5"/>
            <text x="32" y="47" text-anchor="middle" font-family="Noto Serif SC, Songti SC, STSong, SimSun, serif" font-size="38" fill="#ffffff">兔</text>
          </svg>
          <div class="f-logo">兔南家居</div>
        </div>
        <p class="f-en">TUNAN HOME · 源头工厂</p>
        <p class="f-desc">
          自有厂房、自有产线，从选材到交付全链路直营，让高品质家居回归实在的价格。
        </p>
      </div>

      <div class="f-col">
        <h4>快速导航</h4>
        <a href="/">首页</a>
        <a href="/products/">产品</a>
        <a href="/factory/">工厂</a>
        <a href="/custom/">定制</a>
        <a href="/contact/">联系</a>
      </div>

      <div class="f-col">
        <h4>联系方式</h4>
        <p>全国热线：400-888-1988</p>
        <p>业务咨询：138-0000-1988</p>
        <p>邮箱：service@tunan-home.cn</p>
        <p>地址：广东省佛山市顺德区乐从镇工业大道 88 号</p>
      </div>

      <div class="f-col">
        <h4>服务时间</h4>
        <p>周一至周六 8:30 - 18:00</p>
        <p>工厂展厅可预约参观</p>
        <p class="f-note">支持全国发货 · 上门安装</p>
      </div>
    </div>
    <div class="f-bottom">
      <div class="container">
        <span>© 2026 佛山市兔南家居制造有限公司 · 版权所有</span>
        <span>粤ICP备00000000号</span>
      </div>
    </div>
  </footer>
</template>

<style scoped>
.footer { background: #1e1a15; color: #cfc6b8; }
.footer-grid {
  display: grid;
  grid-template-columns: 1.5fr 1fr 1.2fr 1fr;
  gap: 48px;
  padding: 72px 0 56px;
}
.f-logo-wrap { display: flex; align-items: center; gap: 12px; }
.f-mark { width: 40px; height: 40px; flex: none; }
.f-logo {
  font-family: var(--serif);
  font-size: 24px;
  letter-spacing: 0.16em;
  color: #fff;
}
.f-en { font-size: 11px; letter-spacing: 0.3em; color: var(--gold); margin: 8px 0 16px; }
.f-desc { font-size: 13px; line-height: 1.9; max-width: 280px; }
.f-col { display: flex; flex-direction: column; gap: 12px; }
.f-col h4 { color: #fff; font-size: 15px; margin-bottom: 6px; letter-spacing: 0.14em; }
.f-col a, .f-col p { font-size: 13px; color: #a99e8f; }
.f-col a:hover { color: var(--gold); }
.f-note { color: var(--gold) !important; }
.f-bottom { border-top: 1px solid rgba(255, 255, 255, 0.08); }
.f-bottom .container {
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 8px;
  padding: 20px 0;
  font-size: 12px;
  color: #8b8172;
}
@media (max-width: 900px) {
  .footer-grid { grid-template-columns: 1fr 1fr; }
}
@media (max-width: 560px) {
  .footer-grid { grid-template-columns: 1fr; }
}
</style>