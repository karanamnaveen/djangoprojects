from django.shortcuts import render
from appOne.models import Product
from django.http import HttpResponseRedirect
from appOne.forms import ProductForm

# Create your views here.
def getProducts(request):
    products = Product.objects.all()
    return render(request, 'templates/index.html', {'products': products})

def createProduct(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/') # redirect to home page
    return render(request, 'templates/createProduct.html', {'form': form})

def deleteProduct(request, id):
    products = Product.objects.get(id=id)
    products.delete()
    return HttpResponseRedirect('/') # redirect to
    # return redirect('/')

def updateProduct(request, id):
    # we getting the data from database, we are using the data to create a form
    product = Product.objects.get(id=id)
    # ProductForm Constructor is taking the data then configure "instance=product" (product is object)
    # It tells the Constructor to use the 'product' and create a form
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST,instance=product)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request,'templates/updateProduct.html', {'form': form})
