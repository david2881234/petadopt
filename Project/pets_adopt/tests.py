from pets_adopt.models import NewUser,Pets,Adopt

user = NewUser.objects.filter(username='david2881234')
pet = Pets.objects.filter(pet_publisher=user)
ado = Adopt.objects.filter(adopt_pet = pet)


# Create your tests here.
