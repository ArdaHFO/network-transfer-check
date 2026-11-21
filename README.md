This app measures file transfer speeds in a browser and on the server that hosts it.

# Network Transfer Check

[English](README.md) · [Türkçe](README.tr.md)

The Flask app has two measurement paths. The web page transfers files between your browser and the app. `POST /measure` instead requests a 100 MB download from thinkbroadband and runs a speedtest-cli upload from the server.

## Run locally

You need Python 3 with pip and venv, and a browser with JavaScript enabled.

```text
git clone https://github.com/ArdaHFO/network-transfer-check.git
cd network-transfer-check
python -m venv .venv
```

Activate the environment with `.venv\Scripts\activate` in Windows Command Prompt, or `source .venv/bin/activate` on macOS/Linux.

```text
python -m pip install -r requirements.txt
python -m flask --app app run --host 127.0.0.1 --port 8000
```

Open [localhost:8000](http://127.0.0.1:8000). The dependency pins in [requirements.txt](requirements.txt) come from the original development environment; compatibility with newer Python versions has not been verified.

## Measurement paths

| Request | What it does |
| --- | --- |
| `GET /download` | Sends the bundled `20MB.png` to the browser |
| `POST /upload` | Reads the selected file and returns its byte count without saving a copy |
| `GET /ping` | Returns `Pong` so the browser can time an HTTP round trip |
| `POST /measure` | Runs the external download and speedtest-cli upload, then renders a server result page |

The page buttons use the first three routes. The server measurement is a separate POST request and includes speedtest-cli's ping result. `GET /views/measure` redirects to the main page.

Browser uploads are limited to **32 MiB**, including multipart overhead. Download and ping responses disable caching.

## Limits

Custom download and browser transfer rates use actual bytes and elapsed seconds:

```text
Mbps = bytes × 8 / seconds / 1,000,000
```

HTTP and application overhead contribute to these timings. The browser's Ping button is an HTTP measurement, not an ICMP ping. The separate system-ping helper in `app.py` is unused and its output parsing is platform-dependent.

A localhost transfer measures the local browser-to-server path. The external download and speedtest-cli upload measure the server's connection. Neither automatically describes the connection of a visitor using a remote deployment.

These paths have not been validated end to end. Accuracy, repeatability and the availability of the external services remain unverified.

## Code and license

[app.py](app.py) contains the Flask routes and streaming download calculation. Browser controls are in [templates/index.html](templates/index.html), and server results use [templates/measure.html](templates/measure.html). [views.py](views.py) defines the alternate routes.

[MIT license](LICENSE). Flask, Requests, speedtest-cli and external services retain their own licenses and terms.
