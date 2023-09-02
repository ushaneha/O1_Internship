from django.shortcuts import render
import json
import random

# Create your views here.
def task(request):
    with open('o1_project/bts_members.json', 'r') as file:
        bts_members = json.load(file)
    random_member = random.choice(bts_members)
    context = {'bts_member': random_member}
    return render(request, 'task.html', context)




def index(request):
    return render(request,'index.html')
