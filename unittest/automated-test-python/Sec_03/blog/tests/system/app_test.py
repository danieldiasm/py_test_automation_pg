from unittest import TestCase
from unittest.mock import patch

from post import Post
from blog import Blog
import app


class AppTest(TestCase):

    def setUp(self) -> None:
        self.blog_title = 'Test Blog'
        self.test_blog = Blog(self.blog_title, 'Test Author')
        app.blogs = {'Test Blog': self.test_blog}
        self.test_post = Post('Test Post', 'Test Content')

    # Test printing functions

    def test_calls_print_menu_and_print_blog(self):
        with patch('app.print_blogs') as mocked_print_blogs:
            with patch('builtins.input', return_value='q') as mocked_input:
                app.menu()
                mocked_input.assert_called_with(app.MENU_PROMPT)
                mocked_print_blogs.assert_called_once()

    def test_print_blogs(self):
        with patch('builtins.print') as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with('- Test Blog by Test Author (0 posts)')

    def test_ask_read(self):
        with patch('builtins.input', return_value=self.blog_title) as mocked_input:
            with patch('app.print_posts') as mocked_print_posts:
                app.ask_read_blog()
                mocked_print_posts.assert_called_with(self.test_blog)

    def test_print_posts(self):
        self.test_blog.create_post('Test Post', 'Test Content')
        with patch('app.print_post') as mocked_print_post:
            app.print_posts(self.test_blog)
            mocked_print_post.assert_called()

    def test_print_post(self):
        with patch('builtins.print') as mocked_print:
            app.print_post(self.test_post)
            mocked_print.assert_called_with(app.POST_TEMPLATE.format('Test Post', 'Test Content'))

# Test creating functions

    def test_ask_create_blog(self):
        with patch('builtins.input') as mocked_input:
            with patch('builtins.print') as mocked_print:
                mocked_input.side_effect = ('Test Author', 'Test Blog')
                app.ask_create_blog()
                self.assertIsNotNone(app.blogs.get('Test Blog'))

    def test_ask_create_post(self):
        with patch('builtins.input') as mocked_input:
            with patch('builtins.print') as mocked_print:
                mocked_input.side_effect = (self.blog_title, 'Test Post', 'Test Content')
                app.ask_create_post()

                self.assertEqual(app.blogs[self.blog_title].posts[0].title, self.test_post.title)
                self.assertEqual(app.blogs[self.blog_title].posts[0].content, self.test_post.content)

# Menu functions tests

    def test_menu_create_blog(self):
        with patch('builtins.print') as mocked_print:
            with patch('builtins.input') as mocked_input:
                with patch('app.ask_create_blog') as mocked_selection:
                    mocked_input.side_effect = ('c', 'q')
                    app.menu()
                    mocked_selection.assert_called()

    def test_menu_list_blogs(self):
        with patch('builtins.print') as mocked_print:
            with patch('builtins.input') as mocked_input:
                with patch('app.print_blogs') as mocked_selection:
                    mocked_input.side_effect = ('l', 'q')
                    app.menu()
                    mocked_selection.assert_called()

    def test_menu_read_blog(self):
        with patch('builtins.print') as mocked_print:
            with patch('builtins.input') as mocked_input:
                with patch('app.ask_read_blog') as mocked_selection:
                    mocked_input.side_effect = ('r', 'q')
                    app.menu()
                    mocked_selection.assert_called()

    def test_menu_create_post(self):
        with patch('builtins.print') as mocked_print:
            with patch('builtins.input') as mocked_input:
                with patch('app.ask_create_post') as mocked_selection:
                    mocked_input.side_effect = ('p', 'q')
                    app.menu()
                    mocked_selection.assert_called()
