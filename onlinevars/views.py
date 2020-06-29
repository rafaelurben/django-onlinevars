from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseBadRequest

import json

from .models import Variable

# Create your views here.

@csrf_exempt
def api_v1(request, name):
    answer = {
        "name": name,
        "value": None,
        "error": None,
        "cleaned": False,
        "created": False,
        "changed": False,
        "deleted": False
    }

    if request.method == "GET":
        clean = request.GET.get("clean", False)
        create = request.GET.get("create", False)

        if Variable.objects.filter(name=name).exists():
            var = Variable.objects.get(name=name)
            value = var.value
            answer["value"] = value
            if clean and value is not None:
                var.value = None
                var.save()
                answer["cleaned"] = True
            else:
                answer["value"] = var.value
        elif create:
            Variable.objects.create(name=name, value=None)
            answer["created"] = True
        else:
            answer["error"] = f"Var '{name}' not found!"
        return HttpResponse(json.dumps(answer), content_type="application/json")
    elif request.method == "POST":
        value = request.POST.get("value", None)
        append = request.POST.get("append", False)

        if value:
            if request.POST.get("multiple", False):
                names = name.split(",")
            else:
                names = [name]
            for name in names:
                var = Variable.objects.get_or_create(name=name)[0]
                var.value = ((((var.value+"\n") if var.value else "") + (value.strip() or "")) if append else value.strip()) or None
                var.save()

            answer["value"] = value
            answer["changed"] = True
        else:
            answer["error"] = "Missing value! Please send data as application/x-www-form-urlencoded!"
        return HttpResponse(json.dumps(answer), content_type="application/json")
    elif request.method == "DELETE":
        if Variable.objects.filter(name=name).exists():
            Variable.objects.get(name=name).delete()
            answer["deleted"] = True
        else:
            answer["error"] = f"Var '{name}' not found!"
        return HttpResponse(json.dumps(answer), content_type="application/json")
    else:
        answer["error"] = "Use GET, POST or DELETE"
        return HttpResponseBadRequest(json.dumps(answer), content_type="application/json")

# Chat

def chat_start(request):
    if request.method == "GET":
        return render(request, "onlinevars/chat_start.html")
    elif request.method == "POST":
        mykey = request.POST["mykey"]
        postkey = request.POST["postkey"]
        return redirect(f"/onlinevars/chat/{postkey}/{mykey}/")

def chat(request, postkey, mykey):
    mykey = mykey.replace("chat_","")
    postkey = "chat_"+(",chat_".join(postkey.replace("chat_","").replace(" ","").split(",")))
    return render(request, "onlinevars/chat.html", context={"mykey": mykey, "postkey": postkey})
