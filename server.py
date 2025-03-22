from flask import Flask, render_template
from github_api import prepare_resume_data

app = Flask(__name__)
resume_data = None

def update_resume_data():
    global resume_data
    resume_data = prepare_resume_data()

@app.route('/')
def home():
    global resume_data
    if resume_data is None:
        update_resume_data()
    return render_template('resume.html', data=resume_data)

@app.route('/refresh')
def refresh():
    update_resume_data()
    return render_template('resume.html', data=resume_data)

if __name__ == '__main__':
    update_resume_data()
    app.run(debug=True, host='0.0.0.0', port=5000)