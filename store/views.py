from django.shortcuts import render


def index(request):
    return render(
        request, 'index.html'
    )


def product(request, pid):
    return render(
        request, 'product.html'
    )


def category(request, cid):
    return render(
        request, 'category.html'
    )


def cart(request):
    return render(
        request, 'cart.html'
    )


def checkout(request):
    return render(
        request, 'checkout.html'
    )


def checkout_complete(request):
    return render(
        request, 'checkout_complete.html'
    )