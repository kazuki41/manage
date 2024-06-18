from django.urls import path
from . import views
from manage_app.views import ManageList, ManageLoginView, ManageCreate, ManageDetail, ManageUpdate, ManageDelete, PersonList
from django.contrib.auth.views import LogoutView

urlpatterns = [
 path("",ManageList.as_view(), name="topicks"),
 path("login/",ManageLoginView.as_view(), name="login"),
 path("logout/",LogoutView.as_view(next_page="login"), name="logout"),
 path("create/",ManageCreate.as_view(), name="create"),
 path("topicks/<int:pk>/", ManageDetail.as_view(), name="topick"),
 path("update/<int:pk>/", ManageUpdate.as_view(), name="update"),
 path("delete/<int:pk>/", ManageDelete.as_view(), name="delete"),
 path('<str:person_type>/<str:person_name>/', PersonList.as_view(), name='person_list'),
]
