from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Example questions for demonstration purposes
questions = {
    "behavioral": {
        "Software Developer": {
        "easy": ["Describe a time when you had to work as part of a team.",
                "Tell me about a time you faced a challenge at work.",
                "Describe a time when you had to manage a conflict.",
                "How do you prioritize tasks?",
                "Tell me about a time you had to meet a tight deadline.",
                "Describe a situation where you took the initiative.",
                "Tell me about a time when you received constructive criticism.",
                "How do you handle stress at work?",
                "Describe a situation where you had to solve a problem quickly.",
                "Tell me about a time when you had to adapt to a significant change."],
        "medium": ["Describe a time when you led a project.",
                "Tell me about a situation where you had to make a difficult decision.",
                "Describe a time when you had to manage multiple responsibilities.",
                "How do you handle working under pressure?",
                "Tell me about a time when you had to deal with an uncooperative colleague.",
                "Describe a situation where you had to learn something quickly.",
                "Tell me about a time when you had to mentor a colleague.",
                "How do you approach setting goals?",
                "Describe a time when you had to resolve a disagreement within your team.",
                "Tell me about a situation where you exceeded expectations."],
        "hard": ["Describe a time when you had to turn around a failing project.",
                "Tell me about a situation where you had to manage a significant crisis.",
                "Describe a time when you had to give difficult feedback to a team member.",
                "How do you handle situations where you have to deliver bad news?",
                "Tell me about a time when you had to influence others without authority.",
                "Describe a situation where you had to make a quick decision with limited information.",
                "Tell me about a time when you had to navigate a complex organizational change.",
                "How do you handle conflicts between team members?",
                "Describe a situation where you had to make a decision that was unpopular.",
                "Tell me about a time when you had to work with a difficult stakeholder."
]
    }
    },
    "technical": {
        "Software Developer": {
        "easy": ["Explain the difference between SQL and NoSQL databases.", "What is a REST API?"],
        "medium": ["How do you manage state in React?", "Explain the concept of Big O notation."],
        "hard": ["Describe how you would design a scalable system.", "Explain the principles of microservices architecture."]
    }
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
