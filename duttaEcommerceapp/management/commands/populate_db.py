'''
from django.core.management.base import BaseCommand
from duttaEcommerceapp.models.product import Category, SubCategory, Product

class Command(BaseCommand):
    help = 'Populates the database with sample data'

    def handle(self, *args, **kwargs):
        # Create categories
        books = Category.objects.create(name='Clothes')
        games = Category.objects.create(name='Games')
        electronics = Category.objects.create(name='Electronics')

        # Create subcategories
        clothes_0_10 = SubCategory.objects.create(category=clothes, name='Kids', age_group='0-10')
        clothes_11_18 = SubCategory.objects.create(category=clothes, name='Teens', age_group='11-18')
        clothes_19_upper = SubCategory.objects.create(category=clothes, name='Adults', age_group='19-Upper Age')

        games_0_10 = SubCategory.objects.create(category=games, name='Kids', age_group='0-10')
        games_11_18 = SubCategory.objects.create(category=games, name='Teens', age_group='11-18')
        games_19_upper = SubCategory.objects.create(category=games, name='Adults', age_group='19-Upper Age')

        electronics_0_10 = SubCategory.objects.create(category=electronics, name='Kids', age_group='0-10')
        electronics_11_18 = SubCategory.objects.create(category=electronics, name='Teens', age_group='11-18')
        electronics_19_upper = SubCategory.objects.create(category=electronics, name='Adults', age_group='19-Upper Age')

        # Create products
        Product.objects.create(name='Kids T-Shirt', description='A cool t-shirt for kids.', price=19.99, subcategory=clothes_0_10)
        Product.objects.create(name='Teen Hoodie', description='A stylish hoodie for teens.', price=29.99, subcategory=clothes_11_18)
        Product.objects.create(name='Adult Jacket', description='A warm jacket for adults.', price=49.99, subcategory=clothes_19_upper)

        Product.objects.create(name='Kids Puzzle', description='A fun puzzle for kids.', price=9.99, subcategory=games_0_10)
        Product.objects.create(name='Teen Board Game', description='An exciting board game for teens.', price=19.99, subcategory=games_11_18)
        Product.objects.create(name='Adult Chess Set', description='A classic chess set for adults.', price=29.99, subcategory=games_19_upper)

        Product.objects.create(name='Kids Tablet', description='A tablet designed for kids.', price=99.99, subcategory=electronics_0_10)
        Product.objects.create(name='Teen Laptop', description='A high-performance laptop for teens.', price=499.99, subcategory=electronics_11_18)
        Product.objects.create(name='Adult Smartphone', description='A modern smartphone for adults.', price=699.99, subcategory=electronics_19_upper)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with sample data.'))
'''
from django.core.management.base import BaseCommand
from duttaEcommerceapp.models.product import Category, SubCategory, Product

class Command(BaseCommand):
    help = 'Populates the database with sample data'

    def handle(self, *args, **kwargs):
        # Create categories
        books = Category.objects.create(name='Books')
        gifts = Category.objects.create(name='Gifts')
        medicines = Category.objects.create(name='Medicines')

        # Create subcategories
        books_kids = SubCategory.objects.create(category=books, name='Kids', age_group='0-10')
        books_teen = SubCategory.objects.create(category=books, name='Teens', age_group='11-18')
        books_adult = SubCategory.objects.create(category=books, name='Adults', age_group='19-Upper Age')

        gifts_kids = SubCategory.objects.create(category=gifts, name='Kids', age_group='0-10')
        gifts_teen = SubCategory.objects.create(category=gifts, name='Teens', age_group='11-18')
        gifts_adult = SubCategory.objects.create(category=gifts, name='Adults', age_group='19-Upper Age')

        medicines_kids = SubCategory.objects.create(category=medicines, name='Kids', age_group='0-10')
        medicines_teen = SubCategory.objects.create(category=medicines, name='Teens', age_group='11-18')
        medicines_adult = SubCategory.objects.create(category=medicines, name='Adults', age_group='19-Upper Age')

        # Create products for Books
        Product.objects.create(name='Kids Story Book', description='An enchanting story book for kids.', price=10.99, subcategory=books_kids)
        Product.objects.create(name='Teen Novel', description='A thrilling novel for teens.', price=14.99, subcategory=books_teen)
        Product.objects.create(name='Adult Fiction', description='An engaging fiction book for adults.', price=18.99, subcategory=books_adult)

        # Create products for Gifts
        Product.objects.create(name='Kids Toy Set', description='A fun toy set for kids.', price=29.99, subcategory=gifts_kids)
        Product.objects.create(name='Teen Gadget', description='A cool gadget for teens.', price=49.99, subcategory=gifts_teen)
        Product.objects.create(name='Adult Gift Basket', description='A luxurious gift basket for adults.', price=69.99, subcategory=gifts_adult)

        # Create products for Medicines
        Product.objects.create(name='Kids Vitamins', description='Essential vitamins for kids.', price=9.99, subcategory=medicines_kids)
        Product.objects.create(name='Teen Energy Boost', description='An energy boost supplement for teens.', price=19.99, subcategory=medicines_teen)
        Product.objects.create(name='Adult Health Supplement', description='A health supplement for adults.', price=29.99, subcategory=medicines_adult)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with sample data.'))
