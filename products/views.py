from django.shortcuts import get_object_or_404, redirect, render

from .forms import ProductForm
from .models import Product


def product_list(request):
    products = Product.objects.all()

    if request.method == "POST":
        form = ProductForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("product_list")
    else:
        form = ProductForm()

    return render(
        request,
        "products/product_list.html",
        {
            "form": form,
            "products": products,
        },
    )


def product_update(request, id):
    product = get_object_or_404(Product, id=id)

    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)

        if form.is_valid():
            form.save()
            return redirect("product_list")
    else:
        form = ProductForm(instance=product)

    return render(
        request,
        "products/product_update.html",
        {
            "form": form,
        },
    )


def product_delete(request, id):
    product = get_object_or_404(Product, id=id)

    if request.method == "POST":
        product.delete()
        return redirect("product_list")

    return render(
        request,
        "products/product_delete.html",
        {
            "product": product,
        },
    )