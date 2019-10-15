# Generated by Django 2.0 on 2019-10-09 21:57

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HeadlineNews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='新闻标题', max_length=50, verbose_name='新闻标题')),
                ('author', models.CharField(help_text='新闻来源', max_length=20, verbose_name='新闻来源')),
                ('read_num', models.IntegerField(default=0, help_text='阅读次数', verbose_name='阅读次数')),
                ('text', models.TextField(help_text='文章摘要', max_length=500, verbose_name='文章摘要')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(help_text='文章', verbose_name='文章')),
                ('created_time', models.DateTimeField(auto_now_add=True, help_text='发布时间', verbose_name='发布时间')),
                ('img_url', models.ImageField(blank=True, default='', upload_to='HeadlineNews')),
            ],
            options={
                'verbose_name': '头条新闻',
                'verbose_name_plural': '头条新闻',
                'db_table': 'tb_headline_news',
                'ordering': ['id', '-created_time'],
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='新闻标题', max_length=50, verbose_name='新闻标题')),
                ('author', models.CharField(help_text='新闻来源', max_length=20, verbose_name='新闻来源')),
                ('read_num', models.IntegerField(default=0, help_text='阅读次数', verbose_name='阅读次数')),
                ('text', models.TextField(help_text='文章摘要', max_length=500, verbose_name='文章摘要')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(help_text='文章', verbose_name='文章')),
                ('created_time', models.DateTimeField(auto_now_add=True, help_text='发布时间', verbose_name='发布时间')),
            ],
            options={
                'verbose_name': '新闻中心',
                'verbose_name_plural': '新闻中心',
                'db_table': 'tb_news',
                'ordering': ['id', '-created_time'],
            },
        ),
    ]