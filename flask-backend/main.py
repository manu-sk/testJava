from flask import Flask,render_template,request

import loaddata
app = Flask("__main__")
@app.route('/')
def hello_world():
    #namedata = loaddata.retriveDistinctNames()
    return render_template('index.html', data = "manu")

if __name__ == '__main__':

    app.run(debug=True)