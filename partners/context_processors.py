from .models import Partner,Banner

def partner(request):
    return {
        'banners':Banner.objects.all(),
        'partners':Partner.objects.all()
    }