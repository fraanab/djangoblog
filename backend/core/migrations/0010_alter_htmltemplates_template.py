# Generated by Django 4.1.4 on 2022-12-28 00:01

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_htmltemplates_template'),
    ]

    operations = [
        migrations.AlterField(
            model_name='htmltemplates',
            name='template',
            field=models.FileField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location='/core/templates/htmlmails'), upload_to=''),
        ),
    ]
