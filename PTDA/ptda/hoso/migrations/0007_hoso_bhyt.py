# Generated by Django 5.1.2 on 2024-11-02 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hoso', '0006_benhan_dieu_tri_benhan_trieu_chung_hoso_gioi_tinh_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='hoso',
            name='bhyt',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]