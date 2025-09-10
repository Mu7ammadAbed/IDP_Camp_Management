from flask import Flask, render_template

app = Flask(__name__)
# Routes
@app.route('/')
def landing_page():
    return render_template('landing_page.html')

@app.route('/dashboard')
def dashboard():
    return render_template('admin_dashboard.html')

@app.route('/families')
def families():
    return render_template('family_management.html')

@app.route('/special-needs')
def specialNeeds():
    return render_template('special_needs_tracking.html')

if __name__ == '__main__':   
    app.run(debug=True)