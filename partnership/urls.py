from django.urls import path
from partnership.views import CommentView, CommentDataView

app_name = 'partnership'

urlpatterns = [
    path('', CommentView.as_view(), name="comment"),
    path('view', CommentDataView.as_view(), name="comment_data")
]