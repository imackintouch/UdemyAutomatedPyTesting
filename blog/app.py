MENU_PROMPT = 'Enter "c" to create a blog, "l" to list blogs, "r" to read one\
    "p" to create a post, or "q" to quit'

blogs = dict()  # blog_name : Blog object

def menu():
    # show the user all the available blogs
    # Let the user make a choice
    # Do something with that choice
    # Eventually exit

    print_blogs()

    selection = input(MENU_PROMPT)

def print_blogs():
    # Print the available blogs
    print("Blogs!")
    for key, blog in blogs.items(): # (blog_name, Blog), (blog_name, Blog)
        print('- {}'.format(blog))