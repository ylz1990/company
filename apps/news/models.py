from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

# 全部新闻
class News(models.Model):
    title = models.CharField(max_length=50, verbose_name="新闻标题", help_text="新闻标题")
    author = models.CharField(max_length=20, verbose_name="新闻来源", help_text="新闻来源")
    read_num = models.IntegerField(default=0, verbose_name="阅读次数", help_text="阅读次数")
    text = models.TextField(max_length=500, verbose_name="文章摘要", help_text="文章摘要")
    content = RichTextUploadingField(verbose_name="文章", help_text="文章")
    created_time = models.DateTimeField(auto_now_add=True,verbose_name="发布时间", help_text="发布时间")

    def __str__(self):
        return "<News: %s>" % self.title

    class Meta:
        ordering = ["id", '-created_time']
        db_table = "tb_news"  # 指明数据库表名
        verbose_name = "新闻中心"  # 在admin站点中显示的名称
        verbose_name_plural = verbose_name  # 显示的复数名称

# 头条新闻
class HeadlineNews(models.Model):
    title = models.CharField(max_length=50, verbose_name="新闻标题", help_text="新闻标题")
    author = models.CharField(max_length=20, verbose_name="新闻来源", help_text="新闻来源")
    read_num = models.IntegerField(default=0, verbose_name="阅读次数", help_text="阅读次数")
    text = models.TextField(max_length=500, verbose_name="文章摘要", help_text="文章摘要")
    content = RichTextUploadingField(verbose_name="文章", help_text="文章")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="发布时间", help_text="发布时间")
    img_url = models.ImageField(upload_to='HeadlineNews', default="", blank=True)  # upload_to指定图片上传的途径，如果不存在则自动创建

    def __str__(self):
        return "<News: %s>" % self.title

    class Meta:
        ordering = ["id", '-created_time']
        db_table = "tb_headline_news"  # 指明数据库表名
        verbose_name = "头条新闻"  # 在admin站点中显示的名称
        verbose_name_plural = verbose_name  # 显示的复数名称
