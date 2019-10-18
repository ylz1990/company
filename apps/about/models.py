from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class AboutType(models.Model):
    about_type = models.CharField(max_length=20,verbose_name="关于我们",help_text="关于我们")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="发布时间", help_text="发布时间")

    def __str__(self):
        return self.about_type
    class Meta:
        ordering = ["id",'-created_time']
        db_table = "tb_about"  # 指明数据库表名
        verbose_name = "关于我们"  # 在admin站点中显示的名称
        verbose_name_plural = verbose_name  # 显示的复数名称

class About(models.Model):
    about_type = models.ForeignKey(AboutType, on_delete=models.DO_NOTHING, verbose_name="关于我们", help_text="关于我们")
    content = RichTextUploadingField(verbose_name="文章", help_text="文章")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="发布时间", help_text="发布时间")

    def __str__(self):
        return "<About: %s>" % self.about_type

    class Meta:
        ordering = ["id",'-created_time']
        db_table = "tb_company"  # 指明数据库表名
        verbose_name = "公司简介"  # 在admin站点中显示的名称
        verbose_name_plural = verbose_name  # 显示的复数名称