from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class RuleType(models.Model):
    rule_type = models.CharField(max_length=20,verbose_name="制度与规则",help_text="制度与规则")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="发布时间", help_text="发布时间")

    def __str__(self):
        return self.rule_type
    class Meta:
        ordering = ["id",'-created_time']
        db_table = "tb_rule_type"  # 指明数据库表名
        verbose_name = "制度与规则"  # 在admin站点中显示的名称
        verbose_name_plural = verbose_name  # 显示的复数名称



class Rule(models.Model):
    title = models.CharField(max_length=50,verbose_name="标题",help_text="标题")
    rule_type = models.ForeignKey(RuleType, on_delete=models.DO_NOTHING,verbose_name="制度与规则",help_text="制度与规则")
    author = models.CharField(max_length=50,verbose_name="发布人",help_text="发布人")
    read_num = models.IntegerField(default=0,verbose_name="阅读次数", help_text="阅读次数")
    text = models.TextField(max_length=300,default="",verbose_name="文章摘要", help_text="文章摘要")
    content = RichTextUploadingField(verbose_name="文章", help_text="文章")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="发布时间", help_text="发布时间")


    def __str__(self):
        return "<Rule: %s>" % self.title

    class Meta:
        ordering = ["id",'-created_time']
        db_table = "tb_rule"  # 指明数据库表名
        verbose_name = "规则条例"  # 在admin站点中显示的名称
        verbose_name_plural = verbose_name  # 显示的复数名称
