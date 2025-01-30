#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import webbrowser
import threading
import django
from django.core.management import execute_from_command_line
from django.db import connection

def check_virtualenv():
    """Check if the virtual environment is active."""
    return os.environ.get('VIRTUAL_ENV') is not None


def open_browser():
    """Open the default web browser."""
    threading.Timer(2, lambda: webbrowser.open_new('http://127.0.0.1:8000')).start()

def migration_exists(migration_name, app_name):
    """Check if a specific migration already exists."""
    with connection.cursor() as cursor:
        cursor.execute("SELECT name FROM django_migrations WHERE app = %s AND name = %s", [app_name, migration_name])
        return cursor.fetchone() is not None
    

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'duttaEcommerceproject.settings')
    
    if not check_virtualenv():
        print("Virtual environment is not activated. Please activate it and try again.")
        sys.exit(1)

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # Automatically check for 'runserver' and open the browser
    if len(sys.argv) == 1 or 'runserver' in sys.argv:
        if 'runserver' not in sys.argv:
            sys.argv.append('runserver')
        threading.Timer(1.25, open_browser).start()
        
        # Perform migrations automatically with detailed logging
        try:
            django.setup()
            from django.core.management import call_command
            migration_name = '0001_initial'  # Change to your migration name
            app_name = 'duttaEcommerceapp'   # Change to your app name
            
            if not migration_exists(migration_name, app_name):
                print("Starting makemigrations...")
                call_command('makemigrations')
                print("Makemigrations completed.")
            
            print("Starting migrate...")
            call_command('migrate')
            print("Migrate completed.")
        except Exception as e:
            print(f"An error occurred during migrations: {e}")
            sys.exit(1)
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()

'''
#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import webbrowser
import threading
import django
from django.core.management import execute_from_command_line
from django.db import connection

def check_virtualenv():
    """Check if the virtual environment is active."""
    return os.environ.get('VIRTUAL_ENV') is not None

def open_browser():
    """Open the default web browser."""
    threading.Timer(2, lambda: webbrowser.open_new('http://127.0.0.1:8000')).start()

def migration_exists(migration_name, app_name):
    """Check if a specific migration already exists."""
    with connection.cursor() as cursor:
        cursor.execute("SELECT name FROM django_migrations WHERE app = %s AND name = %s", [app_name, migration_name])
        return cursor.fetchone() is not None

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'duttaEcommerceproject.settings')
    
    if not check_virtualenv():
        print("Virtual environment is not activated. Please activate it and try again.")
        sys.exit(1)

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # Automatically check for 'runserver' and open the browser
    if len(sys.argv) == 1 or 'runserver' in sys.argv:
        if 'runserver' not in sys.argv:
            sys.argv.append('runserver')
        threading.Timer(1.25, open_browser).start()
        
        # Perform migrations automatically with detailed logging
        try:
            django.setup()
            from django.core.management import call_command
            migration_name = '0001_initial'  # Change to your migration name
            app_name = 'duttaEcommerceapp'   # Change to your app name
            
            if not migration_exists(migration_name, app_name):
                print("Starting makemigrations...")
                call_command('makemigrations')
                print("Makemigrations completed.")
            
            print("Starting migrate...")
            call_command('migrate')
            print("Migrate completed.")
        except Exception as e:
            print(f"An error occurred during migrations: {e}")
            sys.exit(1)

    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
'''
