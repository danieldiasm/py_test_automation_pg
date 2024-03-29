from blog import Blog

MENU_PROMPT = 'Enter "c" to create a blog, "l" to list blogs, "r" to read one, "p" to create a post, or "q" to quit\n'
POST_TEMPLATE = '''
    ---{}---
    
    {}
    
    '''

# Blogs are stored in RAM during runtime only.
blogs = dict()


def menu():
    print_blogs()
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection == 'c':
            ask_create_blog()
        elif selection == 'l':
            print_blogs()
        elif selection == 'r':
            ask_read_blog()
        elif selection == 'p':
            ask_create_post()
        selection = input(MENU_PROMPT)


def print_blogs():
    for key, blog in blogs.items():
        print('- {}'.format(blog))


def print_posts(blog):
    for post in blog.posts:
        print_post(post)


def print_post(post):
    print(POST_TEMPLATE.format(post.title, post.content))


def ask_create_blog():
    new_user_name = input('Insert your name: ')
    new_blog_title = input('Insert the blog title: ')
    blogs[new_blog_title] = Blog(new_blog_title, new_user_name)
    print('Blog Created!')


def ask_read_blog():
    blog_title = input('Insert the title of a blog to read: ')
    print_posts(blogs[blog_title])


def ask_create_post():
    blog_title = input('Insert the blog title to insert the post: ')
    new_post_title = input('Insert the post title: ')
    new_post_content = input('Insert content:')
    blogs[blog_title].create_post(new_post_title, new_post_content)
    print('Post Created!')


if __name__ == '__main__':
    menu()
