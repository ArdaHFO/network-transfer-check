from flask import Flask, render_template, request, jsonify, send_file
from pathlib import Path
from views import views
import requests
import time
import speedtest
import sys, time, io, requests, threading
import subprocess
import platform
import re

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 32 * 1024 * 1024
app.register_blueprint(views, url_prefix = "/views")

@app.route('/')
def index():
    return render_template('index.html')

def speed_test(size=5, ipv="ipv4", port=80):
    requested_size = "1GB" if size == 1024 else f"{size}MB"
    url = f"http://{ipv}.download.thinkbroadband.com:{port}/{requested_size}.zip"
    start = time.perf_counter()
    with requests.get(url, stream=True, timeout=(10, 60)) as response:
        response.raise_for_status()
        transferred = sum(len(chunk) for chunk in response.iter_content(64 * 1024))
    elapsed = time.perf_counter() - start
    if elapsed <= 0:
        raise RuntimeError("The transfer duration could not be measured.")
    return f"{elapsed:.2f} seconds", transferred * 8 / elapsed / 1_000_000, f"{transferred} bytes"

def measure_ping_speed():
 try:
        count_flag = '-n' if platform.system().lower() == 'windows' else '-c'
        output = subprocess.check_output(['ping', count_flag, '4', 'www.google.com'], timeout=15)
        output = output.decode('utf-8', errors='replace')
        matches = re.search(r'(\d+\.\d+) ms', output)
        if matches:
            ping_speed = float(matches.group(1))
            return ping_speed
 except (OSError, subprocess.SubprocessError):
    pass
    return None

   
@app.route('/measure', methods=['POST'])
def measure():
    if request.method == 'POST':
        ########BEGIN CODE
        t_download_time,  t_download_speed, t_download_datasize = speed_test(100, port=8080)#Add new line
        download_datasize = t_download_datasize
        download_datatime = t_download_time
        download_speed = t_download_speed 

        st = speedtest.Speedtest()
        upload_speed = st.upload() / 10**6  # Convert to Mbps
        
        
        #ping_speed = measure_ping_speed()
        #if ping_speed is not None:
        #    print(f"Ping hızı: {ping_speed:.2f} ms")
        #else:
        #    print("Ping hızı ölçülemedi.")
        ping = st.results.ping

        ########END CODE
    return render_template('measure.html',  download_datatime=download_datatime, download_datasize=download_datasize, download_speed=download_speed, upload_speed=upload_speed, ping=ping)

@app.route('/ping')
def ping():
    return 'Pong', 200, {'Cache-Control': 'no-store'}


@app.route('/download')
def download():
    response = send_file(
        Path(app.root_path) / '20MB.png',
        mimetype='application/octet-stream',
        as_attachment=True,
        download_name='20MB.png',
        conditional=False,
        etag=False,
        max_age=0,
    )
    response.headers['Cache-Control'] = 'no-store'
    return response


@app.route('/upload', methods=['POST'])
def upload():
    file = request.files.get('file')
    if file is None or not file.filename:
        return jsonify(error='Select a file to upload.'), 400
    received = 0
    for chunk in iter(lambda: file.stream.read(64 * 1024), b''):
        received += len(chunk)
    return jsonify(bytes_received=received)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=False)
