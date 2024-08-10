from flask import Flask, render_template, request, redirect, flash
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024  # Max 100 MB
app.secret_key = 'supersecretkey'

# Ensure the upload directory exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    
    file = request.files['file']
    
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    
    # Check file size
    file.seek(0, os.SEEK_END)  # Move to end of file
    file_length = file.tell()  # Get size
    file.seek(0, 0)  # Reset to start

    if file_length < 10 * 1024 * 1024:  # 10 MB minimum
        flash('File is too small. Minimum size is 10 MB.')
        return redirect(request.url)

    file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
    flash('File uploaded successfully')
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
