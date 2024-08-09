from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Example questions for demonstration purposes
questions = {
    "behavioral": {
        "easy": ["Describe a time when you had to work as part of a team.",
                "Tell me about a time you faced a challenge at work.",
                "Describe a time when you had to manage a conflict.",
                "How do you prioritize tasks?",
                "Tell me about a time you had to meet a tight deadline.",
                "Describe a situation where you took the initiative.",
                "Tell me about a time when you received constructive criticism.",
                "How do you handle stress at work?",
                "Describe a situation where you had to solve a problem quickly.",
                "Tell me about a time when you had to adapt to a significant change."
],
        "medium": ["Give an example of how you handle stress.", "Describe a time you had a conflict with a coworker."],
        "hard": ["Describe a situation where you demonstrated leadership.", "Tell me about a time when you had to make a difficult decision."]
    },
    "technical": {
        "easy": ["Explain the difference between SQL and NoSQL databases.", "What is a REST API?"],
        "medium": ["How do you manage state in React?", "Explain the concept of Big O notation."],
        "hard": ["Describe how you would design a scalable system.", "Explain the principles of microservices architecture."]
    }
}

@app.route('/generate_questions', methods=['POST'])
def generate_questions():
    data = request.json
    role = data.get('role')
    topic = data.get('topic')
    difficulty = data.get('difficulty')
    num_questions = data.get('num_questions')

    questions_list = questions.get(topic, {}).get(difficulty, [])
    selected_questions = questions_list[:num_questions]
    
    return jsonify({"questions": selected_questions})

@app.route('/feedback', methods=['POST'])
def provide_feedback():
    data = request.json
    answer = data.get('answer')
    # Placeholder feedback logic
    feedback = f"Your answer to '{answer}' was insightful. Consider providing more specific examples."
    return jsonify({"feedback": feedback})

@app.route('/tips', methods=['GET'])
def get_tips():
    # Placeholder tips
    tips = {
        "general": ["Maintain good body language.", "Dress professionally.", "Be punctual."],
        "role_specific": {
            "Software Developer": ["Practice coding problems.", "Be familiar with system design."],
            "Data Analyst": ["Be ready to discuss data visualization tools.", "Understand statistical analysis techniques."]
        }
    }
    return jsonify(tips)

@app.route('/schedule_mock_interview', methods=['POST'])
def schedule_mock_interview():
    # Placeholder scheduling logic
    return jsonify({"message": "Mock interview scheduled successfully!"})

@app.route('/analyze_progress', methods=['GET'])
def analyze_progress():
    # Placeholder analysis logic
    return jsonify({"progress": "You have completed 5 interviews and received feedback on 3."})

@app.route('/connect_resources', methods=['GET'])
def connect_resources():
    resources = {
        "articles": ["https://example.com/article1", "https://example.com/article2"],
        "books": ["Book Title 1", "Book Title 2"],
        "videos": ["https://example.com/video1", "https://example.com/video2"]
    }
    return jsonify(resources)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
