def foro(request,sector):
    global user_object
    global state_user
    
    if state_user:
        if sector == "all":
            posts = Post.objects.all()
            dates_user = {"nickname":user_object.name,"description":user_object.description,"id":user_object.id}
            for x in creator_post:
                author_post = x.nickname

            return render(request,"index.html",{"user":dates_user,"posts":posts})

        elif sector == "programming":
            #Obtengo los post de la categoria programacion
            posts = Post.objects.filter(category=sector)
            dates_user = {"nickname":user_object.name,"description":user_object.description,"id":user_object.id}

            return render(request,"index.html",{"user":dates_user,"posts":posts})

        elif sector == "bussines"):
            posts = Post.objects.filter(category="bussines")
            dates_user = {"nickname":user_object.name,"description":user_object.description,"id":user_object.id}


            return render(request,"index.html",{"user":dates_user,"posts":posts})
        
        elif sector == "life":
            posts = Post.objects.filter(category="life")
            dates_user = {"nickname":user_object.name,"description":user_object.description,"id":user_object.id}

            return render(request,"index.html",{"user":dates_user,"posts":posts})

        elif sector == "football":
            posts = Post.objects.filter(category="football")
            dates_user = {"nickname":user_object.name,"description":user_object.description,"id":user_object.id}

            return render(request,"index.html",{"user":dates_user,"posts":posts})
            
        elif user_object.nickname == sector:
            posts = Post.objects.filter(nickname_dad=sector)
            dates_user = {"nickname":user_object.name,"description":user_object.description,"id":user_object.id}

            return render(request,"index.html",{"user":dates_user,"posts":posts})
        else:
            return(request,"index_fail.html")
    else:
        return HttpResponseRedirect("/")