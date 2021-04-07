from .models import Article

def blog(request):
    return {'blogs':Article.objects.all()}