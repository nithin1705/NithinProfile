from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/skills")
def skills():
    return render_template("skills.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/education")
def education():
    return render_template("education.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]

        print("New Contact Form Submission")
        print("Name:", name)
        print("Email:", email)
        print("Phone:", phone)
        print("Message:", message)

        return "Thank You! I will contact you soon."

    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)