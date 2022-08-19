# Generated by Django 4.0.2 on 2022-08-15 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0004_remove_word_pronunciation_word_spokenaudio_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='correctAudio',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='word',
            name='correctPhonetics',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='word',
            name='spokenPhonetics',
            field=models.TextField(null=True),
        ),
    ]