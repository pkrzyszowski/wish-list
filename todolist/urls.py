from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from todolist_app.views import index, login_view, logout_view, submit, vote_up, vote_down, get_user_profile, delete, signup

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^login$', login_view, name='login'),
    url(r'^logout/$', logout_view, name='logout'),
    url(r'^submit$', submit, name='submit'),
    url(r'^signup$', signup, name='signup'),
    url(r'^vote-up/(?P<wish_id>\d+)/$', vote_up, name='vote-up'),
    url(r'^vote-down/(?P<wish_id>\d+)/$', vote_down, name='vote-down'),
    # url(r'^increase-points/(?P<user_id>\d+)/$', increase_points, name='increase-points'),
    url(r'^profile/(?P<user_id>\d+)$', get_user_profile, name='profile'),
    url(r'^delete/(?P<wish_id>\d+)/$', delete, name='delete'),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
