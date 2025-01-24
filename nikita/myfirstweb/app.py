from flask import Flask , render_template
app = Flask(__name__)


@app.route("/")   # ip:port/
def home():
    # return "Hey welcome to you in flask application"
    return render_template('index.html')


@app.route("/about")  # ip:port_no/about
def about():
    # return "Hey you are at about page url" 
    return render_template('about.html')

# ip:port_no/contact
@app.route('/contact') 
def contact():
    return render_template('contact.html')

@app.route('/service')
def service():
    return render_template('service.html')


if __name__ == "__main__":
    app.run(debug=True)

    