from django.urls import path, include
from . import views
from rest_framework import routers

routers = routers.DefaultRouter()
routers.register('languages', views.LanguageView)
routers.register('paradigm', views.ParadigmView)
routers.register('programmer', views.ProgrammerView)

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', include(routers.urls))

]
