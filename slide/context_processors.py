from .models import Slide

def slide(request):
    return {'slides':Slide.objects.all()}