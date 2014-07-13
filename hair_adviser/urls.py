from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from django.contrib import admin

import review.tests
from hair_adviser import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hair_adviser.views.home', name='home'),
    url(r'^register/$', 'hair.views.register', name='register'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^about/$', 'hair.views.about', name='about'),
    url(r'^faq/$', 'hair.views.faq', name='faq'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^password_reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
    url(r'^password_reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    # Support old style base36 password reset links; remove in Django 1.7
    url(r'^reset/(?P<uidb36>[0-9A-Za-z]{1,13})-(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm_uidb36'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm',
        name='password_reset_confirm'),
    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),
    url(r'^$', 'hair.views.home', name='home'),
    url(r'^medicine/$', 'hair.views.medicine', name='medicine'),
    url(r'^medicine/(?P<post_id>\w+)$', 'hair.views.view_medicine_post', name='view_medicine_post'),
    url(r'^post/$', 'hair.views.post', name='post'),
    url(r'^law/$', 'hair.views.law', name='law'),
    url(r'^law/(?P<post_id>\w+)$', 'hair.views.view_law_post', name='view_law_post'),
    url(r'^sports/$', 'hair.views.sports', name='sports'),
    url(r'^sports/(?P<post_id>\w+)$', 'hair.views.view_sports_post', name='view_sports_post'),
    url(r'^music/$', 'hair.views.music', name='music'),
    url(r'^music/(?P<post_id>\w+)$', 'hair.views.view_music_post', name='view_music_post'),
    url(r'^programming/$', 'hair.views.programming', name='programming'),
    url(r'^programming/(?P<post_id>\w+)$', 'hair.views.view_programming_post', name='view_programming_post'),
    url(r'^acting/$', 'hair.views.acting', name='acting'),
    url(r'^acting/(?P<post_id>\w+)$', 'hair.views.view_acting_post', name='view_acting_post'),
    url(r'^profile/$', 'hair.views.profile', name='profile'),
    url(r'^edit/$', 'hair.views.edit', name='edit'),
    url(r'^review/', include('review.urls')),
    (r'^messages/', include('django_messages.urls')),

)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += patterns('',
#     url(r'^captcha/', include('captcha.urls')),
# )