from django.test import TestCase # Wrapper for Python uniittest

from store.models import Category, Product

class TestCategoriesModel(TestCase):

    def setup(self):
        self.data1 = Category.objects.create(name='django', slug='django')


    def test_category_model_entry(self):
        """
        Test Category model data insertion/types/field attributes
        """

        data = self.data1
        self.assertTrue(isinstance(data, Category))

