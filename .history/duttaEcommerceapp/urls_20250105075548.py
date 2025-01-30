#Paths - http://127.0.0.1:8000/
from django.urls import path
from .views.home_view import HomePageView
from .views.auth_views import SignUpView, CustomLoginView, CustomPasswordResetView, product_listing_view
from .views.cart_viewbackup import cart_view, update_cart, remove_from_cart, update_quantity
from .views.paymentview import proceed_to_payment,payment_success
from django.conf import settings
from django.conf.urls.static import static
from .views.aichat_views import aichat_view

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),  # homepage URL pattern
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('forgot-password/', CustomPasswordResetView.as_view(), name='forgot_password'),
    path('products/', product_listing_view, name='product_listing'),
    path('verify-otp/', CustomLoginView.as_view(), name='verify_otp'),
    path('cart/', cart_view, name='cart_view'),
    path('update_cart/', update_cart, name='update_cart'),
    path('remove_from_cart/', remove_from_cart, name='remove_from_cart'),
    path('update_quantity/', update_quantity, name='update_quantity'),
    path('proceed_to_payment/', proceed_to_payment, name='proceed_to_payment'),
    path('payment_success/', payment_success, name='payment_success'),  # Define a success view and template for payment success
     path('aichat/', aichat_view, name='aichat'),
]

# Serve static files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
