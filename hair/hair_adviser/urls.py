from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from django.contrib import admin
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
    url(r'^law/$', 'hair.views.law', name='law'),
    url(r'^sports/$', 'hair.views.sports', name='sports'),
    url(r'^music/$', 'hair.views.music', name='music'),
    url(r'^programming/$', 'hair.views.programming', name='programming'),
    url(r'^acting/$', 'hair.views.acting', name='acting'),
    url(r'^ben_carson/$', 'hair.views.ben_carson', name='ben_carson'),
    url(r'^vivien_thomas/$', 'hair.views.vivien_thomas', name='vivien_thomas'),
    url(r'^profile/$', 'hair.views.profile', name='profile'),
    url(r'^edit/$', 'hair.views.edit', name='edit'),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += patterns('',
#     url(r'^captcha/', include('captcha.urls')),
# )