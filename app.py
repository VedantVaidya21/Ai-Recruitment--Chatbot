from flask import Flask, request, jsonify, render_template
import joblib

app = Flask(__name__)

# Load the trained model and vectorizer
model = joblib.load('model.pkl')
vectorizer = joblib.load('cmodel.pkl')

job_titles = [
    {"title": "Software Engineer", "short_name": "SE"},
    {"title": "Data Scientist", "short_name": "DS"},
    {"title": "Product Manager", "short_name": "PM"},
    {"title": "Marketing Manager", "short_name": "MM"},
    {"title": "Human Resources Manager", "short_name": "HRM"},
    {"title": "Graphic Designer", "short_name": "GD"},
    {"title": "Web Developer", "short_name": "WD"},
    {"title": "Systems Analyst", "short_name": "SA"},
    {"title": "Project Manager", "short_name": "PM"},
    {"title": "Business Analyst", "short_name": "BA"},
    {"title": "Database Administrator", "short_name": "DBA"},
    {"title": "Network Engineer", "short_name": "NE"},
    {"title": "UX/UI Designer", "short_name": "UX/UI"},
    {"title": "Financial Analyst", "short_name": "FA"},
    {"title": "Operations Manager", "short_name": "OM"},
    {"title": "Sales Manager", "short_name": "SM"},
    {"title": "Customer Support Specialist", "short_name": "CSS"},
    {"title": "Content Writer", "short_name": "CW"},
    {"title": "Legal Advisor", "short_name": "LA"},
    {"title": "Healthcare Administrator", "short_name": "HA"},
    {"title": "Civil Engineer", "short_name": "CE"},
    {"title": "Electrical Engineer", "short_name": "EE"},
    {"title": "Mechanical Engineer", "short_name": "ME"},
    {"title": "Architect", "short_name": "ARCH"},
    {"title": "Teacher", "short_name": "TCHR"},
    {"title": "Research Scientist", "short_name": "RS"},
    {"title": "Chef", "short_name": "CHEF"},
    {"title": "Nurse", "short_name": "NUR"},
    {"title": "Pharmacist", "short_name": "PHAR"},
    {"title": "Dentist", "short_name": "DEN"},
    {"title": "Veterinarian", "short_name": "VET"},
    {"title": "Accountant", "short_name": "ACC"},
    {"title": "Administrative Assistant", "short_name": "AA"},
    {"title": "Event Coordinator", "short_name": "EC"},
    {"title": "Public Relations Specialist", "short_name": "PRS"},
    {"title": "Social Media Manager", "short_name": "SMM"},
    {"title": "Research Analyst", "short_name": "RA"},
    {"title": "Logistics Manager", "short_name": "LM"},
    {"title": "Quality Assurance Specialist", "short_name": "QA"},
    {"title": "Supply Chain Manager", "short_name": "SCM"},
    {"title": "Business Development Manager", "short_name": "BDM"},
    {"title": "Training Coordinator", "short_name": "TC"},
    {"title": "Real Estate Agent", "short_name": "REA"},
    {"title": "Insurance Agent", "short_name": "IA"},
    {"title": "Technical Support Specialist", "short_name": "TSS"},
    {"title": "Copywriter", "short_name": "CW"},
    {"title": "Animator", "short_name": "ANIM"},
    {"title": "Interior Designer", "short_name": "ID"},
    {"title": "Fashion Designer", "short_name": "FD"},
    {"title": "Medical Technician", "short_name": "MT"},
    {"title": "Construction Manager", "short_name": "CM"},
    {"title": "Electrician", "short_name": "ELEC"},
    {"title": "Plumber", "short_name": "PLUM"},
    {"title": "Welder", "short_name": "WELD"},
    {"title": "Driver", "short_name": "DRV"},
    {"title": "Security Guard", "short_name": "SG"},
    {"title": "Housekeeper", "short_name": "HK"},
    {"title": "Tour Guide", "short_name": "TG"},
    {"title": "Flight Attendant", "short_name": "FA"},
    {"title": "Travel Agent", "short_name": "TA"},
    {"title": "Environmental Scientist", "short_name": "ES"},
    {"title": "Biologist", "short_name": "BIO"},
    {"title": "Chemist", "short_name": "CHEM"},
    {"title": "Physicist", "short_name": "PHY"},
    {"title": "Geologist", "short_name": "GEO"},
    {"title": "Astronomer", "short_name": "AST"},
    {"title": "Meteorologist", "short_name": "MET"},
    {"title": "Archivist", "short_name": "ARCH"},
    {"title": "Librarian", "short_name": "LIB"},
    {"title": "Curator", "short_name": "CUR"},
    {"title": "Museum Educator", "short_name": "ME"},
    {"title": "Park Ranger", "short_name": "PR"},
    {"title": "Historian", "short_name": "HIST"}
]

def get_job_response(message):
    for job in job_titles:
        if job["title"].lower() in message.lower() or job["short_name"].lower() in message.lower():
            return f"Please send your resume for the {job['title']} position."
    return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/candidate')
def candidate_login():
    return render_template('candidate.html')

@app.route('/recruiter_login')
def recruiter_login():
    return render_template('recruiter_login.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    message = data.get('message')
    
    # Check for specific job roles
    job_response = get_job_response(message)
    if job_response:
        response = job_response
    else:
        # Transform the message using the vectorizer
        message_vectorized = vectorizer.transform([message])
        
        # Get the prediction from the model
        prediction = model.predict(message_vectorized)[0]
        
        # Use prediction as response
        response = prediction

    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
