from django.shortcuts import render
from django.http import HttpResponse,Http404,JsonResponse
import requests
import json


	


def index(request):
	return render(request,'athena/index.html')


def searchReq(request):
	res=False
	req={"query":None,"domains":None}
	js='{"em":"1"}';
	if request.method == 'GET':
		query=request.GET.get('query')
		domains=request.GET.get('domains')
		if(domains==""):
			domains=None
		if(domains!=None):
			domains=domains.split(',')
		req={"query":query,"domains":domains}
		
		try:
			response = requests.get('https://api.coursera.org/api/courses.v1?q=search&query='+query+'&includes=instructorIds,partnerIds&fields=instructorIds,domainTypes,partnerIds,partnerLogo,photoUrl,certificates,description,previewLink')	
			if(not request.is_ajax()):
				js=response.content
			else:
				js=response.json()
			res=True
		except:
			res=False
	else:
		if(not request.is_ajax()):	
			raise Http404("Invalid Request")
	context={"result":js,"success":res,"request":json.dumps(req)}
	if(request.is_ajax()):
		return JsonResponse(context)
	else:
		return render(request,'athena/searchPage.html',context)


