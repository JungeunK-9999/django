# Generated by Django 2.2.3 on 2019-07-19 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190719_1457'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('d', 'Draft'), ('p', 'Published'), ('w', 'Withdrawn')], default='d', max_length=1),
            preserve_default=False,
        ),
    ]
