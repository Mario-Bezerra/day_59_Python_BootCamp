from flask import Flask, render_template
import requests
from post import Post

response = requests.get("https://api.npoint.io/b79a1c660a11fd0e5254")
data_blog = response.json()

blog_objects = []
for blog in data_blog:
    b_object = Post(blog["id"], blog["title"], blog["subtitle"], blog["body"], blog["by"], blog["from"])
    blog_objects.append(b_object)

app = Flask(__name__)

@app.route('/')
def blog():
    return render_template("index.html", blog_objects=blog_objects)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in blog_objects:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", blog=requested_post)

if __name__ == "__main__":
    app.run(debug=True)
