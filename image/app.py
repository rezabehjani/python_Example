from flask import Flask, render_template
import os

PEOPLE_FOLDER = os.path.join('static', 'people_photo')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER


@app.route('/index')
def show_index():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'qr.png')
    return render_template("index.html", user_image = full_filename)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5555)