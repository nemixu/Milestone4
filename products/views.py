from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from profiles.models import UserProfile
from .models import Product, Category, Review
from .forms import ProductForm, ReviewForm

# Create your views here.


def all_products(request):
    """ A view to show products """
    products = Product.objects.all()
    categories = None
    
    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)
    
    context = {
        'products' : products,
        'current_categories' : categories,
    }
    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual class details and reviews for that specific class """

    product = get_object_or_404(Product, pk=product_id)
    reviews = Review.objects.filter(product=product_id)
    review_form = ReviewForm()
    context = {
        'product': product,
        'reviews': reviews,
        'page_title': product.name,
        'review_form': review_form
    }

    return render(request, 'products/product_detail.html', context)

@login_required
def add_product(request):
    """add products to the store"""
    if not request.user.is_superuser:
        messages.error(request, 'Oops! You don\'t have the required permission\
        to access this page. Login with the required credentials to do so!')
        return redirect(reverse('home'))
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added a product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:        
        form = ProductForm()
    
    page_title = 'Add a product'    
    template = 'products/add_product.html'
    context = {
        'form': form,
        'page_title': page_title,
    }
    
    return render(request, template, context)

@login_required
def edit_product(request, product_id):
    """edit a product and update to the db"""
    if not request.user.is_superuser:
        messages.info(request, 'Oops! You don\'t have the required \
                      permission to access this page. Login with the \
                      required credentials to do so!')
        return redirect(reverse('home'))
    
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f'You have successfully updated {product.name}.')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to edit product. Please ensure the form is valid.')
            
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')
    
    page_title = 'Edit a product'    
    template = 'products/edit_product.html'
    context = {
        'form':form,
        'product': product,
        'page_title': page_title,
    }
    
    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """Delete a product from products"""
    if not request.user.is_superuser:
        messages.error(request, 'Oops! You don\'t have the required permission\
        to access this page. Login with the required credentials to do so!')
        return redirect(reverse('home'))
    
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product has been deleted!')
    
    return redirect(reverse('home'))


def add_review(request, product_id):
    """View to handle the POST of reviews from a specific user"""
    user_profile = UserProfile.objects.get(user=request.user)
    product = get_object_or_404(Product, pk=product_id)
    reviews = Review.objects.filter(product=product_id)
    review_form = ReviewForm()
    context = {
        "product": product,
        "reviews": reviews,
        "review_form": review_form,        
    }
    return render(request, 'products/product_detail.html', context)
    
    
    
    # if request.method == "POST":
    #     user_profile = UserProfile.objects.get(user=request.user)
    #     product = get_object_or_404(Product, pk=product_id)
    #     reviews = Review.objects.filter(product=product_id)
    #     form_data = {
    #         'comment': request.POST['comment'],
    #     }

    #     review_form = ReviewForm(form_data)
        
    #     if review_form.is_valid():
    #         comment = review_form.save(commit=False)
    #         comment.save()
    #         messages.success(request, "comment added")
            
    #     else:
    #         messages.error(request, "Sorry that failed")
            
    # else:
    #     review_form = ReviewForm()
    # template = "products/product_detail.html"
    # context = {
    #     "product": product,
    #     "reviews": reviews,
    #     "review_form": review_form,        
    # }
    # return render(request, template , context)
    # if request.user.is_authenticated:
    #     product = get_object_or_404(Product, pk=product_id)
    #     reviews = Review.objects.filter(product=product_id)
    #     review_form = ReviewForm()
    #     return render(request, 'products', context)
    #     if request.method == "POST":
    #         review_form = ReviewForm(request.POST, instance=product)
    #         if review_form.is_valid():
    #             review_form.save()
    #             messages.success(request, f'You have successfully left a rating for {product.name}.')
    #             return redirect(reverse('product_detail', args=[product.id]))
    #     else:
    #         review_form = ReviewForm()
    #     return render(request, 'products', context)
    
    # else:
    #     return redirect('home')