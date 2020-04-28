# Generated by Django 2.2.5 on 2020-04-28 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offlineTask', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SingleImageIdentifyInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('singleImageId', models.IntegerField(verbose_name='')),
                ('is_confirm', models.BooleanField()),
                ('is_identify', models.BooleanField(default=False)),
                ('is_show', models.BooleanField(default=False)),
                ('imagePreprocessPath', models.CharField(max_length=10000, verbose_name='')),
                ('imageIdentifyPath', models.CharField(max_length=10000, verbose_name='')),
                ('imageIdentifyResultPath', models.CharField(max_length=10000, verbose_name='')),
                ('overDate', models.CharField(max_length=45, verbose_name='')),
            ],
            options={
                'verbose_name': '图片识别信息',
                'verbose_name_plural': '图片识别信息',
            },
        ),
        migrations.CreateModel(
            name='SingleImageSpliceInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('singleImageId', models.IntegerField(verbose_name='')),
                ('is_splice', models.BooleanField(default=False)),
                ('imagePreprocessPath', models.CharField(max_length=10000, verbose_name='')),
                ('imageSplicePath', models.CharField(max_length=10000, verbose_name='')),
                ('overDate', models.CharField(max_length=45, verbose_name='')),
            ],
            options={
                'verbose_name': '图片比对信息',
                'verbose_name_plural': '图片比对信息',
            },
        ),
    ]