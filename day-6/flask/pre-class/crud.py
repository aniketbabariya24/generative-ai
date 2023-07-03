from flask import Flask, request, jsonify

app = Flask(__name__)
data = {}

@app.route('/')
def hello_world():
    return f'Hello, World!'

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        key = request.form['key']
        value = request.form['value']
        data[key] = value
        return 'Entry created successfully'

    return '''
        <form method="POST">
            <label for="key">Key:</label>
            <input type="text" name="key" id="key" required><br><br>
            <label for="value">Value:</label>
            <input type="text" name="value" id="value" required><br><br>
            <input type="submit" value="Create">
        </form>
    '''

@app.route('/read', methods=['GET'])
def read():
    return jsonify(data)

@app.route('/update', methods=['GET','POST'])
def update():
    if request.method == 'POST':
        key = request.form['key']
        if key in data:
            value = request.form['value']
            data[key] = value
            return 'Entry updated successfully'
        else:
            return 'Key not found'

    return '''
        <form method="POST">
            <label for="key">Key:</label>
            <input type="text" name="key" id="key" required><br><br>
            <label for="value">Value:</label>
            <input type="text" name="value" id="value" required><br><br>
            <input type="submit" value="Update">
        </form>
    '''

@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method == 'POST':
        key = request.form['key']
        if key in data:
            del data[key]
            return 'Entry deleted successfully'
        else:
            return 'Key not found'

    return '''
        <form method="POST">
            <label for="key">Key:</label>
            <input type="text" name="key" id="key" required><br><br>
            <input type="submit" value="Delete">
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)
