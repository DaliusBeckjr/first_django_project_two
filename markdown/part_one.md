# Assignment

### Part one

Create a new project with a single app

/ - redirects to the "/blogs" route with a method called "root"

/blogs - display the string "placeholder to later display a list of all blogs" with a method named "index"

/blogs/new - display the string "placeholder to display a new form to create a new blog" with a method named "new"

/blogs/create - redirect to the "/" route with a method called "create"

/blogs/< number > - display the string "placeholder to display blog number: {number}" with a method named "show" (eg. localhost:8000/blogs/15 should display the message: 'placeholder to display blog number 15')

/blogs/< number >/edit - display the string "placeholder to edit blog {number}" with a method named "edit"
/blogs/< number >/delete - redirect to the "/blogs" route with a method called "destroy"