from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class GoldType(models.Model):
    gold_type = models.CharField(max_length=20,verbose_name="黄金学堂",help_text="黄金学堂")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="发布时间", help_text="发布时间")

    def __str__(self):
        return self.gold_type
    class Meta:
        ordering = ["id",'-created_time']
        db_table = "tb_gold_type"  # 指明数据库表名
        verbose_name = "黄金学堂"  # 在admin站点中显示的名称
        verbose_name_plural = verbose_name  # 显示的复数名称



# 全部新闻
class Golds(models.Model):
    title = models.CharField(max_length=50, verbose_name="新闻标题", help_text="新闻标题")
    author = models.CharField(max_length=20, verbose_name="新闻来源", help_text="新闻来源")
    gold_type = models.ForeignKey(GoldType, on_delete=models.DO_NOTHING, verbose_name="黄金学堂", help_text="黄金学堂")
    read_num = models.IntegerField(default=0, verbose_name="阅读次数", help_text="阅读次数")
    text = models.TextField(max_length=500, verbose_name="文章摘要", help_text="文章摘要")
    content = RichTextUploadingField(verbose_name="文章", help_text="文章")
    created_time = models.DateTimeField(auto_now_add=True,verbose_name="发布时间", help_text="发布时间")

    def __str__(self):
        return "<Golds: %s>" % self.title

    class Meta:
        ordering = ["id", '-created_time']
        db_table = "tb_gold"  # 指明数据库表名
        verbose_name = "黄金新闻"  # 在admin站点中显示的名称
        verbose_name_plural = verbose_name  # 显示的复数名称