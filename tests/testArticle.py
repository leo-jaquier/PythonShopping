import unittest
from shopping.article import Article


class TestArticle(unittest.TestCase):

    _article = None
    _id = 0
    _description = ""
    _price = 0.0

    def setUp(self):
        # Private attributes
        self._id = 1
        self._description = "product description"
        self._price = 20.45
        self._article = Article(self._id, self._description, self._price)

    def test_all_properties_after_instantiation_success(self):
        # given
        # then
        self.assertEqual(self._id, self._article.id)
        self.assertEqual(self._description, self._article.description)
        self.assertEqual(self._price, self._article.price)

    def test_description_short_description_return_new_value(self):
        # given

        self.expected_description = "After Shave"
        # when
        self._article.description = self.expected_description
        # then
        self.assertEqual(self._article.description, self.expected_description)


if __name__ == '__main__':
    unittest.main()
