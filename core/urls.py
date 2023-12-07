from django.urls import path
from .views import*
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', index),
    path('about/', about),
    path('signup/', signup),
    path('signin/', LoginView.as_view(template_name = 'core/signin.html', authentication_form = SignInForm)),
    path('signout/', LogoutView.as_view(next_page = '/')),
    path('profile/<int:id>/', profile),
    path('post/<int:id>/', detail),
    path('post/upload/', postUpload),
    path('post/update/<int:id>/', postUpdate),
    path('post/delete/<int:id>/', postDelete),
    path('profile/update/<int:id>/', profileUpdate),
    path('comment/delete/<int:id>/', commentDelete),
]