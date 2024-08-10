from flask import Flask, request, render_template, redirect, url_for, flash
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024  # 100 MB limit
app.secret_key = 'supersecretkey'

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)

    file = request.files['file']

    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)

    if file and len(file.read()) < 10 * 1024 * 1024:  # Check if file is smaller than 10MB
        flash('File must be at least 10MB in size')
        return redirect(request.url)

    file.seek(0)  # Reset file pointer after checking size

    filename = file.filename
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    flash('File successfully uploaded')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
