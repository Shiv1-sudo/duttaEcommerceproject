from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail  # Make sure to import send_mail
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
#import logging
#import smtplib
#import ssl
#from email.mime.text import MIMEText
#from email.mime.multipart import MIMEMultipart
 # Ensure you import the User model

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

'''# Enable HTTP connection debug logging with error handling
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
'''
#testing
def send_otp(email, otp):
    try:
        # Retrieve the user by email
        user = User.objects.get(email=email)
        user.otp = otp
        user.save()

        # Email content
        subject = "Your OTP Code"
        body = f"Your OTP code is: {otp}"
        sender_email = settings.EMAIL_HOST_USER
        receiver_email = 'duttashivani06@gmail.com'#email  # Send the OTP to the user's email
        password = settings.EMAIL_HOST_PASSWORD

        # Create the email message
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = receiver_email
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        # Connect to the SMTP server using TLS
        context = ssl.create_default_context()
        with smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT) as server:
            server.set_debuglevel(1)  # Enable SMTP debug output
            print(f"Connecting to SMTP server: {settings.EMAIL_HOST} on port {settings.EMAIL_PORT}")
            server.starttls(context=context)
            print(f"Starting TLS session")
            server.login(sender_email, password)
            print(f"Logged into SMTP server as {sender_email}")
            print(f"Attempting to send OTP to {receiver_email}")
            server.sendmail(sender_email, receiver_email, msg.as_string())

        print(f"OTP sent to {receiver_email}: {otp}")

    except User.DoesNotExist:
        print(f"User with email {'duttashivani06@gmail.com'} does not exist.")
        # Handle user not found error (e.g., log the error, return a response, etc.)

    except smtplib.SMTPException as e:
        print(f"Failed to send OTP due to SMTP error: {e}")
        # Handle SMTP exceptions

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        # Handle any other exceptions

################
'''def send_otp(email, otp):
    try:
        # Retrieve the user by email
        user = User.objects.get(email=email)
        user.otp = otp
        user.save()

        # Email content
        subject = "Your OTP Code"
        body = f"Your OTP code is: {otp}"
        sender_email = "duttashivani06@gmail.com"
        receiver_email = email  # Send the OTP to the user's email
        password = "zduf soha vify xfxy"

        # Create the email message
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = receiver_email
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        # Connect to the SMTP server using TLS
        context = ssl.create_default_context()
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls(context=context)
            server.login(sender_email, password)
            # Log the receiver email 
            print(f"Attempting to send OTP to {receiver_email}")
            server.sendmail(sender_email, receiver_email, msg.as_string())

        print(f"OTP sent to {receiver_email}: {otp}")

    except User.DoesNotExist:
        print(f"User with email {email} does not exist.")
        # Handle user not found error (e.g., log the error, return a response, etc.)

    except smtplib.SMTPException as e:
        print(f"Failed to send OTP due to SMTP error: {e}")
        # Handle SMTP exceptions

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        # Handle any other exceptions
'''
'''
def send_otp(email, otp):
    try:
        # Retrieve the user by email
        user = User.objects.get(email=email)
        user.otp = otp
        user.save()

        # Email content
        subject = "Your OTP Code"
        body = f"Your OTP code is: {otp}"
        sender_email = "duttashivani06@gmail.com"
        receiver_email = "duttashivani06@gmail.com"#email  # Send the OTP to the user's email
        password = "zduf soha vify xfxy"

        # Create the email message
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = receiver_email
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        # Connect to the SMTP server using TLS
        context = ssl.create_default_context()
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.set_debuglevel(1)  # Enable SMTP debug output
            print(f"Connecting to SMTP server: smtp.gmail.com on port 587")
            server.starttls(context=context)
            print(f"Starting TLS session")
            server.login(sender_email, password)
            print(f"Logged into SMTP server as {sender_email}")
            print(f"Attempting to send OTP to {receiver_email}")
            server.sendmail(sender_email, receiver_email, msg.as_string())

        print(f"OTP sent to {receiver_email}: {otp}")

    except User.DoesNotExist:
        print(f"User with email {email} does not exist.")
        # Handle user not found error (e.g., log the error, return a response, etc.)

    except smtplib.SMTPException as e:
        print(f"Failed to send OTP due to SMTP error: {e}")
        # Handle SMTP exceptions

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        # Handle any other exceptions
'''
class CustomLoginView(View):
    def get(self, request):
        try:
            form = LoginForm()
            return render(request, 'login.html', {'form': form})
        except Exception as e:
            print(f"An error occurred in GET request: {e}")
            # Handle error (e.g., log the error, return an error response, etc.)

    def post(self, request):
        try:
            form = LoginForm(request.POST)
            otp_form = OTPForm(request.POST)
            
            if 'send_otp' in request.POST and form.is_valid():
                email = form.cleaned_data['email']

                if User.objects.filter(email=email).exists():
                    otp = self.generate_otp()
                    self.send_otp(email, otp)
                    # Save the OTP to the user or session for verification later
                    request.session['email'] = email
                    request.session['otp'] = otp
                    return render(request, 'login.html', {'form': form, 'otp_form': otp_form, 'otp_sent': True, 'otp_message': 'OTP has been sent to your email address.'})
                else:
                    form.add_error(None, 'Invalid email address')

            if 'login' in request.POST and otp_form.is_valid():
                otp = otp_form.cleaned_data['otp']
                email = request.session.get('email')

                try:
                    # Validate the OTP
                    if otp == request.session.get('otp'):
                        user = User.objects.get(email=email)
                        login(request, user)
                        return redirect('home')
                    else:
                        otp_form.add_error('otp', 'Invalid OTP')
                except User.DoesNotExist:
                    otp_form.add_error('otp', 'Invalid OTP')
                except Exception as e:
                    print(f"An error occurred during OTP validation: {e}")
                    # Handle other exceptions (e.g., log the error, return an error response, etc.)

            return render(request, 'login.html', {'form': form, 'otp_form': otp_form})
        except Exception as e:
            print(f"An error occurred in POST request: {e}")
            # Handle error (e.g., log the error, return an error response, etc.)

    def generate_otp(self):
        try:
            return ''.join(random.choices(string.digits, k=6))
        except Exception as e:
            print(f"An error occurred while generating OTP: {e}")
            # Handle error (e.g., log the error, return an error response, etc.)

    def send_otp(self, email, otp):
        try:
            subject = 'Your OTP Code'
            message = f'Your OTP code is: {otp}'
            from_email = 'duttashivani06@gmail.com'
            recipient_list = [email]  # Send to the user's email

            send_mail(subject, message, from_email, recipient_list)
            print(f"OTP sent to {email}: {otp}")
        except Exception as e:
            print(f"Failed to send OTP: {e}")
            # Handle error (e.g., log the error, return an error response, etc.)

class CustomPasswordResetView(PasswordResetView):
    form_class = ForgotPasswordForm
    template_name = 'forgot_password.html'
    success_url = reverse_lazy('password_reset_done')



