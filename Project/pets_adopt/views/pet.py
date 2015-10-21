#coding:utf-8
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from pets_adopt.forms import Post_Pet,Adopt_Request_Form,Change_User_State
from pets_adopt.models import Pets,Adopt


def index(request):
    template_name = 'pets_adopt/index.html'
    if request.method =='POST':
        old_state = request.user
        form = Change_User_State(request.POST,instance=old_state)
        form.save()
        show_all_pet = Pets.objects.all()
        return render(request,template_name,{'shows':show_all_pet,"form":form})
    else:
        form = Change_User_State()
        show_all_pet = Pets.objects.all()
        return render(request,template_name,{'shows':show_all_pet,"form":form})



@login_required
def new_pet(request):
    template_name = 'pets_adopt/writing.html'
    if request.method == 'POST':
        form = Post_Pet(request.POST)
        if form.is_valid:
            Pets = form.save(commit=False)
            Pets.pet_publisher = request.user
            Pets.save()
            return redirect('pet_detail',pets_id=Pets.id)
    else:
        form = Post_Pet()
        return render(request,template_name,{'form':form})


def pet_detail(request, pets_id):
    template_name = 'pets_adopt/pets_detail.html'
    pet = get_object_or_404(Pets, id=pets_id)
    return render(request,template_name,{'pet':pet})

@login_required
def pet_adopt(request,pets_id):
    template_name = "pets_adopt/adopt_form.html"
    if request.method == 'POST':
        form = Adopt_Request_Form(request.POST)
        if form.is_valid:
            pets = Pets.objects.get(id = pets_id)
            adopt = form.save(commit=False)
            adopt.adopt_person = request.user
            adopt.adopt_pet = pets
            adopt.mode = 0
            adopt.save()
            return redirect('pet_adopt_success',adopt_id=adopt.id)
    else:
        pet = get_object_or_404(Pets, id=pets_id)
        form = Adopt_Request_Form()
        return render(request,template_name,{'pet':pet, 'form':form})


def pet_adopt_success(request,adopt_id):
    template_name = "pets_adopt/adopt_success.html"
    adopt = get_object_or_404(Adopt, id=adopt_id)
    pet = adopt.adopt_pet
    return render(request,template_name,{'adopt':adopt,'pet':pet})

@login_required
def user_check_response(request):
    template_name = 'pets_adopt/check_response.html'
    pet = Pets.objects.filter(pet_publisher = request.user)
    all_adopt_request = Adopt.objects.filter(adopt_pet = pet)
    return render(request,template_name,{'all_adopt_requests':all_adopt_request})


