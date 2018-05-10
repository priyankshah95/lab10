from weather import Weather

from django.shortcuts import render

from django.views.generic.base import TemplateView
class HomeView(TemplateView):

	template_name = "home.html"

	def get(self,request,*args,**kwargs):

		context = self.get_context_data(**kwargs)

		weather = Weather()

		location = weather.lookup_by_location('halifax')

		condition = location.condition()

		context['condition'] = condition

		return self.render_to_response(context)



