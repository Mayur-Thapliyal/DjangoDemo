from rest_framework.routers import DefaultRouter
from app_user.views import UserView
router=DefaultRouter()
router.register('user',viewset=UserView,basename='User') 

urlpatterns = []
urlpatterns+=router.urls