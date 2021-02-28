from django.shortcuts import render
from .models import *
# Create your views here.


def home(request):
	template_name = 'index.html'

	title = Param.objects.get(param_name='title')
	description = Param.objects.get(param_name='description')
	logo = Param.objects.get(param_name='logo')
	favicon = Param.objects.get(param_name='favicon')
	email = Param.objects.get(param_name='email')
	phone = Param.objects.get(param_name='phone')
	location = Param.objects.get(param_name='location')
	google_map = Param.objects.get(param_name='google_map')


	our_services_description = Param.objects.get(param_name='our_services_description')
	our_services_title = Param.objects.get(param_name='our_services_title')
	services = Service.objects.filter(activ=True)

	what_we_do_image = Param.objects.get(param_name='what_we_do_image')
	what_we_do_video_url = Param.objects.get(param_name='what_we_do_video_url')
	what_we_do_description = Param.objects.get(param_name='what_we_do_description')
	what_we_do_title = Param.objects.get(param_name='what_we_do_title')
	what_we_do_lignes = Param.objects.filter(param_name='what_we_do_lignes')

	our_projects_description = Param.objects.get(param_name='our_projects_description')
	our_projects_title = Param.objects.get(param_name='our_projects_title')
	projects = Project.objects.filter(activ=True)




	args = {
		'title':title,
		'logo':logo,
		'email':email,
		'phone':phone,
		'description':description,
		'location':location,
		'favicon':favicon,
		'google_map':google_map,
		
		'what_we_do_image': what_we_do_image,
		'what_we_do_video_url': what_we_do_video_url,
		'what_we_do_description': what_we_do_description,
		'what_we_do_title' :what_we_do_title,
		'what_we_do_lignes' :what_we_do_lignes,
		
		'services':services,
		'our_services_description':our_services_description,
		'our_services_title':our_services_title,
		
		'projects':projects,
		'our_projects_description':our_projects_description,
		'our_projects_title':our_projects_title,
	}

	return render(request  ,template_name , args)