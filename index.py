from flask import Flask,render_template,request,session,redirect


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mykey'

@app.route('/')
def index():

    session['forlist'] = False
    session['people'] = list()
    session['menu'] = list()
    session['foods'] = dict()
    session['result'] = dict()
    return render_template('index.html')

@app.route('/addpeople',methods=['GET', 'POST'])
def addpeople():
    session['forlist'] = True
    if request.method == 'POST':
        name = request.form['name']
        if name not in session['people']:
            session['people'].append(name)
        
    return render_template('index.html',name=name)

@app.route('/addfood',methods=['GET', 'POST'])
def addfood():
    session['forlist'] = True
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        peoples = request.form.getlist('people')
        session['menu'].append(name)
        session['foods'].update({name:{"people":peoples,"price":price}})

    # session['menu'] = menu
    for i in session['foods'] :
        for x in session['menu'] :
            if i == x :
                countitem = len(session['foods'][i]['people'])  #จำนวนคนในการเลือกอาหารนั้น
                hhh = int(session['foods'][x]['price']) / countitem  # ราคาหารจำนวนอาหาร
                hhh = round(hhh,2)
    for y in session['people']:
        if y in session['foods'][i]['people']:
            try:
                dt = session['result'][y]
                print('...',dt)
                dt = dt+hhh
                session['result'].update({y:dt})
            except KeyError:
                session['result'].update({y:hhh})


    # print(menu)
    # print(countitem)
    # print(hhh)

    for i in session['result']:
        print(i,'\t\t\t',session['result'][i])
    # print(people)
    return render_template('index.html')

@app.route('/clare')
def clare():
    session['people'] = session['result'] = session['foods'] = session['menu'] = None
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)