from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/data', methods=['POST'])
def data():
    # Example: Get data from a form
    user_input = request.form['input']
    return f"You entered: {user_input}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
