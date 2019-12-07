from django.urls import path
from fieldsapp.views import BlogListView, NewPostView

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('new/', NewPostView.as_view(), name='pole')

]
