from flask import Flask,render_template,request,session,redirect


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mykey'

people = list()
foods = dict()

@app.route('/')
def index():
    session['people'] = False
    return render_template('index.html')

@app.route('/addpeople',methods=['GET', 'POST'])
def addpeople():
    if request.method == 'POST':
        name = request.form['name']
        people.append(name)

        # print(people)
        session['people'] = people
        
    return render_template('index.html',name=name)

@app.route('/addfood',methods=['GET', 'POST'])
def addfood():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        people = request.form.getlist('people')
        foods.update({name:{"people":people,"price":price}})

    print(foods)
    # print(people)
        
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)