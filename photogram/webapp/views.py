from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.contrib.auth.decorators import login_required

from .forms import PostForm

def hello(request: HttpRequest) -> HttpResponse:
    # return HttpResponse('Hello World')
    return render(request, 'webapp/hello.html')

@login_required(login_url='/admin/login/')
def post_photo(request: HttpRequest):
    if request.method=='POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form_save = form.save(commit=False)
            form_save.fk_user = request.user
            form_save.save()
            return HttpResponse('Foto salva')
    else:
        form = PostForm()
    return render(request, 'webapp/index.html', { 'form': form })
