# Create your views here.
from django.http import HttpResponse, HttpRequest
from django.template import Context, loader
from slideshow.core.models import Slideshow

def home(request):
    t = loader.get_template('index.html')
    c = Context({
        'title': "Slideshow Project!",
        'user': request.user,
})
    return HttpResponse(t.render(c))
