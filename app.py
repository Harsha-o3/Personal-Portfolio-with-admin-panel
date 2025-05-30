from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/admin-login')
def admin_login():
    return render_template('admin-login.html', error=None)

@app.route('/admin-authenticate', methods=['POST'])
def admin_authenticate():
    username = request.form['username']
    password = request.form['password']

    if username == 'Harsha' and password == 'harsha123':
        return redirect(url_for('admin_dashboard'))
    else:
        return render_template('admin-login.html', error="Invalid credentials")

@app.route('/admin-dashboard')
def admin_dashboard():
    return render_template('admin-dashboard.html')

@app.route('/admin-projects')
def admin_projects():
    return render_template('admin-projects.html')

@app.route('/admin-blogs')
def admin_blogs():
    return render_template('admin-blogs.html')

@app.route('/admin-messages')
def admin_messages():
    return render_template('admin-messages.html')

if __name__ == '__main__':
    app.run(debug=True)
