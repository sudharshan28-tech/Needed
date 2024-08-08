from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///interview_bot.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Models
class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50))
    difficulty = db.Column(db.String(50))
    text = db.Column(db.String(500))

class UserResponse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))
    response = db.Column(db.String(1000))
    feedback = db.Column(db.String(1000))

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    progress = db.Column(db.String(1000))

# Create tables if they do not exist
@app.before_first_request
def create_tables():
    if not os.path.exists('interview_bot.db'):
        print("Database file not found. Creating tables.")
    else:
        print("Database file found. Ensuring tables exist.")
    with app.app_context():
        db.create_all()

# Routes
@app.route('/questions', methods=['GET'])
def get_questions():
    question_type = request.args.get('type')
    difficulty = request.args.get('difficulty')
    try:
        questions = Question.query.filter_by(type=question_type, difficulty=difficulty).all()
        return jsonify([q.text for q in questions])
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/feedback', methods=['POST'])
def give_feedback():
    data = request.json
    try:
        response = UserResponse(question_id=data['question_id'], response=data['response'], feedback='Good job! Keep improving.')
        db.session.add(response)
        db.session.commit()
        return jsonify({'feedback': response.feedback})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/tips', methods=['GET'])
def get_tips():
    tips = {
        'general': 'Be confident and dress appropriately.',
        'specific': 'For tech roles, focus on your problem-solving skills.'
    }
    return jsonify(tips)

@app.route('/schedule', methods=['POST'])
def schedule_mock_interview():
    # Implementation for scheduling
    return jsonify({'status': 'scheduled'})

@app.route('/progress', methods=['GET'])
def get_progress():
    user_id = request.args.get('user_id')
    try:
        user = User.query.get(user_id)
        if user:
            return jsonify({'progress': user.progress})
        else:
            return jsonify({'error': 'User not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/resources', methods=['GET'])
def get_resources():
    resources = [
        {'type': 'article', 'title': 'How to ace your interview', 'link': 'https://example.com'},
        {'type': 'book', 'title': 'Cracking the Coding Interview', 'link': 'https://example.com'}
    ]
    return jsonify(resources)

if __name__ == '__main__':
    # Create tables and run the application
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=80, debug=True)
