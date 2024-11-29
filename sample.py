from flask import Flask, render_template, request, jsonify
from product import saveProd, getProdId, getProduct, updateRate, delProduct


app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template('base.html')


@app.route('/add')
def padd():
    return render_template('newProd.html')


@app.route('/addc')
def cadd():
    return render_template('newClient.html')

@app.route('/aboutus')
def about():
    return "<h1> This is aboutus page<h1>"


@app.route('/info')
def info():
    return "<h2>This is the information Page</h2>"


@app.route('/welcome/<user>')
def loggedin(user):
    return f"Wecome {user}'s page...."


@app.route('/demorend')
def demo():
    x={"title":"Demo Page", "message":"This is the rendered page"}
    return render_template('demo.html',**x)

@app.route('/dlist')
def listeg():
    phones=[
        {"Brand":"Apple","Model":"iPhone15", "Storage":"128GB","Processor":"A18 BC"},
        {"Brand":"Samsung","Model":"S24", "Storage":"256GB","Processor":"Exynos"},
        {"Brand":"Redmi","Model":"Note 13Pro", "Storage":"256GB","Processor":"Dimensity"}
    ]
    return render_template('demolist.html',mobile=phones)


@app.route('/saveProd', methods=['POST'])
def savep():
    if request.method=='POST':
        form_data={
            'brand': request.form['brand'],
            'model': request.form['model'],
            'storage':request.form['storage'],
            'processor':request.form['processor'],
            'rate':request.form['rop']
        }
        result= saveProd(form_data)
        if result['status']=='success':
            return f"<h1>{ result['message'] } </h1> <a href='/add'>Go Back </a>"
        else:
            return f"<h1>{ result['message'] } </h1> <a href='/add'>Go Back </a>"
                
    return render_template('/savep')

    
@app.route('/eprod')
def eprod():   
    mid = getProdId()
    return render_template('editProd.html', ids= mid)

@app.route('/fetchProd', methods=['POST'])
def fprod():
    x = request.form.get('mid')
    data = getProduct(x)
    return data


@app.route('/urate', methods=['POST'])
def uprate():
    form_data={
        "id": request.form.get('mid'),
        "rate":request.form.get('rate')
    }
    data = updateRate(form_data)
    return jsonify({"status":"success", "message":"Record Updated"})
    pass


@app.route('/delmid', methods=['POST'])
def delmid():
    k = request.form.get('mid')
    data = delProduct(k)
    return jsonify({"status":"success", "message":"Record deleted"})



if __name__ == '__main__':
    app.run(debug=True)