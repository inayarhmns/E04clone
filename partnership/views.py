from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.views import View
from partnership.forms import CommentForm

class CommentView(View):
    form_class = CommentForm
    def get(self, request, *args, **kwargs):
        return render(request, "comments/partnership.html", {})

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponse({'message': 'success'})
            return HttpResponse({'message': 'field couldn\'t validate'})
        return HttpResponse({'message': 'Wrong request'})