from flask import Flask, Response
import subprocess

app = Flask(__name__)

@app.route('/')
def stream():
    def generate():
        process = subprocess.Popen(['python', 'win.py'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for line in iter(process.stdout.readline, b''):
            yield line.decode('utf-8') + '<br/>'
    return Response(generate(), mimetype='text/html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
