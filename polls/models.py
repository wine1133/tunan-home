from django.db import models


class Contract(models.Model):
    """联系表单提交记录。"""

    contact = models.CharField("联系人", max_length=50)
    phone = models.CharField("联系电话", max_length=20)
    company = models.CharField("公司/品牌", max_length=100, blank=True, default="")
    project_type = models.CharField("项目类型", max_length=50, default="成品采购")
    quantity = models.CharField("预计数量", max_length=50, default="10 件以内")
    city = models.CharField("交付城市", max_length=50, blank=True, default="")
    budget = models.CharField("预算区间", max_length=50, default="1 万以内")
    message = models.TextField("需求说明", blank=True, default="")
    created_at = models.DateTimeField("提交时间", auto_now_add=True)

    class Meta:
        db_table = "contract"
        verbose_name = "表单数据"
        verbose_name_plural = "表单数据"

    def __str__(self):
        return f"{self.contact}（{self.phone}）"