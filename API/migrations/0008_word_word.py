# Generated by Django 4.0.2 on 2022-08-15 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0007_alter_word_spokenaudio'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='word',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
