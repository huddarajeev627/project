'''from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from blog.views import BlogPostViewSet

router = DefaultRouter()
router.register(r'posts', BlogPostViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
'''
from django.contrib import admin
from django.urls import path
from blog.views import home, RegisterView, BlogListCreateView, BlogDetailView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('', home),  # 👈 root URL par hello message
    path('admin/', admin.site.urls),

    # Auth
    path('api/register/', RegisterView.as_view()),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Blog
    path('api/posts/', BlogListCreateView.as_view()),
    path('api/posts/<int:pk>/', BlogDetailView.as_view()),
]
