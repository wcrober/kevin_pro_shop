# Generated by Django 3.2.7 on 2021-09-23 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20210923_0108'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='service',
            options={'ordering': ('-created',), 'verbose_name_plural': 'Services'},
        ),
        migrations.AddField(
            model_name='service',
            name='desc',
            field=models.TextField(blank=True),
        ),
    ]