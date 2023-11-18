from django.shortcuts import render
from .models import Post


# Create your views here.
from django.views.generic import ListView,DeleteView,CreateView,DetailView,UpdateView

class List_post(ListView):                                      # context=  name_model.list            post_list   object.post
    model=Post                                                  # templates   new_model.action         post._list
    
class Detail_post(DetailView):                                 # context name_model                    post  or object
    model=Post                                                 # template    name_model.action         post_detail

class Create_post(CreateView):
    model=Post
    fields='__all__'
    success_url='/posts/'
class Update_post(UpdateView):
    pass
class Delete_post(DeleteView):
    pass

