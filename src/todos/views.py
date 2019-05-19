from django.shortcuts import render,get_object_or_404
from django.views.generic import View
from django.forms.models import model_to_dict
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse

import json

from .forms import ToDoForm
from .models import ToDo

class IndexView(View):
    """ 
    View for Index Page 

    URL : '/'
    """
    return_data = {}
    template_name = "index.html"

    def get(self, request,*args, **kwargs):
        return render(request,self.template_name,self.return_data)


class TodosView(View):
    """
    View for To Do List and Delete
    URL : '/todos/'
    """
    return_data = {}
    template_name = "todo_list.html"

    def get(self, request,*args, **kwargs):
        """
        GET : For listing ToDos
        """
        self.return_data['todos'] = ToDo.objects.filter(active=True).order_by('-pk')
        return render(request,self.template_name,self.return_data)

    def post(self, request,*args, **kwargs):
        """
        POST : For Deleting ToDo
        """
        if request.is_ajax:
            try:
                todo = ToDo.objects.get(id=request.POST['id']) 
                todo.active = False
                todo.save()
                data = json.dumps({'status':'success'})
            except:
                data = json.dumps({'status':'error'})

            return HttpResponse(data, content_type='application/json')

        return render(request,self.template_name,self.return_data)

class DetailsView(View):
    """
    View for To Do Details view
    URL : '/todos/<pk>/'
    """
    return_data = {}
    template_name = "details.html"

    def get(self, request,*args, **kwargs):
        if kwargs:
            self.return_data['todo'] = ToDo.objects.get(pk=kwargs['pk'])
        return render(request,self.template_name,self.return_data)


class CreateView(View):
    """
    View for Creating and Updating ToDos
    URL for create : '/todos/add/'
    URL for update : '/todos/add/<pk>/'
    """
    return_data = {}
    template_name = "add_todo.html"

    def get(self, request,*args, **kwargs):
        """
        GET : Rendering ToDoForm for create/update
        """
        if kwargs:
            todo = ToDo.objects.get(pk=kwargs['pk'])
            self.return_data['form'] = ToDoForm(initial=self.get_initial(todo))
        else:
            self.return_data['form'] = ToDoForm()
        return render(request,self.template_name,self.return_data)

    def post(self, request,*args, **kwargs):
        """
        POST : Create/update by form submission
        """
        form = ToDoForm(request.POST)

        if form.is_valid():
            if kwargs:
                todo = ToDo.objects.get(pk=kwargs['pk'])
                form.save(todo)
            else:
                form.save()
            return HttpResponseRedirect("/todos/")

        self.return_data['form'] = form
        return render(request,self.template_name,self.return_data)

    def get_initial(self,todo):
        initial = {}
        initial['title'] = todo.title
        initial['description'] = todo.description
        initial['date'] = todo.date.strftime("%Y-%m-%d %H:%M:%S")
        initial['status'] = todo.status
        return initial


class ToDoApiView(View):
    """
    Api for ToDo :  List & Individual view
    URL for List API : '/app/v1/todos/'
    URL for Get ToDo : '/app/v1/todos/<pk>/'
    """
    def get(self, request,*args, **kwargs):
        if kwargs:
            todo = get_object_or_404(ToDo, pk=kwargs['pk'])
            data = {"results": {
                "title": todo.title,
                "description": todo.description,
                "date": todo.date,
                "status": todo.status,
                "created": todo.created,
                "modified": todo.modified,
                "active": todo.active,
            }}
            return JsonResponse(data)
        else:
            MAX_OBJECTS = 20
            todos = ToDo.objects.filter()[:MAX_OBJECTS]
            data = {"results": list(todos.values("title", "description", "date", 
                "status", "created", "modified", "active"))}
            return JsonResponse(data)
