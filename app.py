from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Example questions for demonstration purposes
questions = {
    "behavioral": {
        "Software Developer": {
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
        "Data Analyst": {
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
        "Marketing Manager": {
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
        }
    },
    "technical": {
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
                "How do you ensure the privacy and security of data?",
                "Explain the importance of data-driven decision-making.",
                "Describe your experience with ETL (Extract, Transform, Load) processes."
            ],
            "hard": [
                "Describe a complex data analysis project you have worked on.",
                "How do you approach designing a data pipeline?",
                "Explain the concept of predictive modeling.",
                "How do you handle unstructured data in analysis?",
                "Describe your experience with big data technologies like Hadoop or Spark.",
                "How do you ensure scalability in data processing?",
                "Explain the concept of time series analysis.",
                "How do you integrate data from multiple sources?",
                "Describe your approach to data governance in a large organization.",
                "Explain the concept of anomaly detection in data analysis."
            ]
        },
        "Marketing Manager": {
            "easy": [
                "What is your experience with digital marketing?",
                "How do you measure the success of a marketing campaign?",
                "Explain the concept of target audience.",
                "Describe your experience with social media marketing.",
                "What tools do you use for email marketing?",
                "How do you approach content marketing?",
                "Explain the importance of branding in marketing.",
                "Describe your experience with market research.",
                "What is the role of analytics in marketing?",
                "How do you manage a marketing budget?"
            ],
            "medium": [
                "Describe your experience with SEO (Search Engine Optimization).",
                "How do you develop a marketing strategy?",
                "Explain the concept of customer segmentation.",
                "Describe your experience with paid advertising.",
                "How do you handle marketing automation?",
                "Explain the concept of conversion rate optimization.",
                "Describe your approach to influencer marketing.",
                "How do you measure ROI in marketing?",
                "Explain the importance of customer retention.",
                "Describe your experience with product launches."
            ],
            "hard": [
                "Describe a challenging marketing campaign you have managed.",
                "How do you approach crisis management in marketing?",
                "Explain the concept of integrated marketing communications.",
                "Describe your experience with omnichannel marketing.",
                "How do you handle a significant rebranding effort?",
                "Explain the concept of growth hacking.",
                "Describe your approach to competitive analysis.",
                "How do you ensure alignment between sales and marketing?",
                "Explain the concept of customer lifetime value (CLV).",
                "Describe your experience with global marketing strategies."
            ]
        }
    },
    "Situational": {
        "Software Developer": {
            "easy": [
                "What would you do if you were assigned a task outside your expertise?",
                "How would you handle a situation where you had to work on a project with unclear requirements?",
                "What steps would you take if you discovered a bug in production?",
                "How would you manage a situation where your project deadline was moved up?",
                "What would you do if you were asked to implement a feature you strongly disagreed with?",
                "How would you handle a situation where you had conflicting tasks from different stakeholders?",
                "What would you do if a team member was not contributing to the project?",
                "How would you approach a situation where you had to learn a new technology quickly?",
                "What steps would you take if you were given an unrealistic deadline?",
                "How would you manage a situation where a project requirement changed at the last minute?"
            ],
            "medium": [
                "How would you handle a situation where you identified a major flaw in the project architecture?",
                "What would you do if you were asked to lead a project with a team of less experienced developers?",
                "How would you manage a situation where you were working on multiple projects with conflicting priorities?",
                "What steps would you take if you realized that a project was going to miss its deadline?",
                "How would you handle a situation where a critical piece of code was missing documentation?",
                "What would you do if you were asked to implement a feature that required skills you didn't have?",
                "How would you manage a situation where you had to work with a difficult client?",
                "What would you do if you discovered a security vulnerability in the code?",
                "How would you handle a situation where you had to refactor a large portion of legacy code?",
                "What steps would you take if you were asked to mentor a new team member?"
            ],
            "hard": [
                "How would you handle a situation where a project you were leading was failing?",
                "What would you do if you were asked to make a critical decision with limited information?",
                "How would you manage a situation where you had to deliver bad news to a client or stakeholder?",
                "What steps would you take if you were asked to salvage a project that had already failed?",
                "How would you approach a situation where you had to work with a new team that had low morale?",
                "What would you do if you were asked to make a technical decision that had significant business implications?",
                "How would you manage a situation where you had to integrate a new technology into an existing system?",
                "What steps would you take if you were asked to resolve a conflict between team members?",
                "How would you handle a situation where you had to make a major change to the project scope?",
                "What would you do if you were asked to take over a project from another developer who left unexpectedly?"
            ]
        },
        "Data Analyst": {
            "easy": [
                "How would you handle a situation where you had missing data in a critical report?",
                "What steps would you take if you discovered an error in your analysis after it was delivered?",
                "How would you manage a situation where you had to analyze a dataset with limited information?",
                "What would you do if you were asked to perform an analysis with a tight deadline?",
                "How would you approach a situation where you had conflicting data from different sources?",
                "What steps would you take if you were asked to analyze a dataset that was outside your expertise?",
                "How would you handle a situation where your analysis contradicted the expectations of your stakeholders?",
                "What would you do if you discovered that the data you were analyzing was outdated?",
                "How would you manage a situation where you had to present your findings to a non-technical audience?",
                "What steps would you take if you were asked to deliver insights on a dataset that was incomplete?"
            ],
            "medium": [
                "How would you handle a situation where your analysis revealed unexpected trends?",
                "What steps would you take if you were asked to develop a new model with insufficient data?",
                "How would you manage a situation where you had to reconcile conflicting analytical results?",
                "What would you do if you were asked to present your analysis to senior management with little notice?",
                "How would you handle a situation where you were asked to analyze a highly sensitive dataset?",
                "What steps would you take if your analysis was questioned by a senior analyst?",
                "How would you manage a situation where you had to deliver actionable insights from a very large dataset?",
                "What would you do if you were asked to analyze data using a tool you were unfamiliar with?",
                "How would you handle a situation where your analysis led to a major strategic decision?",
                "What steps would you take if you were asked to collaborate on an analysis with a colleague from a different department?"
            ],
            "hard": [
                "How would you handle a situation where your analysis had significant financial implications?",
                "What would you do if you were asked to make a data-driven decision with incomplete data?",
                "How would you manage a situation where you had to balance accuracy with speed in delivering analysis?",
                "What steps would you take if your analysis led to a decision that was later questioned?",
                "How would you approach a situation where your analysis had to be defended in front of a board of directors?",
                "What would you do if you were asked to develop a predictive model with minimal historical data?",
                "How would you handle a situation where you had to explain a complex analytical model to non-technical stakeholders?",
                "What steps would you take if you were asked to lead a project that involved integrating data from multiple sources?",
                "How would you manage a situation where your analysis revealed a major risk to the business?",
                "What would you do if you were asked to provide insights on a rapidly changing dataset?"
            ]
        },
        "Marketing Manager": {
            "easy": [
                "How would you handle a situation where your marketing campaign was not performing as expected?",
                "What steps would you take if you were asked to launch a new product with minimal budget?",
                "How would you manage a situation where you had to market a product in a highly competitive market?",
                "What would you do if you were asked to improve the brand image of a company?",
                "How would you handle a situation where your team was not meeting its targets?",
                "What steps would you take if you were asked to develop a marketing strategy for a new market?",
                "How would you manage a situation where you had to handle negative feedback on social media?",
                "What would you do if you were asked to increase the ROI of a marketing campaign?",
                "How would you handle a situation where you had to create a marketing plan with limited data?",
                "What steps would you take if you were asked to coordinate a multi-channel marketing campaign?"
            ],
            "medium": [
                "How would you handle a situation where your marketing campaign faced unexpected challenges?",
                "What steps would you take if you were asked to rebrand a well-known product?",
                "How would you manage a situation where you had to align marketing efforts with a new company strategy?",
                "What would you do if you were asked to create a marketing plan for a product with a declining market share?",
                "How would you handle a situation where your marketing efforts were not generating leads?",
                "What steps would you take if you were asked to launch a new product in an unfamiliar market?",
                "How would you manage a situation where you had to work with a limited marketing budget?",
                "What would you do if you were asked to manage a crisis situation that affected the brand?",
                "How would you handle a situation where you had to develop a marketing strategy for a niche audience?",
                "What steps would you take if you were asked to improve customer engagement through marketing?"
            ],
            "hard": [
                "How would you handle a situation where your marketing strategy was failing to achieve its objectives?",
                "What would you do if you were asked to manage a major marketing campaign with high stakes?",                                                                                                                      
                "How would you manage a situation where you had to lead a marketing team through a significant organizational change?",
                "What steps would you take if you were asked to turn around a failing brand?",
                "How would you handle a situation where your marketing efforts were met with strong resistance from stakeholders?",
                "What would you do if you were asked to create a marketing strategy for a product in a saturated market?",
                "How would you manage a situation where you had to respond to a major PR crisis?",
                "What steps would you take if you were asked to lead a global marketing campaign?",
                "How would you handle a situation where you had to drive growth in a declining market?",
                "What would you do if you were asked to lead a rebranding effort after a major scandal?"
            ]
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
