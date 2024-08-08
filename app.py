from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///interview_bot.db'
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

# Routes
@app.route('/questions', methods=['GET'])
def get_questions():
    question_type = request.args.get('type')
    difficulty = request.args.get('difficulty')
    questions = Question.query.filter_by(type=question_type, difficulty=difficulty).all()
    return jsonify([q.text for q in questions])

@app.route('/feedback', methods=['POST'])
def give_feedback():
    data = request.json
    response = UserResponse(question_id=data['question_id'], response=data['response'], feedback='Good job! Keep improving.')
    db.session.add(response)
    db.session.commit()
    return jsonify({'feedback': response.feedback})

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
    user = User.query.get(user_id)
    return jsonify({'progress': user.progress})

@app.route('/resources', methods=['GET'])
def get_resources():
    resources = [
        {'type': 'article', 'title': 'How to ace your interview', 'link': 'https://example.com'},
        {'type': 'book', 'title': 'Cracking the Coding Interview', 'link': 'https://example.com'}
    ]
    return jsonify(resources)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
