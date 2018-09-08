from django.http import HttpResponse
from django.template import loader
from .models import List


def index(request):
    wish_list = List.objects.all()
    template = loader.get_template('polls/index.html')
    context = {
        'wish_list': wish_list,
    }
    return HttpResponse(template.render(context, request))
