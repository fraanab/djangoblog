# Generated by Django 4.1.4 on 2022-12-26 20:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_alter_comment_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Upvote',
        ),
    ]
