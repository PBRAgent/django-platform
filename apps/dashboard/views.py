from django.shortcuts import render


# Create your views here.
def index(request):
    data_list = [{"name": "foo"}, {"name": "bar"}]
    return render(request, "index.html", context={"users": data_list})
