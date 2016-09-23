from django.shortcuts import render, get_object_or_404
from .models import Product
from .forms import ProductAddForm

# Create your views here.
def detail_view(request, object_id=None):
    # this will be visible in the console/logs!
    print("The request is {}.\nThe user is {}.\nAuthenticated: {}."
          .format(request, request.user, request.user.is_authenticated))

    # and we can use this right away!!
    if request.user.is_authenticated:
        greeting = 'Hello {}'.format(str(request.user).capitalize())
    else:
        greeting = 'I don\'t know you'

    product = get_object_or_404(Product, id=object_id)
    template = 'detail_view.html'
    context = {'greeting': greeting,
               'object': product,
               }
    return render(request, template, context)


def create_view(request):
    # None is so that we can load an empty page
    # and only raise validation errors when the data has been submitted
    form = ProductAddForm(request.POST or None)
    print(request.POST)
    if form.is_valid():
        # turns request data from QueryDict to a dictionary and removes CSRF token
        # will only include valid fields!
        data = form.cleaned_data
        print(data)
        # now we extract values from the clean data and
        # and construct a new Product instance with them, then save it
        title = data.get('title')
        description = data.get('description')
        price = data.get('price')
        is_available = data.get('is_available')
        new_product = Product.objects.create(
            title=title, description=description, price=price, is_available=is_available
        )
        #new_product.save()  # this is not needed, the new item is already saved
    template = 'create_view.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


def detail_slug_view(request, slug=None):
    print('The slug is', slug)
    product = get_object_or_404(Product, slug=slug)
    # product = 1
    greeting = 'Hello!'
    template = 'detail_view.html'
    context = { 'greeting': greeting,
                'object': product,
               }
    return render(request, template, context)

def list_view(request):
    template = 'list_view.html'
    context = {}
    return render(request, template, context)
