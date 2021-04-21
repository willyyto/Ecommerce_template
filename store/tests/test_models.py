from django.contrib.auth.models import User
from django.test import TestCase

from store.models import Category, Product


class TestCategoriesModel(TestCase):

    def setUp(self):
        self.data1 = Category.objects.create(name="django", slug="django")

    def test_category_model_entry(self):
        """
        Test Catagory model data insertion/types/field attributes
        """

        data = self.data1
        self.assertTrue(isinstance(data, Category))
        self.assertEqual(str(data), 'django')

class TestProductModel(TestCase):

    def setUp(self):
        Category.objects.create(name="django", slug="django")
        User.objects.create(username="admin")
        self.data1 = Product.objects.create(category_id=1, title='django test', created_by_id=1,
                                             slug='django-test', price='20.00')

    def test_product_model_entry(self):
        """
        Test product model data insertion/types/field attributes
        """

        data = self.data1
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), 'django test')