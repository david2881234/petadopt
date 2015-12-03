from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from pets_adopt.forms import Blog_Post
from pets_adopt.models import Pets,Adopt
from pets_adopt.models import Blog
from django.utils import timezone



def post_list(request, pets_id):
    template = 'pets_adopt/blog/post_list.html'
    template2 = 'pets_adopt/blog/post_list_no_create.html'
    pet = get_object_or_404(Pets, id=pets_id)
    blog = Blog.objects.filter(pet = pet)
    if (pet.pet_owner == request.user):
        return render(request, template, {'posts': blog, 'pet': pet})
    else:
        return render(request, template2, {'posts': blog, 'pet': pet})

def post_new(request, pets_id):
    template = 'pets_adopt/blog/post_new.html'
    pet = get_object_or_404(Pets, id=pets_id)
    if request.method == 'POST':
        form = Blog_Post(request.POST)
        if form.is_valid:
            blog = form.save(commit=False)
            blog.author = request.user
            blog.pet= pet
            blog.published_date = timezone.now()
            blog.save()
            return redirect('post_list', pets_id=pet.id)
    else:
        form = Blog_Post()
        return render(request, template, {'pet': pet, 'form': form})
