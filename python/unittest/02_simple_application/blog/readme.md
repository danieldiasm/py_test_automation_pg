# Blog Application

The Blog Application is a simple application of a Blog that runs on Terminal.

### Application Structure:

- app.py

  - Imports
  - Constants (IN CAPS)
  - Vars
  - Functions
    - Menu: Prints available blogs and collects user input.
    - Print Blogs: Print Availble Blogs in memory (dict blogs).
    - Print Posts: Print available posts of a selected blog.
    - Print Post: Print a selected post in detail.
    - Ask Create Blog: Creates a new blog in memory.
    - Ask Read Blog: Captures user input to read an existent blog.
    - Ask Create Post: Will make a set of questions to create a post on Selected Blog
    - if name == main: This starts the main loop if app.py is the file executed first by the user.

- blog.py

  - Imports
  - Class Blog
    - Init having basic infos.
  - Representation Method (repr).
  - Create Post: Creates a post on the instance of the blog.
  - json: returns to user a blog data on json format.

- post.py
  - Class Post
    - Init: initialize the object with few necessary data
    - JSON: returns a json format of a instance of the object
