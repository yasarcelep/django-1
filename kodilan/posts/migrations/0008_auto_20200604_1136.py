# Generated by Django 3.0.6 on 2020-06-04 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_auto_20200601_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(0, 'ONAYLANMADI'), (1, 'ONAYLANDI'), (2, 'YAYINLANMADI')]),
        ),
    ]