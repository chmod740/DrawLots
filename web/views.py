import random

from django.shortcuts import render, render_to_response, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

from web.models import User, Draw, DrawResult
# Create your views here.
def login(req):
    return render_to_response('login.html')

@csrf_exempt
def check_login(req):
    username = req.POST.get('username')
    password = req.POST.get('password')
    users = User.objects.filter(username__exact=username, password__exact=password)
    if len(users) == 0:
        return render_to_response('login.html', {'msg':'用户名或密码不正确'})
    else:
        user = {'username':users[0].username, 'name': users[0].name, 'user_group': users[0].user_group}
        req.session['user'] = user
        return HttpResponseRedirect('index.html')

def index(req):
    try:
        user = req.session['user']
    except:
        user = None
        return HttpResponseRedirect('login.html')
    draws = Draw.objects.filter(user_group__exact=user.get('user_group'))
    return render_to_response('index.html', {'user': user, 'draws': draws})

def logout(req):
    req.session.clear()
    return HttpResponseRedirect('login.html')

def draw(req):
    try:
        user = req.session['user']
    except:
        user = None
        return HttpResponseRedirect('login.html')


    user = User.objects.get(username__exact=user.get('username'))
    try:
        id = req.GET.get('id')
        id = int(id)
        draw_obj = Draw.objects.get(id__exact=id)

        if draw_obj.user_group != user.user_group:
            return HttpResponseRedirect('login.html')

        draw_results = DrawResult.objects.filter(user__exact=user, draw__exact=draw_obj)
        if len(draw_results) == 0:
            draw_result = None
        else:
            draw_result = draw_results[0]
        draw_results = DrawResult.objects.filter(draw__exact=draw_obj)
        return render_to_response('draw.html', {'draw_id': id, 'draw_result': draw_result, 'draw_results': draw_results})
    except:
        return HttpResponseRedirect('index.html')

def get_my_draw(req):
    draw_id = req.GET.get('id')
    draw_id = int(draw_id)
    try:
        draw_obj = Draw.objects.get(id__exact=draw_id)
        user = req.session['user']
        user = User.objects.get(username__exact=user.get('username'))
        drawResults = DrawResult.objects.filter(user__exact=user, draw__exact=draw_obj)

        if draw_obj.user_group != user.user_group:
            return HttpResponseRedirect('login.html')
        if len(drawResults) == 0:
            temp_list = draw_obj.data.split()
            data_list = []
            for element in temp_list:
                data_list.append(int(element))
            drawResults = DrawResult.objects.filter(draw_id__exact=draw_id)
            for element in drawResults:
                data_list.remove(element.result)
            i = random.randint(0, len(data_list)-1)
            drawResult = DrawResult()
            drawResult.user = user
            drawResult.draw = draw_obj
            drawResult.result = data_list[i]
            drawResult.save()
            return HttpResponseRedirect('draw.html?id=' + str(draw_id))
        else:
            return HttpResponseRedirect('draw.html?id=' + str(draw_id))
    except:
        return HttpResponseRedirect('index.html')