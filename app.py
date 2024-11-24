from flask import Flask, request, send_file
import os
import subprocess

app = Flask(__name__)

FILES = './uploads'
os.makedirs(FILES, exist_ok=True)

@app.route('/')
def index():
    return send_file('main.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']

    # Save the uploaded file
    upload_path = os.path.join(FILES, file.filename)
    file.save(upload_path)

    try:
        subprocess.run(
            [
                "libreoffice",
                "--headless",
                "--convert-to",
                "pdf",
                "--outdir",
                FILES,
                upload_path
            ],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Error converting {input_path} to PDF: {e.stderr.decode()}")

    response_path = upload_path.rsplit('.',1)[0] + '.pdf'

    return send_file(response_path, as_attachment=True)

if __name__ == '__main__':
    app.run()

