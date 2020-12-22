from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Articles
from .forms import ArticleForm

class ArticleList(ListView):
    template_name = "articles/list.html"
    model = Articles
    context_object_name = "articles"
    paginate_by = 10

class ArticleCreate(LoginRequiredMixin, CreateView):
    login_url = "/accounts/login"
    template_name = "articles/create.html"
    form_class = ArticleForm
    success_url = reverse_lazy("list")

class ArticleDetail(DetailView):
    template_name = "articles/detail.html"
    model = Articles
    context_object_name = "article"

class ArticleUpdate( UpdateView):
    template_name = "articles/edit.html"
    model = Articles
    context_object_name = "article"
    form_class = ArticleForm

    def get_success_url(self):
        return reverse("detail", kwargs={"pk": self.object.pk})

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Articles, pk=kwargs["pk"])
        if article.create_user.id == self.request.user.id:
            return super().get(request, **kwargs)
        else:
            return render(self.request, "403.html")

class ArticleDelete(DeleteView):
    model = Articles
    success_url = reverse_lazy("list")
    template_name = "articles/list.html"

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Articles, pk=kwargs["pk"])
        if article.create_user.id == self.request.user.id:
            return super().get(request, **kwargs)
        else:
            return render(self.request, "403.html")

    def delete(self, request, *args, **kwargs):
        result = super().delete(request, *args, **kwargs)
        messages.success(
            self.request, '「{}」を削除しました'.format(self.object))
        return result