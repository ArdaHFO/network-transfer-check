This project explores how files are sent and received when measuring a connection speed.

<h1 align="center">Network Transfer Lab</h1>

<p align="center"><strong>Explore the mechanics behind a speed test.</strong></p>
<p align="center">A Flask coursework prototype combining a browser timing interface with an experimental server-side transfer route.</p>

<p align="center">
  <strong>English</strong> · <a href="README.tr.md">Türkçe</a><br />
  <a href="#run-the-local-interface"><strong>Run the local interface</strong></a> ·
  <a href="#inside-the-project">Project overview</a> ·
  <a href="#validation-and-current-limits">Current limits</a>
</p>

---

This repository contains a Python, HTML and JavaScript speed-test experiment from a November 2023 coursework project. Its browser interface explores timed downloads, uploads and HTTP requests. A separate server route experiments with a larger download and speedtest-cli upload measurement.

**This is an experimental coursework prototype.** Transfer routes, timing calculations and the server result template have received static fixes. The project remains an experiment whose output has not been validated as a bandwidth benchmark.

## Run the local interface

| Requirement | Purpose |
| --- | --- |
| Python 3 with pip and venv | Isolated development environment |
| Flask, Requests and speedtest-cli | Application imports |
| Browser with JavaScript | Timing interface |

```text
git clone https://github.com/ArdaHFO/network-transfer-lab.git
cd network-transfer-lab
python -m venv .venv
```

Activate `.venv\Scripts\activate` in Windows Command Prompt or `source .venv/bin/activate` on macOS/Linux, then install the recorded dependencies and start a local preview.

```text
python -m pip install -r requirements.txt
python -m flask --app app run --host 127.0.0.1 --port 8000
```

Open [localhost:8000](http://127.0.0.1:8000). The Flask CLI and the application entry point both default to local access with debug mode disabled. Dependency pins are historical and their compatibility with current Python installations has not been revalidated.

## Inside the project

- **Browser timing interface.** Separate controls illustrate download timing, multipart uploads and HTTP round trips.
- **Custom server download.** The `speed_test` function streams a configured file from an external endpoint and tracks received bytes.
- **Library comparison.** `POST /measure` includes a speedtest-cli upload measurement and reads its ping result.
- **Flask blueprints.** A small `views.py` module provides additional page routes.
- **Transfer fixtures.** Several image files are included for experimentation.

The backend uses speedtest-cli alongside custom transfer measurement.

## Browser and server paths

| Component | Intended action | Current state |
| --- | --- | --- |
| Browser download | Fetch the bundled fixture and calculate a rate | Actual received bytes and elapsed seconds |
| Browser upload | Send a file to `POST /upload` | Server confirms byte count without saving an application file |
| Browser ping | Time `GET /ping` | Uncached `Pong` response |
| `POST /measure` | Download 100 MB and perform a library upload | Renders the server result template |
| `GET /views/measure` | Open the interface | Redirects instead of displaying empty results |

Browser HTTP timing and server-originated transfers measure different paths. A result produced on a remote server describes that server's connectivity, not necessarily the user's connection.

## Validation and current limits

The source has been reviewed statically. No application execution, automated tests, external transfers or benchmarks were performed for these changes.

- Browser transfer rates use successful responses, actual payload bytes, elapsed seconds and decimal Mbps. The download fixture is the bundled `20MB.png`, with caching disabled.
- Upload requests are limited to 32 MiB including multipart overhead. The server confirms the complete byte count without retaining a saved application file.
- The server download calculation uses one measured duration and actual received bytes. Its result template is included. These paths have not been exercised at runtime.
- Browser timing includes HTTP/application overhead. A local Flask server measures a local path, not ISP bandwidth.
- The server measurement route depends on external transfer services and speedtest-cli. Current availability, accuracy and repeatability are not established.
- The unused system-ping helper remains platform-dependent. Its invocation has a timeout and fixed request count.

Controlled route checks and repeated transfer measurements are still needed before making accuracy claims.

## Project map

```text
app.py                 Flask routes and server transfer experiment
views.py               Additional page routes
templates/index.html   Browser timing interface
templates/measure.html Server transfer result view
1MB.png, 5MB.png,
10MB.png, 20MB.png      Transfer fixtures
requirements.txt       Historical dependency versions
```

## Development and contributions

For a proposed change, state whether it affects browser timing or server timing. Include the route, HTTP status, expected payload size and calculation in bug reports. Separate local route checks from network benchmarks, and avoid presenting a successful page render as proof of measurement accuracy.

## License and credits

Distributed under the [MIT license](LICENSE). Flask, Requests, speedtest-cli and external services retain their own licenses and terms.
