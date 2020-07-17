# Generated by Django 2.2.10 on 2020-04-08 18:46

from django.db import migrations, models
import django.db.models.deletion
import djangocms_text_ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
        ('slides', '0002_auto_20200408_1201'),
    ]

    operations = [
        migrations.CreateModel(
            name='KipyaCard',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='slides_kipyacard', serialize=False, to='cms.CMSPlugin')),
                ('card_image', models.ImageField(upload_to='uploads/general_images/', verbose_name='Card Image')),
                ('card_content', djangocms_text_ckeditor.fields.HTMLField(blank=True, default='', help_text='Content may also be added using child plugins.', verbose_name='Card Content')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]