from flask import Flask
from flask import render_template
from flask import jsonify

app = Flask(__name__)


jobs = [
    {
        "id": 1,
        "title": "Software Engineer",
        "location": "New York City",
        "salary": "$100,000 - $150,000",
        "description": "We are seeking a talented software engineer to join our team. The ideal candidate will have experience with Python and React, and will be responsible for developing and maintaining our web application.",
        "responsibility": "- Design, develop, and maintain our web application\n- Write clean, efficient, and well-documented code\n- Collaborate with cross-functional teams to identify and solve complex problems",
        "requirements": "- Bachelor's degree in Computer Science or related field\n- 3+ years of experience with Python and React\n- Strong problem-solving skills\n- Excellent written and verbal communication skills"
    },
    {
        "id": 2,
        "title": "Marketing Manager",
        "location": "Los Angeles",
        "salary": "$80,000 - $120,000",
        "description": "We are looking for an experienced marketing manager to join our team. The ideal candidate will have a proven track record of developing and executing successful marketing campaigns.",
        "responsibility": "- Develop and execute marketing campaigns to drive customer acquisition and retention\n- Manage marketing budgets and analyze campaign performance\n- Collaborate with cross-functional teams to develop marketing materials",
        "requirements": "- Bachelor's degree in Marketing or related field\n- 5+ years of experience in marketing\n- Strong analytical skills\n- Excellent written and verbal communication skills"
    },
    {
        "id": 3,
        "title": "Customer Support Representative",
        "location": "Chicago",
        "salary": "$40,000 - $60,000",
        "description": "We are seeking a friendly and customer-focused support representative to join our team. The ideal candidate will have excellent communication skills and be able to troubleshoot and resolve customer issues.",
        "responsibility": "- Respond to customer inquiries via phone, email, and chat\n- Troubleshoot and resolve customer issues\n- Escalate issues to the appropriate team members as needed",
        "requirements": "- High school diploma or equivalent\n- 2+ years of experience in customer service\n- Excellent communication skills\n- Ability to work well in a team environment"
    },
    {
        "id": 4,
        "title": "Graphic Designer",
        "location": "Miami",
        "description": "We are looking for a creative and experienced graphic designer to join our team. The ideal candidate will have a strong portfolio and be able to work on a variety of projects.",
        "responsibility": "- Design and develop visual materials for print and web\n- Collaborate with cross-functional teams to develop marketing materials\n- Manage multiple projects and deadlines",
        "requirements": "- Bachelor's degree in Graphic Design or related field\n- 3+ years of experience in graphic design\n- Strong portfolio showcasing a variety of design styles\n- Proficient in Adobe Creative Suite"
    }
]


@app.route('/')
def index():
    return render_template('home.html', jobs=jobs)


@app.route('/api/joblist')
def joblist():
    return jsonify(jobs)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
