
from flask import Flask, Blueprint, render_template, url_for, redirect



views = Blueprint(__name__, "views")

app = Flask(__name__)
app.register_blueprint(views, url_prefix = "/")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/page1")
def page_1():
    return render_template("page_1.html")

@app.route("/page2")
def page_2():
    return render_template("page_2.html")

@app.route("/page3")
def page_3():
    return render_template("page_3.html")

@app.route("/admin")
def admin_page():
    return render_template("admin.html")


@app.route("/javascript")
def javascript_redirect():
    return redirect(url_for("home"))

@app.route("/js")
def js_redirect():
    return redirect(url_for("home"))

@app.route("/home")
def home_redirect():
    return redirect(url_for("home"))



@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"),404



if __name__ == "__main__":
    app.run(debug=True, port=8000)

########################################