from django.core.management.base import BaseCommand
from duttaEcommerceapp.models.techservicesmodel import TechService

class Command(BaseCommand):
    help = 'Populate the database with tech services data'

    def handle(self, *args, **kwargs):
        services_data = [
            ("freeCodeCamp", "An open-source community that helps people learn to code by building projects for nonprofits.", "Free", "https://www.freecodecamp.org", "Free"),
            ("GitHub", "A development platform used for source code management and collaboration.", "Free", "https://github.com", "Free"),
            ("Stack Overflow", "A platform where developers and technology professionals ask and answer coding-related questions.", "Free", "https://stackoverflow.com", "Free"),
            ("HackerRank", "A platform for coding challenges and competitions.", "Free", "https://www.hackerrank.com", "Free"),
            ("DEV Community", "A platform for developers to share and discuss tech articles, tutorials, and experiences.", "Free", "https://dev.to", "Free"),
            ("LinkedIn Learning Subscription", "Access to thousands of professional courses and tutorials across various fields.", "$29.99 per month", "https://www.linkedin.com/learning", "Paid"),
            ("Coursera Specializations", "Online specializations and courses from top universities and companies to help you develop new skills.", "Varies by course (typically between $39 to $79 per month)", "https://www.coursera.org/specializations", "Paid"),
            ("JobScan Resume Optimization", "Optimize your resume for Applicant Tracking Systems (ATS) to improve your chances of getting noticed by employers.", "$49.95 per month", "https://www.jobscan.co", "Paid"),
            ("Raspberry Pi 4 Model B", "A small and affordable computer that you can use to learn programming and build projects.", "$55.00", "https://www.raspberrypi.org/products/raspberry-pi-4-model-b", "Paid"),
            ("Python Programming Course on Udemy", "A comprehensive online course to learn Python programming from scratch.", "$49.99", "https://www.udemy.com/course/pythonforbeginners", "Paid")
        ]

        for name, description, price, link, type in services_data:
            TechService.objects.create(name=name, description=description, price=price, link=link, type=type)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with tech services data'))
