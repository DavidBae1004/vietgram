from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views
from images import views as image_views

urlpatterns = [
    url(
        regex=r'^$',
        view=user_views.index,
        name='index'
        ),
    url(
        regex=r'^login/$',
        view=user_views.login,
        name='login'
    ),
    url(
        regex=r'^explore/$',
        view=user_views.explore,
        name='explore'
    ),
    url(r'^daveadmin/', admin.site.urls),
    url(
        regex=r'^images/(?P<image_id>[\d+])/like/$',
        # ?P<iamges_id>[\d+] / for the name of <iamges_id>, as the type number -->[\d+]  
        view=image_views.like_image,
        name='like_image'
    ),
        url(
        regex=r'^images/(?P<image_id>[\d+])/comment/$',
        # ?P<iamges_id>[\d+] / for the name of <iamges_id>, as the type number -->[\d+]  
        view=image_views.comment_image,
        name='comment_image'
    ),
    url(
        regex=r'profile/(?P<username_from_url>.+)/$',
        view=user_views.profile,
        name='profile'
    ),
        url(
        regex=r'images/(?P<iamag>.+)/$',
        view=user_views.profile,
        name='profile'
    ),
    
    


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
