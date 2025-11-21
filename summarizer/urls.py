from django.urls import path, include
from . import views

urlpatterns = [
    path('test/',views.test),
    path('sum/',views.summary_view,name='sum')
]
