from django.shortcuts import render_to_response
from django.template import RequestContext
from products.models import Product
from random import Random

def index(request, product_uuid=None):
    product = None if not product_uuid else Product.objects.get(uuid=product_uuid)
    if request.method == 'POST':
        p = Product()
        p.name = request.POST.get('name', None)
        p.description = request.POST.get('description', None)
        p.image_url = request.POST.get('image_url', None)
        p.url = request.POST.get('url', None)
        p.author = request.user if request.user.id else None
        p.save()
    if not product and Product.objects.count() != 0:
        product = Product.objects.order_by('-created')[0]
    ctx = {
        'product': product,
        'latest': Product.objects.order_by('-created')[:5],
    }
    return render_to_response('index.html', ctx, context_instance=RequestContext(request))
