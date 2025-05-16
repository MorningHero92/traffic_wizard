from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)

# Папка, куда сохраняются видео
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Разрешённые расширения файлов
ALLOWED_EXTENSIONS = {'mp4', 'avi', 'mov'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_video():
    if 'video' not in request.files:
        return "Файл не выбран", 400

    file = request.files['video']

    if file.filename == '':
        return "Имя файла пустое", 400

    if file and allowed_file(file.filename):
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        return f"Видео загружено: {file.filename}"
    else:
        return "Неподдерживаемый формат файла", 400

if __name__ == '__main__':
    app.run(debug=False)
