
def new_post(request):
    return render(request,"add_post.html")

def add_post(request):
    global user_object

    title = request.POST["post-title"]
    content = request.POST["post-content"]
    category = request.POST["category"]
    img = request.FILES.get("post-img")
    nickname_dad = user_object["nickname"]

    if request.FILES.get("post-img") == "":
        Post.objects.create(title = title, content = content , category = category,nickname_dad = nickname_dad)
    else:
        Post.objects.create(title = title, content = content , category = category,img = img,nickname_dad = nickname_dad)   
    
    return HttpRensponseRedirect("/ ")