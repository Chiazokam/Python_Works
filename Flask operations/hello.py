from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

#@app.route("/about")
def about():
    return render_template("about.html")
app.add_url_rule('/about', 'about', about)  #The add_url_rule() method

@app.route("/contact")
@app.route("/feedback")
def contact():
    return render_template("contact.html") #Serve the contact page for both /contact and /feedback requests

if __name__ == '__main__':
    app.run(debug = True)
