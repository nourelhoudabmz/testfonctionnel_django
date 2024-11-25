"""
This file contains all the functions and views of Userapp Application.
"""
# Third Party imports.
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

# Local imports.
from userapp.forms import SignupForm
from userapp.models import Category, Product, Tag


def signup(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()
            return HttpResponseRedirect('/accounts/login')
        else:
            return render(request, 'userapp/register.html', {'error': form.errors, 'form': form})
    return render(request, 'userapp/register.html', {'form': form})


@method_decorator(login_required, name='dispatch')
class GetCategory(ListView):
    """
        This class is used to get the list of all the categories
        available in category model of userapp Application
    """
    model = Category
    template_name = 'userapp/category_list.html'
    context_object_name = 'categories'


@method_decorator(login_required, name='dispatch')
class CreateCategory(CreateView):
    """
        This class is used to create a Category in Category Model.
    """
    model = Category
    fields = '__all__'

    def get_success_url(self):
        return reverse('all-categories')


@method_decorator(login_required, name='dispatch')
class UpdateCategory(UpdateView):
    """
        This class is used to update an existing
        category object of Category Model.
    """
    model = Category
    fields = '__all__'

    def get_success_url(self):
        return reverse('all-categories')


@method_decorator(login_required, name='dispatch')
class DeleteCategory(DeleteView):
    """
        This class is used to Delete a Category from Category Model.
    """
    model = Category

    def get_success_url(self):
        return reverse('all-categories')


# ----------------------Tag CRUD------------------

@method_decorator(login_required, name='dispatch')
class GetTag(ListView):
    model = Tag
    template_name = 'userapp/tag_list.html'
    context_object_name = 'tags'


@method_decorator(login_required, name='dispatch')
class CreateTag(CreateView):
    model = Tag
    fields = '__all__'

    def get_success_url(self):
        return reverse('all-tags')


@method_decorator(login_required, name='dispatch')
class UpdateTag(UpdateView):
    model = Tag
    fields = '__all__'

    def get_success_url(self):
        return reverse('all-tags')


@method_decorator(login_required, name='dispatch')
class DeleteTag(DeleteView):
    model = Tag

    def get_success_url(self):
        return reverse('all-tags')


# ---------------------Product CRUD-------------
@method_decorator(login_required, name='dispatch')
class GetProduct(ListView):
    model = Product
    template_name = 'userapp/product_list.html'
    context_object_name = 'products'


@method_decorator(login_required, name='dispatch')
class CreateProduct(CreateView):
    model = Product
    fields = '__all__'

    def get_success_url(self):
        return reverse('all-product')


@method_decorator(login_required, name='dispatch')
class UpdateProduct(UpdateView):
    model = Product
    fields = '__all__'

    def get_success_url(self):
        return reverse('all-product')


@method_decorator(login_required, name='dispatch')
class DeleteProduct(DeleteView):
    model = Product

    def get_success_url(self):
        return reverse('all-product')
