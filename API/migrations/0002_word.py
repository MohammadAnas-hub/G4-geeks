# Generated by Django 4.0.2 on 2022-08-06 21:27

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('word_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('score', models.FloatField()),
                ('wordUser', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='speaker', to='API.usermodell')),
            ],
        ),
    ]
