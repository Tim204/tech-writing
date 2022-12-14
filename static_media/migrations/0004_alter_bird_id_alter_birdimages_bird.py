# Generated by Django 4.1.3 on 2022-11-20 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('static_media', '0003_alter_birdimages_bird'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bird',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='birdimages',
            name='bird',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='bird_images', to='static_media.bird'),
        ),
    ]
