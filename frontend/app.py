from flask import Flask, request, jsonify


app = Flask(__name__)

@app.route('/highlight', methods=['POST'])
def highlight():
    data = request.get_json()
    highlighted = data.get('word', '')
    print(f"Highlighted word: {highlighted}")
    if highlighted:
        return jsonify(message="Hello")
    

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
