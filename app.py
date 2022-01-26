from flask import Flask,render_template

app = Flask(__name__)

# creating the route function and render html  files that
@app.route('/')
def home():

       return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
