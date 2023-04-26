from django.urls import path,include
from .import views
from .import models
from rest_framework import routers

router = routers.DefaultRouter()
# router.register('Table1', views.NewitemTableView)
# router.register('Table', views.TableView)
router.register('login', views.loginView)
router.register('secondary', views.SecondaryView)



urlpatterns = [
    path('', include(router.urls)),
    # path('Tables/<int:Table_no>',views.TableView,name='TableView')

]