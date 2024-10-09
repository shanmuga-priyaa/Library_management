from django.urls import path
from .views import *

urlpatterns = [
    path('memberadd/', memberaddView.as_view()),
    path('memberlist/',memberlistView.as_view()),
    path('memberdelete/<int:id>/',memberdeleteView.as_view(),name="member_delete")
]