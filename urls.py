from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('duttaEcommerceapp.urls')),  # Include URLs from the app
    
]

#from .testingfile import test_email  # Import your test email view
'''from django.urls import path
from .views import test_email  # Import your test email view

urlpatterns = [
    # Other URL patterns
    path('test-email/', test_email, name='test_email'),  # Test email URL pattern
]
#path('test-email/', test_email, name='test_email'),  # Test email URL pattern
'''