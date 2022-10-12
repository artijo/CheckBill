from flask import Flask,render_template,request,session,redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mykey'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/addpeople',methods=['GET', 'POST'])
def addpeople():

    render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)