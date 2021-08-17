import os
import json
from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'C:/Users/Student/PycharmProjects/pythonProject/static/img/'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


@app.route('/')
def index():
    return render_template("index.html")


@app.route("/", methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and (file.content_type.rsplit('/', 1)[1] in ALLOWED_EXTENSIONS).__bool__():
            filename = secure_filename(file.filename)
            file.save(app.config['UPLOAD_FOLDER'] + filename)
            with open(f"{app.config['UPLOAD_FOLDER'] + filename}", 'r') as f:
        # твой код
    return redirect("/")


def classification(my_file):
    with open(my_file, "r") as f:
        name = os.path.basename(f.name)
        if name.find("_") == -1 or name[name.find("_") + 1] == "1":
            main = True
        else:
            main = False
    output = json.dumps({'type': (f'{"main" if main else "other"}')})
    print(output)


if __name__ == "__main__":
    app.run()

classification("myfile_1.txt")
