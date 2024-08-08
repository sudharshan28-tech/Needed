from flask import Flask, request, jsonify

app = Flask(__name__)

# Store user scores
user_scores = {}

@app.route('/submit_answer', methods=['POST'])
def submit_answer():
    data = request.get_json()
    user_answer = data.get('user_answer')
    
    # For simplicity, the correct answer is always 8 for this example
    correct_answer = 8
    
    if int(user_answer) == correct_answer:
        result = "Correct!"
        score = user_scores.get('user', 0) + 1
        user_scores['user'] = score
    else:
        result = "Incorrect!"
    
    return jsonify({"message": result, "score": user_scores.get('user', 0)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
