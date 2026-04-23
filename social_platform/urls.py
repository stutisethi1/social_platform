from django.contrib import admin
from django.urls import path, include   
from .views import home
from accounts.views import signup, login_view, logout_view
from friends.views import send_request, accept_request
from api.views import get_posts
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

    path('send-request/<int:user_id>/', send_request, name='send_request'),
    path('accept-request/<int:request_id>/', accept_request, name='accept_request'),

    path('api/posts/', get_posts),


    path('posts/', include('posts.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)