# Generated by Django 3.0.6 on 2020-06-01 19:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20200601_1853'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(null=True)),
                ('position', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('apply_url', models.URLField()),
                ('apply_email', models.EmailField(max_length=254)),
                ('location', models.CharField(max_length=200)),
                ('type', models.SmallIntegerField()),
                ('status', models.SmallIntegerField()),
                ('is_featured', models.BooleanField()),
                ('activation_code', models.CharField(max_length=200)),
                ('renewal_code', models.CharField(max_length=200)),
                ('notes', models.TextField()),
                ('pub_date', models.DateTimeField()),
                ('created_at', models.DateTimeField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Company')),
                ('tags', models.ManyToManyField(to='posts.Tag')),
            ],
        ),
    ]