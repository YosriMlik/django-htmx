from django.urls import path, include
from authentification.views import *

urlpatterns = [
    path('login/', login),
    path('profile/', profile, name="account_profile"),
    path('signup/', signup, name='account_signup'),
    path('password/reset/', password_reset, name="account_password_reset"),
    path('password/reset/done/', password_reset_done),
    path('password/change/', password_change),
    #path('password/reset/key/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$', CustomPasswordResetConfirmView.as_view()),
    #path('password/reset/key/e-set-password/', CustomPasswordResetConfirmView.as_view()),
    #path('password/reset/key/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view()),
    path('confirm-email/<key>/', email_confirm),
    path('logout/', logout),
    path('', include('allauth.urls')),
]