# Generated by Django 2.2.10 on 2020-04-08 08:53

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ADSSubscriber',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('fullname', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
