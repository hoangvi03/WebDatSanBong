from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home,name='home'),
    path('themdm',views.ThemDM,name='themdm'),
    path('xemsptheoloai/<int:madm>', views.XemSPTheoLoai, name='xemsptheoloai'),
    path('xemchitietsp<int:masp>', views.XemChiTietSP, name='xemchitietsp'),
    path('xemgiohang', views.XemGioHang, name='xemgiohang'),
    path('themgiohang<int:msp>', views.ThemGioHang, name='themgiohang'),
]