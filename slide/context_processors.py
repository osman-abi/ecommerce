from .models import Slide

def slide(request):
    return {'slide':Slide.objects.all()}