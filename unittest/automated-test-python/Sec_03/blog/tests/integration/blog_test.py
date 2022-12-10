from unittest import TestCase
from blog import Blog


class BlogTest(TestCase):

    def test_create_post_in_blog(self):
        b = Blog('Test', 'Test Author')
        b.create_post('post title', 'post content')

        self.assertEqual(1, len(b.posts))
        self.assertEqual('post title', b.posts[0].title)
        self.assertEqual('post content', b.posts[0].content)

    def test_json_no_posts(self):
        b1 = Blog('Test', 'Test Author')
        expected_b1 = {'Title': 'Test', 'Author': 'Test Author', 'Posts': []}

        self.assertEqual(expected_b1, b1.json())

    def test_json(self):
        b1 = Blog('Test', 'Test Author')
        b1.create_post('post title', 'post content')

        b2 = Blog('My Day', 'Rolf')
        b2.create_post('Monday Post', 'This is a post about monday')

        expected_b1 = {'Title': 'Test',
                       'Author': 'Test Author',
                       'Posts': [
                           {'title': 'post title',
                            'content': 'post content'}
                       ]}
        result_b1 = b1.json()

        expected_b2 = {'Title': 'My Day',
                       'Author': 'Rolf',
                       'Posts': [
                           {'title': 'Monday Post',
                            'content': 'This is a post about monday'}
                       ]}
        result_b2 = b2.json()

        self.assertDictEqual(expected_b1, result_b1)
        self.assertDictEqual(expected_b2, result_b2)
