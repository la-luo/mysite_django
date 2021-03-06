
from django.conf.urls import url, include
from canteen import views

urlpatterns = [
    url(r'^$', views.search, name='home_view'),
    url(r'^restaurant/(?P<res_id>\d+)/$',views.restaurant, name='restaurant'),
    url(r'^menu/(?P<menu_ID>\d+)/$', views.menu, name='menu_view'),
    url(r'^menu-mobile/(?P<menu_ID>\d+)/$', views.menu_mobile),
    url(r'^joinus/$', views.join_us, name='join_us'),
    url(r'^success/$', views.success_view, name='success'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^account/$', views.account, name='account'),
    url(r'^edit-res/(?P<res_id>\d+)/$', views.edit_res, name='edit_res'),
    url(r'^edit-menu/(?P<menu_id>\d+)/$', views.edit_menu_info),
    url(r'^delete/(?P<res_id>\d+)/$', views.delete_res, name='delete_res'),
    url(r'^add-dish/(?P<menu_id>\d+)/$', views.add_dish),
    url(r'^account/edit_menu/(?P<menu_id>\d+)/$', views.edit_menu, name='edit_menu_view'),
    url(r'^edit-res/account/(?P<res_id>\d+)/$', views.edit_restaurant, name='edit_res_view'),
    url(r'^add-dishtype/(?P<menu_id>\d+)/$', views.add_dishtype, name='add_dishtype'),
    url(r'^delete-dishtype/(?P<menu_id>\d+)/(?P<dishtype>\w+)/$', views.delete_dishtype, name='delete_dishtype'),
    url(r'^edit-dish/(?P<dish_id>\d+)/$', views.edit_dish, name='edit_dish'),
    url(r'^delete-dish/(?P<dish_id>\d+)/$', views.delete_dish, name='delete_dish_view'),
    url(r'^payment/(?P<conversation_id>\d+)/$', views.payment),
    url(r'^sms/$', views.sms),
    url(r'^charge/(?P<conversation_id>\d+)/$', views.charge),
    url('^', include('django.contrib.auth.urls')),
]

#   url(r'^signup/$', views.signup, name='signup'),