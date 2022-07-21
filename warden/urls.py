from django.urls import path
import warden.views
urlpatterns = [
    path('warden_home/', warden.views.warden_home, name='warden_home'),
    path('w_home/', warden.views.w_home, name='w_home'),
    path('addatt/', warden.views.addatt, name='addatt'),
    path('addatt1/', warden.views.addatt1, name='addatt1'),
    # path('ex/', warden.views.ex, name='ex'),
    path('hreg/', warden.views.hreg, name='hreg'),
    path('w_rooma2/', warden.views.w_rooma2, name='w_rooma2'),
    path('b_pending/', warden.views.b_pending, name='b_pending'),
    path('approve_booking/<id>', warden.views.approve_booking, name='approve_booking'),
    path('reject_booking/<id>', warden.views.reject_booking, name='reject_booking'),
    path('approve_list_booking/', warden.views.approve_list_booking, name='approve_list_booking'),
    path('vacate/', warden.views.vacate, name='vacate'),
    path('w_room/', warden.views.w_room, name='w_room'),

    path('w_rooma/', warden.views.w_rooma, name='w_rooma'),
    path('w_rooma1/<id>', warden.views.w_rooma1, name='w_rooma1'),


    ]