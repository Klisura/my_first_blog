# Generated by Django 4.2.5 on 2023-12-06 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app_blog', '0003_alter_post_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='header_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
