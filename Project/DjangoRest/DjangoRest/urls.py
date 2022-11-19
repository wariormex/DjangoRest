from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .views import HomeTemplateView, TestAuthView, LogoutViewEx, ItemReturnAllView, ItemReturnView
from dj_rest_auth.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test_auth/', TestAuthView.as_view(), name='test_auth', ),
    path('item-return-all/', ItemReturnAllView.as_view(), name='item_return_all', ),
    path('item-return/<int:pk>', ItemReturnView.as_view(), name='item_return', ),
    path('rest-auth/logout/', LogoutViewEx.as_view(), name='rest_logout', ),
    path('rest-auth/login/', LoginView.as_view(), name='rest_login', ),
    path('', HomeTemplateView.as_view(), name='home', ),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

