"""
URL configuration for mysite project.
"""
from django.contrib import admin
from django.urls import path, re_path
from django.views.generic import TemplateView

from polls.views import api_hello, contract_create

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/hello/", api_hello),
    path("api/contract/", contract_create),
    # 每个导航按钮对应一个独立的 HTML 根页面（多页面架构）
    path("", TemplateView.as_view(template_name="index.html")),
    path("products/", TemplateView.as_view(template_name="products.html")),
    path("factory/", TemplateView.as_view(template_name="factory.html")),
    path("custom/", TemplateView.as_view(template_name="custom.html")),
    path("contact/", TemplateView.as_view(template_name="contact.html")),
    # 兜底：其余路径回首页
    re_path(r"^.*$", TemplateView.as_view(template_name="index.html")),
]