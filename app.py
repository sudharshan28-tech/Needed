from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Example questions for demonstration purposes
questions = {
    "Behavioral": {
        "easy": [
            "Describe a time when you had to work as part of a team.",
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
        "medium": [
            "Describe a time when you led a project.",
            "Tell me about a situation where you had to make a difficult decision.",
            "Describe a time when you had to manage multiple responsibilities.",
            "How do you handle working under pressure?",
            "Tell me about a time when you had to deal with an uncooperative colleague.",
            "Describe a situation where you had to learn something quickly.",
            "Tell me about a time when you had to mentor a colleague.",
            "How do you approach setting goals?",
            "Describe a time when you had to resolve a disagreement within your team.",
            "Tell me about a situation where you exceeded expectations."
        ],
        "hard": [
            "Describe a time when you had to turn around a failing project.",
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
    },
    "Technical": {
        "Software Developer": {
            "easy": [
                "What is your experience with Python?",
                "How do you manage version control using Git?",
                "What is a RESTful API?",
                "Explain the concept of object-oriented programming.",
                "Describe the difference between a list and a tuple in Python.",
                "How do you ensure the quality of your code?",
                "Explain the importance of testing in software development.",
                "What is the difference between SQL and NoSQL databases?",
                "How do you handle exceptions in programming?",
                "Describe your experience with cloud computing platforms."
            ],
            "medium": [
                "Explain the SOLID principles of software design.",
                "How do you optimize database queries?",
                "Describe your experience with microservices architecture.",
                "What is continuous integration/continuous deployment (CI/CD)?",
                "How do you ensure security in web applications?",
                "Explain the concept of polymorphism in object-oriented programming.",
                "How do you manage dependencies in a software project?",
                "Describe your approach to writing scalable code.",
                "What is the role of a software architect?",
                "Explain the concept of machine learning and its applications."
            ],
            "hard": [
                "Describe a complex system you have designed or worked on.",
                "How do you handle performance bottlenecks in a large-scale application?",
                "Explain the trade-offs between different types of data structures.",
                "How do you approach designing a distributed system?",
                "Describe your experience with containerization and orchestration tools like Docker and Kubernetes.",
                "How do you ensure high availability and reliability in a system?",
                "Explain the concept of eventual consistency in distributed databases.",
                "How do you handle large-scale data processing?",
                "Describe your experience with real-time data streaming technologies.",
                "Explain the principles of DevOps and how you have applied them in your projects."
            ]
        },
        "Data Analyst": {
            "easy": [
                "What tools do you use for data analysis?",
                "How do you handle missing data in a dataset?",
                "What is the difference between structured and unstructured data?",
                "Describe your experience with SQL queries.",
                "How do you ensure data quality?",
                "What is data normalization, and why is it important?",
                "Explain the concept of data visualization.",
                "How do you choose the right chart type for your data?",
                "Describe your experience with Excel for data analysis.",
                "What is the significance of data governance?"
            ],
            "medium": [
                "Explain the concept of data warehousing.",
                "How do you perform exploratory data analysis?",
                "Describe your experience with statistical modeling.",
                "What is the role of machine learning in data analysis?",
                "How do you handle large datasets?",
                "Explain the concept of A/B testing.",
                "Describe your experience with Python or R for data analysis.",
                "How do you approach data storytelling?",
                "What is the significance of outliers in a dataset?",
                "How do you ensure the security of sensitive data?"
            ],
            "hard": [
                "Describe a complex data analysis project you have worked on.",
                "How do you handle real-time data analysis?",
                "Explain the concept of predictive modeling.",
                "Describe your experience with big data technologies.",
                "How do you approach data integration from multiple sources?",
                "Explain the concept of anomaly detection.",
                "Describe your experience with data engineering.",
                "How do you handle the challenges of data scalability?",
                "What is the role of AI in data analytics?",
                "Explain the concept of data ethics and how it applies to your work."
            ]
        },
        "Marketing Manager": {
            "easy": [
                "What digital marketing tools do you use?",
                "How do you measure the success of a marketing campaign?",
                "Explain the concept of SEO.",
                "Describe your experience with social media marketing.",
                "How do you segment your target audience?",
                "What is the importance of branding in marketing?",
                "Explain the concept of content marketing.",
                "How do you handle customer feedback?",
                "Describe your experience with email marketing.",
                "What is the role of analytics in marketing?"
            ],
            "medium": [
                "Explain the concept of customer journey mapping.",
                "How do you approach market research?",
                "Describe your experience with influencer marketing.",
                "What is the significance of customer retention?",
                "How do you create a marketing budget?",
                "Explain the concept of product positioning.",
                "Describe your experience with marketing automation.",
                "How do you handle a marketing crisis?",
                "What is the role of storytelling in marketing?",
                "How do you approach cross-channel marketing?"
            ],
            "hard": [
                "Describe a complex marketing campaign you have led.",
                "How do you handle the challenges of global marketing?",
                "Explain the concept of omnichannel marketing.",
                "Describe your experience with brand management.",
                "How do you approach data-driven marketing?",
                "Explain the concept of customer lifetime value (CLTV).",
                "Describe your experience with growth hacking.",
                "How do you handle the challenges of marketing in a highly competitive industry?",
                "What is the role of AI in modern marketing?",
                "Explain the concept of sustainable marketing and how it applies to your work."
            ]
        }
    },
    "Situational": {
        "easy": [
            "What would you do if you disagreed with your manager's decision?",
            "How would you handle a situation where you missed a deadline?",
            "What would you do if you were assigned a task outside your expertise?",
            "How would you approach a situation where a team member isn't pulling their weight?",
            "What would you do if you had to handle multiple urgent tasks at once?",
            "How would you deal with a difficult client?",
            "What would you do if you noticed a mistake in your colleague's work?",
            "How would you handle a situation where you had to learn a new skill quickly?",
            "What would you do if you received conflicting instructions from two managers?",
            "How would you handle a situation where you had to work with a new team?"
        ],
        "medium": [
            "How would you handle a situation where a project is falling behind schedule?",
            "What would you do if you had to mediate a conflict between team members?",
            "How would you approach a situation where your team is resistant to change?",
            "What would you do if you were asked to lead a project with an unfamiliar technology?",
            "How would you handle a situation where you had to meet an unrealistic deadline?",
            "What would you do if you received negative feedback from a client?",
            "How would you approach a situation where your project budget is cut?",
            "What would you do if your team is consistently missing targets?",
            "How would you handle a situation where you have to make a decision without enough data?",
            "What would you do if you had to deliver a project with limited resources?"
        ],
        "hard": [
            "How would you handle a situation where a key team member suddenly leaves?",
            "What would you do if you had to manage a project with conflicting stakeholder interests?",
            "How would you approach a situation where your project is under public scrutiny?",
            "What would you do if your team is struggling with low morale?",
            "How would you handle a situation where you have to turn around a failing project?",
            "What would you do if you had to implement a major organizational change?",
            "How would you handle a situation where you have to negotiate with a difficult client?",
            "What would you do if you had to lead a team through a crisis?",
            "How would you approach a situation where your company is facing a financial downturn?",
            "What would you do if you had to manage a cross-functional team with conflicting priorities?"
        ]
    }
}

@app.route('/generate_questions', methods=['POST'])
def generate_questions():
    data = request.json
    role = data.get('role')
    category = data.get('topic')  # Assuming 'topic' refers to 'category'
    difficulty = data.get('difficulty')
    num_questions = data.get('num_questions')

    # Initialize an empty list for questions
    questions_list = []

    if category == 'Technical' and role:
        # Fetch questions based on role, category, and difficulty for Technical category
        questions_list = questions.get(category, {}).get(role, {}).get(difficulty, [])
    else:
        # Fetch questions based only on category and difficulty for non-Technical categories
        questions_list = questions.get(category, {}).get(difficulty, [])

    # Select the required number of questions
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
