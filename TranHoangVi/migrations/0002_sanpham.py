# Generated by Django 5.0.4 on 2024-05-31 02:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TranHoangVi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SanPham',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tenSP', models.CharField(max_length=100)),
                ('donGia', models.CharField(max_length=10)),
                ('hinhanh', models.CharField(max_length=100)),
                ('maDM', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TranHoangVi.danhmuc')),
            ],
        ),
    ]
