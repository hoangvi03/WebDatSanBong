from django.db import models

# Create your models here.

class DanhMuc(models.Model):
    tenDM = models.CharField(max_length=100)
    
class SanPham(models.Model):
    tenSP = models.CharField(max_length=100)
    donGia = models.CharField(max_length=10)
    hinhanh = models.CharField(max_length=100)
    maDM = models.ForeignKey(DanhMuc, on_delete=models.CASCADE)