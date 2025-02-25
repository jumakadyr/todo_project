from django.urls import path
from account.views.user import register, user_login, user_logout, activate
from account.views.password import (
    CustomPasswordChangeView,
    CustomPasswordChangeDoneView,
    CustomPasswordResetView,
    CustomPasswordResetDoneView,
    CustomPasswordResetConfirmView,
    CustomPasswordResetCompleteView
)

app_name = 'account'

urlpatterns = [
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', register, name='register'),
    path('activate/<uidb64>/<token>/', activate, name='activate'),
]

urlpatterns += [
    path('password-change/', CustomPasswordChangeView.as_view(), name='password-change'),
    path('password-reset/', CustomPasswordResetView.as_view(), name='password-reset'),
    path('password-change/done/', CustomPasswordChangeDoneView.as_view(), name='password-change-done'),
    path('password-reset/done/', CustomPasswordResetDoneView.as_view(), name='password-reset-done'),
    path('password-reset/complete/', CustomPasswordResetCompleteView.as_view(), name='password-reset-complete'),
    path('password-reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password-reset-confirm'),
]