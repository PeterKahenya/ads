# Generated by Django 2.2.10 on 2020-04-08 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('slides', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slide',
            name='slide_id',
        ),
        migrations.AlterField(
            model_name='slide',
            name='cmsplugin_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='slides_slide', serialize=False, to='cms.CMSPlugin'),
        ),
    ]