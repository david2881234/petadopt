#coding:utf-8
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from pets_adopt.forms import Post_Pet,Adopt_Request_Form,Comment_Form
from pets_adopt.models import Pets,Adopt,Comment
from django.contrib import messages


def index(request): #首頁,顯示所有寵物資訊,並能更改狀態
    template_name = 'pets_adopt/index.html'
    pet_not_adopt = Pets.objects.filter(state=0)
    pet_have_adopt = Pets.objects.filter(state=1)
    return render(request,template_name,{'pet_not_adopt':pet_not_adopt,'pet_have_adopt':pet_have_adopt})



@login_required
def new_pet(request): #PO一個寵物送養資訊,確認後顯示寵物細節
    template_name = 'pets_adopt/post_a_pet.html'
    if request.method == 'POST':
        form = Post_Pet(request.POST,request.FILES)
        if form.is_valid:
            image_file = request.FILES["photo"]
            Pets = form.save(commit=False)
            Pets.photo = image_file
            Pets.pet_publisher = request.user
            Pets.pet_owner = request.user
            Pets.save()
            messages.success(request,u'新增寵物成功')
            return redirect('pet_detail',pets_id=Pets.id)
    else:
        form = Post_Pet()
        return render(request,template_name,{'form':form})


def pet_detail(request, pets_id): #顯示寵物細節,已領養 或 登入者就是寵物擁有者時,沒有領養按鈕
    template_name = 'pets_adopt/pets_detail.html'
    template_name2 = 'pets_adopt/pets_detail2.html'
    pet = get_object_or_404(Pets, id=pets_id)
    if (pet.pet_owner == request.user) or (pet.state == 1):
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
            messages.success(request,u'領養訊息已送出')
            #return redirect('pet_adopt_success',adopt_id=adopt.id)
            return redirect('index')
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
        adopt_already = Adopt.objects.filter(adopt_pet = pet,mode = 4)
        adopt_request_standby = Adopt.objects.filter(adopt_pet = pet,mode = 0)
        adopt_request_have_sent = Adopt.objects.filter(adopt_pet = pet,mode = 1)
        return render(request,template_name,{'standby_pets':adopt_request_standby,'sent_pets':adopt_request_have_sent,
                                             'already':adopt_already})

@login_required
def user_check_confirm(request): #顯示待領養者確認的寵物
    if request.method =='POST':
        return redirect('pet_adopt_second_confirm')
    else:
        template_name = 'pets_adopt/adopt_action/check_confirm.html'
        adopt_confirmed = Adopt.objects.filter(adopt_person = request.user, mode=3)
        adopt_not_yet = Adopt.objects.filter(adopt_person = request.user, mode=0)
        return render(request,template_name,{'adopts_confirmed':adopt_confirmed,'adopts_not_yet':adopt_not_yet})
# mode=0:待批準,1:通過,2:拒絕,3:待領養者確認,4:待送養者確認

def pet_adopt_first_confirm(request, adopt_id): #將那個領養表單設定待收養者確認,其他拒絕
    template_name = 'pets_adopt/adopt_action/adopt_success1.html'
    adopt_yes = get_object_or_404(Adopt, id=adopt_id) #允許的領養者
    adopt_yes.mode = 3
    adopt_yes.save()
    pet = adopt_yes.adopt_pet
    all_adopt_request = Adopt.objects.filter(adopt_pet = pet)
    for each_adopt in all_adopt_request:  #其他人全部設拒絕
        if each_adopt == 0:
            each_adopt.mode = 2
            each_adopt.save()
    adopt_person = adopt_yes.adopt_person
    return render(request,template_name,{'adopt_yes':adopt_yes,'adopt_person':adopt_person})


def pet_adopt_second_confirm(request, adopt_id): #收養者確認領養，等待送養者last check
    template_name = 'pets_adopt/adopt_action/adopt_success2.html'
    adopt_yes = get_object_or_404(Adopt, id=adopt_id) #被挑中的領養者
    adopt_yes.mode = 4
    adopt_yes.save()
    pet = adopt_yes.adopt_pet
    publisher = pet.pet_publisher
    #pet.state = 1
    #pet.pet_publisher = adopt_yes.adopt_person
    #pet.save()
    return render(request,template_name,{'adopt_yes':adopt_yes,'publisher':publisher})


def pet_adopt_last_confirm(request, adopt_id): #送養者確認完畢後，將那個領養表單設定為已領養，寵物state也設定為已領養,主人換掉
    adopt_yes = get_object_or_404(Adopt, id=adopt_id)
    pet = adopt_yes.adopt_pet
    pet_new_owner = pet.pet_owner
    if request.method == 'POST': #信用評價
        template_name = 'pets_adopt/adopt_action/comment_success.html'
        form = Comment_Form(request.POST)
        comment = form.save(commit=False)
        comment.person = pet_new_owner
        comment.save()
        all_comment = Comment.objects.filter(person = pet_new_owner)
        good = 0
        ok = 0
        bad=0
        for cmt in all_comment: #顯示這個人的評價
            if cmt.credit == 0:
                good += 1
            elif cmt.credit == 1:
                ok += 1
            elif cmt.credit == 2:
                bad += 1
        return render(request,template_name, {'comment':comment,'good':good,'ok':ok,'bad':bad})
    else:
        template_name = 'pets_adopt/adopt_action/adopt_success3.html'
        adopt_yes.mode = 1
        adopt_yes.save()
        pet.state = 1
        pet.pet_owner = adopt_yes.adopt_person
        pet.save()
        form = Comment_Form()
        return render(request,template_name,{'adopt_yes':adopt_yes,'pet':pet,'form':form})