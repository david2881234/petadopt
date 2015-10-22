#coding:utf-8
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from pets_adopt.forms import Post_Pet,Adopt_Request_Form,Change_User_State
from pets_adopt.models import Pets,Adopt


def index(request): #首頁,顯示所有寵物資訊,並能更改狀態
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
def new_pet(request): #PO一個寵物送養資訊,確認後顯示寵物細節
    template_name = 'pets_adopt/post_a_pet.html'
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


def pet_detail(request, pets_id): #顯示寵物細節,已領養 或 登入者就是送養者時,沒有領養按鈕
    template_name = 'pets_adopt/pets_detail.html'
    template_name2 = 'pets_adopt/pets_detail2.html'
    pet = get_object_or_404(Pets, id=pets_id)
    if (pet.pet_publisher == request.user) or (pet.state == 1):
        return render(request,template_name2,{'pet':pet})
    return render(request,template_name,{'pet':pet})

#以下為收養者發出欲收養訊息,收養者檢視全部收養人,並決定一個適合的收養人

@login_required
def pet_adopt(request,pets_id): #收養者填寫收養單,發給送養者
    template_name = "pets_adopt/adopt_action/sent_form.html"
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


def pet_adopt_success(request,adopt_id): #成功送出送養訊息畫面
    template_name = "pets_adopt/adopt_action/sent_success.html"
    adopt = get_object_or_404(Adopt, id=adopt_id)
    pet = adopt.adopt_pet
    return render(request,template_name,{'adopt':adopt,'pet':pet})

@login_required
def user_check_response(request): #送養者檢查所有發布的寵物,已送養的也會顯示
    if request.method =='POST':
        return redirect('pet_adopt_confirm')
    else:
        template_name = 'pets_adopt/adopt_action/check_response.html'
        pet = Pets.objects.filter(pet_publisher = request.user)
        adopt_request_standby = Adopt.objects.filter(adopt_pet = pet,mode = 0)
        adopt_request_have_sent = Adopt.objects.filter(adopt_pet = pet,mode = 1)
        return render(request,template_name,{'standby_pets':adopt_request_standby,'sent_pets':adopt_request_have_sent})


def pet_adopt_confirm(request, adopt_id): #將那個領養表單設定通過,其他拒絕,寵物標記為已領養
    template_name = 'pets_adopt/adopt_action/adopt_success.html'
    adopt_yes = get_object_or_404(Adopt, id=adopt_id) #允許的領養者
    adopt_yes.mode = 1
    adopt_yes.save()
    pet = adopt_yes.adopt_pet
    all_adopt_request = Adopt.objects.filter(adopt_pet = pet)
    for each_adopt in all_adopt_request:  #其他人全部設拒絕
        if each_adopt == 0:
            each_adopt.mode = 2
            each_adopt.save()
    pet.state = 1
    pet.save()
    return render(request,template_name,{'adopt_yes':adopt_yes})