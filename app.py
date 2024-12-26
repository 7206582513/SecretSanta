from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

def secret_santa_picker(names):
    participants = names[:]
    random.shuffle(participants)

    for i, name in enumerate(names):
        if participants[i] == name:
            return secret_santa_picker(names)  # Retry if anyone gets themselves

    pairings = {name: participants[i] for i, name in enumerate(names)}
    return pairings

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/assign', methods=['POST'])
def assign():
    data = request.get_json()
    names = data.get('names', [])
    exclusions = data.get('exclusions', [])
    
    if len(names) < 2:
        return jsonify({"error": "Need at least 2 participants!"}), 400
    
    # Implement exclusion logic if required
    pairings = secret_santa_picker(names)
    return jsonify(pairings)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)

