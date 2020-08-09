from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from gestor_general.models import User
from gestor_general.models import Post
from gestor_general.models import Ansewer_Post
from datetime import datetime


# Create your views here.
user_object = {"nickname": "", "description":"","id":0}
state_user = False

def log_in(request):
    global user_object
    user_object = {"nickname": "", "description":"","id":0}
    return render(request,"login.html",{"err":False})

def verificar(request):
    global state_user
    global user_object
    #sign in verification
    nickname_post = request.POST["nickname-post"]
    password_post = request.POST["password-post"]
    
    users = User.objects.all()

    for user in users:
        if user.nickname == nickname_post:
            if user.password == password_post:
                state_user = True
                
    
    if state_user:
        user_db = User.objects.filter(nickname=nickname_post)
        for x in user_db:
            nickname_register = x.nickname
            description_register = x.personal_description
            id_register = x.id
        user_object = {"nickname": nickname_post , "description": description_register,"id":id_register}
        return HttpResponseRedirect("/foro/all")             
    else:
        return render(request,"login.html",{"err":True})
 

def foro(request,sector):
    global user_object
    global state_user
    sector = sector.lower()
    #Uso el estado del usuario y el objeto usuario
    if sector == "all":
        posts = Post.objects.all()
        categorys = ["Programming","Life","Football","Bussines","All"]
        return render(request,"index.html",{"user":user_object,"posts":posts,"state_user":state_user,"categorys":categorys})

    elif sector == "programming":
        #Obtengo los post de la categoria programacion
        posts = Post.objects.filter(category=sector)
        categorys = ["Bussines","Life","Football","All","Programming"]
        return render(request,"index.html",{"user":user_object,"posts":posts,"state_user":state_user,"categorys":categorys})

    elif sector == "bussines":
        posts = Post.objects.filter(category="bussines")
        categorys = ["Programming","Life","Football","All","Bussines"]
        return render(request,"index.html",{"user":user_object,"posts":posts,"state_user":state_user,"categorys":categorys})
        
    elif sector == "life":
        posts = Post.objects.filter(category="life")
        categorys = ["Programming","Bussines","Football","All","Life"]
        return render(request,"index.html",{"user":user_object,"posts":posts,"state_user":state_user,"categorys":categorys})

    elif sector == "football":
        posts = Post.objects.filter(category="football")
        categorys = ["Programming","Life","Bussines","All","Football"]
        return render(request,"index.html",{"user":user_object,"posts":posts,"state_user":state_user,"categorys":categorys})
            
    else:
        return(request,"index_fail.html")

def personal_post(request,user_name):
    global state_user
    global user_object

    if state_user:
        if user_object["nickname"] == user_name:
            posts = Post.objects.filter(nickname_dad=user_object["nickname"])
            return render(request,"index.html",{"user":user_object,"posts":posts,"state_user":state_user})
        else:
            return HttpResponseRedirect("/")
        
        
def register(request):
    return render(request,"Singup.html")


def validity_register(request):
    global state_user
    global user_object

    nickname_new = request.POST["nickname-post"]
    password_new = request.POST["password-post"]
    description_new = request.POST["description-post"]
    perfil_photo_new = request.FILES.get("image-post")
    all_users = User.objects.all()

    availability = True

    print(perfil_photo_new)

    for user in all_users:
        if user.nickname == nickname_new:
            availability = False

    if availability:
        if request.FILES.get("image-post") != None or perfil_photo_new != None:
            User.objects.create(nickname = nickname_new, password = password_new,personal_description = description_new,photo = perfil_photo_new)
        else:
             User.objects.create(nickname = nickname_new, password = password_new,personal_description = description_new)


        #Obtengo el id del usuario
        users = User.objects.all()

        for user in users:
            if user.nickname == nickname_new:
                new_id = user.id
        
        user_object = {"nickname": nickname_new, "description": description_new ,"id": new_id}
        state_user = True

        return HttpResponseRedirect("/foro/all")
    else:
        return render(request,"register_fail.html")




def new_post(request):
    global user_object
    global state_user

    if state_user:
        return render(request,"add_post.html",{"user":user_object})
    else:
        return HttpResponseRedirect("/")

def add_post(request):
    global user_object
    global state_user
    if state_user:

        title = request.POST["post-title"]
        content = request.POST["post-content"]
        category = request.POST["post-category"]
        img = request.FILES.get("post-img")
        nickname_dad = user_object["nickname"]

        if request.FILES.get("post-img") == None:
            Post.objects.create(title = title, content = content , category = category,nickname_dad = nickname_dad,ansewer = False)
        else:
            Post.objects.create(title = title, content = content , category = category,img = img,nickname_dad = nickname_dad,ansewer = False)   
        
        return HttpResponseRedirect("/foro/all")

    else:
        return HttpResponseRedirect("/")

def read_post(request,id):
    global user_object
    global state_user

    status_imagen = False
    post_data = Post.objects.filter(id = id)
    ansewer = False

    for data in post_data:
        nickname_author = data.nickname_dad
        post_id = data.id
        if data.img != "image-user.png" :
            status_imagen= True
        if data.ansewer:
            ansewer = True


    autor_data = User.objects.filter(nickname=nickname_author)

    ansewers=None    

    if ansewer:
        ansewers = Ansewer_Post.objects.filter(id_post_ansewer=post_id)

    return render(request,"post.html",{"post_data":post_data,"autor_data":autor_data,"user":user_object,"state":state_user,"status1":status_imagen,"status_ansewer":ansewer,"body_ansewers":ansewers,"post_id":post_id})


def ansewer(request,id):
    global state_user
    global user_object
    if state_user:
        post = Post.objects.filter(id=id)
        for data in post:
            title = data.title
        return render(request,"ansewer_post.html",{"id":id,"title":title,"user":user_object})
    else:
        return HttpResponseRedirect("/")

def save_ansewer(request,id):
    global state_user
    global user_object
    if state_user:
        content_ans = request.POST["post-content"]
        post = Post.objects.get(id=id)
        post.ansewer = True
        post.save()
        Ansewer_Post.objects.create(content=content_ans,id_post_ansewer=id,nickname_create=user_object["nickname"])

        return HttpResponseRedirect("/post/read/%s" %(id))
    else:
        return HttpResponseRedirect("/")