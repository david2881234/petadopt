from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from pets_adopt.forms import Blog_Post
from pets_adopt.models import Pets,Adopt
from pets_adopt.models import Blog
from django.utils import timezone



def post_list(request, pets_id):
    template = 'pets_adopt/blog/post_list.html'
    pet = get_object_or_404(Pets, id=pets_id)
    blog = Blog.objects.filter(pet = pet)
    can_post = False
    if (pet.pet_owner == request.user):
        can_post = True
    return render(request, template, {'posts': blog, 'pet': pet,'can_post':can_post})


def post_new(request, pets_id):
    template = 'pets_adopt/blog/post_new.html'
    pet = get_object_or_404(Pets, id=pets_id)
    if request.method == 'POST':
        form = Blog_Post(request.POST, request.FILES)
        if form.is_valid:
            image_file = request.FILES["photo"]
            blog = form.save(commit=False)
            blog.photo = image_file
            blog.author = request.user
            blog.pet= pet
            blog.published_date = timezone.now()
            blog.save()
            return redirect('post_list', pets_id=pet.id)
    else:
        form = Blog_Post()
        return render(request, template, {'pet': pet, 'form': form})


def question_index(request):
    template = 'pets_adopt/extra/questionnaire.html'
    return render(request, template, {'nbar': 'question'})


def question_handle(request):
    template = 'pets_adopt/extra/question_result.html'
    result = 0
    right = False
    for i in range(1, 11):
        if request.POST.get('Q' + str(i)) == 'T':
            result += 10
    if result >= 70:
        right = True
    return render(request, template, {'right': right, 'result': result, 'nbar': 'question'})
