from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


class Recruit(models.Model):
    title = models.CharField(max_length=20,verbose_name="招聘岗位",help_text="招聘岗位")
    author = models.CharField(max_length=20,verbose_name="发布人",help_text="发布人")
    salary = models.CharField(max_length=20,verbose_name="薪资待遇",help_text="薪资待遇")
    responsibilities = RichTextUploadingField(verbose_name="岗位要求", help_text="岗位要求")
    content = RichTextUploadingField(verbose_name="岗位职责", help_text="岗位职责")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="发布时间", help_text="发布时间")
    img_url = models.ImageField(upload_to='recruit', default="", blank=True)  # upload_to指定图片上传的途径，如果不存在则自动创建

    def __str__(self):
        return "<Recruit: %s>" % self.title

    class Meta:
        ordering = ["id",'-created_time']
        db_table = "tb_recruit"  # 指明数据库表名
        verbose_name = "招聘中心"  # 在admin站点中显示的名称
        verbose_name_plural = verbose_name  # 显示的复数名称