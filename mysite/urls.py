from django.conf.urls import patterns, include, url
from mysite.views import hello, current_datetime, hours_ahead, display_meta
from books.views import search_form, search
from contact.views import success_page, contact
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^hello/$',hello),
	url(r'^time/$',current_datetime),
	url(r'^time/plus/(\d{1,2})/$',hours_ahead),
	url(r'^admin/',include(admin.site.urls)),
	url(r'^meta/$', display_meta),
	#url(r'^search-form/$', search_form),
	url(r'^search/$', search),
	url(r'^contact/thanks/$', success_page),
	url(r'^contact/$', contact),
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
