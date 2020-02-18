from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from range.models import Score
from django.db import transaction
# Create your views here.

def show(requests):
	start = requests.POST.get('start')
	end = requests.POST.get('end')
	name = requests.POST.get('name')
	score_list = Score.objects.all()
	name = Score.objects.filter(name=name)
	if name:
		name = name[0]
	else:
		name = None
	try:
		start = int(start)
		end = int(end)
	except:
		start = 0
		end = len(score_list)
	
	score_list = sorted(score_list, key=lambda x:x.score)
	return render(requests,'show.html',{
		'score_list':score_list,'start':start,'end':end,'name':name})

def add(requests):
	name = requests.POST.get('name')
	score = requests.POST.get('score')
	Score.objects.create(name=name, score=score)
	return HttpResponseRedirect('/range/show/')

def rank(requests):
	start = requests.POST.get('start')
	end = requests.POST.get('end')
	return render(requests,'range.html')