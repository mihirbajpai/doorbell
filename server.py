from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/offer', methods=['POST'])
def offer():
    data = request.get_json()
    # Send the offer data to the Android app
    # In a real scenario, this would involve storing the offer data and sending it to the correct user
    return jsonify({'answer': 'Sample answer from server'})

if __name__ == '__main__':
    app.run(debug=True)
