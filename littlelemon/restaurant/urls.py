from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router: DefaultRouter = DefaultRouter()
router.register(r'tables', views.BookingViewSet, basename='booking')

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.MenuItemView.as_view(), name='menu-list'),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view(), name='menu-detail'),
    path('booking/', include(router.urls), name='booking'),
    path('api-token-auth/', obtain_auth_token),
]
