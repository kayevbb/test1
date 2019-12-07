from pyexpat.errors import messages

from django import http
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator

from .forms import ProfileForm
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, TemplateView
from .models import Post, Fields


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'


class NewPostView(LoginRequiredMixin, CreateView):
    model = Fields
    template_name = 'new_post.html'
    form_class = ProfileForm
    success_url = reverse_lazy('home')

class ProfileView(TemplateView):
    template_name = "blog.html"

