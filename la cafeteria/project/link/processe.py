from .models import LinksModels

def get_list_processe(request):
    ctr ={}
    models = LinksModels.objects.all()
    for model in models:
        ctr[model.key] = model.link
    return ctr