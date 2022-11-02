from django.urls import path
from partnership.views import CommentView

app_name = 'partnership'

urlpatterns = [
    path('', CommentView.as_view, name="comment")
]