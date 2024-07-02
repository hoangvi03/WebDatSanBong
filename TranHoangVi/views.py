from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import DanhMuc, SanPham
from django.contrib import messages

# Create your views here.
def Home(request):
    return render(request, 'pages/home.html')

def ThemDM(request):
    dm = DanhMuc.objects.all()
    data = {
        'DanhMuc' : dm,
    }
    if request.method == 'POST':
        tendm = request.POST.get('tenDM')
        if tendm:
            DanhMuc.objects.create(
                tenDM = tendm
            )
            return redirect('themdm')
    return render(request, 'pages/ThemDanhMuc.html', data)

def XemSPTheoLoai(request, madm):
    sp = SanPham.objects.filter(maDM=madm)
    dm = DanhMuc.objects.get(id=madm)
    data = {
        'SanPham' : sp,
        'DanhMuc' : dm
    }
    return render(request, 'pages/XemSanPham.html', data)

def XemChiTietSP(request, masp):
    sp = SanPham.objects.get(id=masp)
    data = {
        '1SanPham' : sp
    }
    return render(request, 'pages/XemCTSP.html', data)

def ThemGioHang(request, msp):
    cart = request.session.get('cart', {})
    sp = SanPham.objects.get(id=msp)
    if msp in cart:
        cart[msp]['soluong'] += 1
    else:
        cart[msp]={
            'name' : sp.tenSP,
            'gia' : sp.donGia,
            'soluong': 1,
        }
    request.session['cart'] = cart
    messages.success(request, f"Thêm {sp.tenSP} vào giỏ hàng thành công!")
    return redirect('xemgiohang')

def XemGioHang(request):
    cart = request.session.get('cart', {})
    data = {
        'Gio' : cart
    }
    return render(request, 'pages/XemGioHang.html', data)
    