from django.core.management import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()
        category_list = [
            {'name': 'игрушки', 'desc': 'машинки и т.д'},
            {'name':'молоко','desc':'коровья жидкость' },
            {'name':'хоз товары', 'desc':'гвозди мыло и т.д'}
        ]
        for category_item in category_list:
            Category.objects.create(**category_item)

        product_list = [
            {"name": "Сладости",
                    "desc": "сладости",
                    "image": None,
                    "category": "еда",
                    "price": 12,
                    "create_date": None,
                    "last_change": None
             },
            {'name':'Шрекс',
             'desc':'Напиток из ушей шрека',
             'image':None,
             'category': 'напиток',
             'price': 99,
             'create_date':None,
             'last_change':None
             },
            {'name': 'Фионикс',
             'desc': 'Напиток из ушей Фионы',
             'image': None,
             'category': 'напиток',
             'price': 98,
             'create_date': None,
             'last_change': None
             }
        ]
        for product_item in product_list:
            Product.objects.create(**product_item)

