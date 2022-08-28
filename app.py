from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])  # for calling the HTML Page
def home_page():
    """
    Run http://127.0.0.1:5000/ from browser
    :return:
    """
    return render_template('index.html')


@app.route('/via_postman', methods=['POST'])  # for calling the API from Postman/SOAPUI
def math_operation_via_postman():
    """
    1. Open Postman APK -> POST & http://127.0.0.1:5000/via_postman
    2. Select Body -> raw -> JSON
    3. {"operation":"divide", "num1": 10, "num2": 20}
    :return: Postman Output
    """
    if request.method == 'POST':
        operation = request.json['operation']
        num1 = int(request.json['num1'])
        num2 = int(request.json['num2'])
        if operation == 'add':
            r = num1+num2
            result = 'the sum of '+str(num1)+' and '+str(num2) + ' is '+str(r)
        if operation == 'subtract':
            r = num1 - num2
            result = 'the difference of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if operation == 'multiply':
            r = num1 * num2
            result = 'the product of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if operation == 'divide':
            r = num1 / num2
            result = 'the quotient when ' + str(num1) + ' is divided by ' + str(num2) + ' is ' + str(r)
        return jsonify(result)


@app.route('/pow', methods=['GET'])          # this will be called from the browser
def power():
    """
    Run http://127.0.0.1:5000/pow?num=5&pow=5 from browser
    :return: HTML Page
    """
    num = int(request.args.get('num'))
    pow = int(request.args.get('pow'))
    return f"<h1>Power of {num}<sup>{pow}</sup> is {num**pow}</h1>"


@app.route('/math', methods=['POST'])  # this will be called from the HTML
def math_operation_via_browser():
    """
    1. Open Postman APK -> POST & http://127.0.0.1:5000/via_postman
    2. Select Body -> raw -> JSON
    3. {"operation":"divide", "num1": 10, "num2": 20}
    :return: Postman Output
    """
    if request.method == 'POST':
        operation = request.form['operation']
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        if operation == 'add':
            r = num1+num2
            result = 'the sum of '+str(num1)+' and '+str(num2) + ' is '+str(r)
        if operation == 'subtract':
            r = num1 - num2
            result = 'the difference of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if operation == 'multiply':
            r = num1 * num2
            result = 'the product of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if operation == 'divide':
            r = num1 / num2
            result = 'the quotient when ' + str(num1) + ' is divided by ' + str(num2) + ' is ' + str(r)
        return render_template('results.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
