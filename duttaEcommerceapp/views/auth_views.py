
#New with otp_verify.html addition
#'''
from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth import authenticate, login
import random
import string
import smtplib
import ssl
import logging
import http.client as http_client
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from duttaEcommerceapp.forms.signupform import SignUpForm
from duttaEcommerceapp.forms.loginform import LoginForm, OTPForm
from duttaEcommerceapp.forms.forms import ForgotPasswordForm
from duttaEcommerceapp.models.models import User
from django.conf import settings
from django.contrib.auth.decorators import login_required
from duttaEcommerceapp.models.product import Product, SubCategory, Category

logger = logging.getLogger(__name__)

class SignUpView(View):
    def get(self, request):
        form = SignUpForm()
        return render(request, 'signup.html', {'form': form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            print(f"User {user.email} created successfully!")  # Debug statement
            login(request, user)
            return redirect('login')  # Redirect to login page
        print("Form is not valid. Errors: ", form.errors)  # Debug statement
        return render(request, 'signup.html', {'form': form})

def generate_otp():
    characters = string.ascii_letters + string.digits
    otp = ''.join(random.choice(characters) for _ in range(6))
    return otp

# Enable HTTP connection debug logging with error handling
try:
    http_client.HTTPConnection.debuglevel = 1
    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)
    requests_log = logging.getLogger("requests.packages.urllib3")
    requests_log.setLevel(logging.DEBUG)
    requests_log.propagate = True
    print("HTTP connection debug logging enabled successfully.")
except Exception as e:
    print(f"Failed to enable HTTP connection debug logging: {e}")

def send_otp(email, otp):
    try:
        subject = 'Your OTP Code'
        message = f'Your OTP code is: {otp}'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [email]

        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))
        print("Creating SSL context")
        context = ssl.create_default_context()
        print("SSL context created successfully")
        print(f"Connecting to SMTP server: {settings.EMAIL_HOST} on port {settings.EMAIL_PORT}")
        with smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT) as server:
            server.set_debuglevel(1)  # Enable SMTP debug output
            print(f"Connecting to SMTP server: {settings.EMAIL_HOST} on port {settings.EMAIL_PORT}")
            server.starttls(context=context)
            print("Starting TLS session")
            server.login(from_email, settings.EMAIL_HOST_PASSWORD)
            print(f"Logged into SMTP server as {from_email}")
            print(f"Attempting to send OTP to {email}")
            server.sendmail(from_email, recipient_list, msg.as_string())

        print(f"OTP sent to {email}: {otp}")
    except User.DoesNotExist:
        print(f"User with email {email} does not exist.")
    except smtplib.SMTPException as e:
        print(f"Failed to send OTP due to SMTP error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
'''
class CustomLoginView(View):
    def get(self, request):
        try:
            form = LoginForm()
            return render(request, 'login.html', {'form': form, 'otp_sent': False})
        except Exception as e:
            logging.error(f"An error occurred in GET request: {e}")
            return render(request, 'login.html', {'form': None, 'error': str(e)})

    def post(self, request):
        try:
            form = LoginForm(request.POST)
            otp_form = OTPForm(request.POST)

            if 'send_otp' in request.POST and form.is_valid():
                email = form.cleaned_data['email']

                if User.objects.filter(email=email).exists():
                    otp = generate_otp()
                    send_otp(email, otp)
                    request.session['email'] = email
                    request.session['otp'] = otp
                    #return render(request, 'otp_verify.html', {'otp_form': otp_form, 'otp_message': 'OTP has been sent to your email address.'})
                    return render(request, 'login.html', {'form':form,'otp_form': otp_form, 'otp_sent': True, 'otp_message': 'OTP has been sent to your email address.'})

                else:
                    form.add_error(None, 'Invalid email address')
                    return render(request, 'login.html', {'form': form, 'otp_form': otp_form,'otp_sent':False})

            if 'verify_otp' in request.POST and otp_form.is_valid():
                otp = otp_form.cleaned_data['otp']
                email = request.session.get('email')

                try:
                    if otp == request.session.get('otp'):
                        user = User.objects.get(email=email)
                        login(request, user)
                        return redirect('product_listing')  # Redirect to the product listing page
                    else:
                        otp_form.add_error('otp', 'Invalid OTP')
                except User.DoesNotExist:
                    otp_form.add_error('otp', 'Invalid OTP')
                except Exception as e:
                    logging.error(f"An error occurred during OTP validation: {e}")

            return render(request, 'otp_verify.html', {'otp_form': otp_form})
        except Exception as e:
            logging.error(f"An error occurred in POST request: {e}")
            return render(request, 'login.html', {'form': None,'otp_form':otp_form ,'error': str(e)})
'''
#
class CustomLoginView(View):
    def get(self, request):
        try:
            form = LoginForm()
            otp_form = OTPForm()
            return render(request, 'login.html', {'form': form, 'otp_form': otp_form, 'otp_sent': False, 'otp_message': None})
        except Exception as e:
            logging.error(f"An error occurred in GET request: {e}")
            return render(request, 'login.html', {'form': None, 'otp_form': None, 'otp_message': None, 'error': str(e)})

    def post(self, request):
        try:
            form = LoginForm(request.POST)
            otp_form = OTPForm(request.POST)

            if 'send_otp' in request.POST and form.is_valid():
                email = form.cleaned_data['email']

                if User.objects.filter(email=email).exists():
                    otp = generate_otp()
                    send_otp(email, otp)
                    request.session['email'] = email
                    request.session['otp'] = otp
                    return render(request, 'login.html', {
                        'form': form,
                        'otp_form': otp_form,
                        'otp_sent': True,
                        'otp_message': 'OTP has been sent to your email address.'
                    })
                else:
                    form.add_error(None, 'Invalid email address')
                    return render(request, 'login.html', {'form': form, 'otp_form': otp_form, 'otp_sent': False, 'otp_message': None})

            if 'verify_otp' in request.POST and otp_form.is_valid():
                otp = otp_form.cleaned_data['otp']
                email = request.session.get('email')

                try:
                    if otp == request.session.get('otp'):
                        user = User.objects.get(email=email)
                        login(request, user)
                        return redirect('product_listing')
                    else:
                        otp_form.add_error('otp', 'Invalid OTP')
                except User.DoesNotExist:
                    otp_form.add_error('otp', 'Invalid OTP')
                except Exception as e:
                    logging.error(f"An error occurred during OTP validation: {e}")

            return render(request, 'login.html', {
                'form': form,
                'otp_form': otp_form,
                'otp_sent': True,
                'otp_message': 'Invalid OTP'
            })
        except Exception as e:
            logging.error(f"An error occurred in POST request: {e}")
            return render(request, 'login.html', {'form': None, 'otp_form': otp_form, 'otp_message': None, 'error': str(e)})

class CustomPasswordResetView(PasswordResetView):
    form_class = ForgotPasswordForm
    template_name = 'forgot_password.html'
    success_url = reverse_lazy('password_reset_done')


'''import logging'''
@login_required
def product_listing_view(request):
    categories = Category.objects.prefetch_related('subcategories')
    products = Product.objects.all()
    logger.debug(f"Categories: {categories}")
    logger.debug(f"Products: {products}")
    return render(request, 'productlisting.html', {
        'categories': categories,
        'products': products
    })
#'''