# Generated by Django 3.2.23 on 2023-11-28 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_alter_post_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='picture',
            field=models.ImageField(default='blog/default.jpg', upload_to='blog/'),
        ),
    ]
