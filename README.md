<h1 align="center">Speedtest Final</h1>

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

**The name “Final” identifies this repository, not a verified release status.** The tracked implementation has incomplete routes and calculation issues. It is suitable for studying the code and planning corrections, but the current output is not a validated bandwidth measurement.

## Run the local interface

| Requirement | Purpose |
| --- | --- |
| Python 3 with pip and venv | Isolated development environment |
| Flask, Requests and speedtest-cli | Application imports |
| Browser with JavaScript | Timing interface |

```text
git clone https://github.com/ArdaHFO/speedtestFinal.git
cd speedtestFinal
python -m venv .venv
```

Activate `.venv\Scripts\activate` in Windows Command Prompt or `source .venv/bin/activate` on macOS/Linux, then install the recorded dependencies and start a local preview.

```text
python -m pip install -r requirements.txt
python -m flask --app app run --host 127.0.0.1 --port 8000
```

Open [localhost:8000](http://127.0.0.1:8000). The Flask CLI keeps this preview on the local interface instead of using the script's all-interface debug launch. Dependency pins are historical and their compatibility with current Python installations has not been revalidated.

## Inside the project

- **Browser timing interface.** Separate controls illustrate download timing, multipart uploads and HTTP round trips.
- **Custom server download.** The `speed_test` function streams a configured file from an external endpoint and tracks received bytes.
- **Library comparison.** `POST /measure` includes a speedtest-cli upload measurement and reads its ping result.
- **Flask blueprints.** A small `views.py` module provides additional page routes.
- **Transfer fixtures.** Several image files are included for experimentation.

The backend does use speedtest-cli. The older README's claim that the project avoids its predefined measurement functions does not describe the current `app.py`.

## Browser and server paths

| Component | Intended action | Current state |
| --- | --- | --- |
| Browser download | Fetch an external image and calculate a rate | Fixed assumed size and incorrect Mbps conversion |
| Browser upload | Send a file to `POST /upload` | No matching backend route |
| Browser ping | Time `GET /ping` | No matching backend route |
| `POST /measure` | Download 100 MB and perform a library upload | Undefined variable and missing result template |
| `GET /views/measure` | Display the result template | Template is absent |

Browser HTTP timing and server-originated transfers measure different paths. A result produced on a remote server describes that server's connectivity, not necessarily the user's connection.

## Validation and current limits

The Python code, templates, routes and dependency manifest were reviewed. No external transfers, speed benchmarks or runtime integration tests were performed.

- `speed_test` refers to `startP`, which is not defined.
- Both result routes reference `templates/measure.html`, which is not in this repository.
- The browser's upload and ping handlers call endpoints that are not implemented. The JavaScript does not check HTTP success before displaying timing results.
- Download size assumptions, time conversion and byte-to-bit conversion need correction before values can be described as Mbps.
- The remote image and transfer service are external dependencies. Their availability and cross-origin behavior are not verified.
- The unused system-ping helper is platform-dependent. The server's main entry point enables debug mode on all interfaces, so use the local preview command above.

These are existing source limitations. This documentation update does not change the application. A useful next step is to complete the route-to-template flow, then validate units and actual byte counts with controlled fixtures before measuring an internet connection.

## Project map

```text
app.py                 Flask routes and server transfer experiment
views.py               Additional page routes
templates/index.html   Browser timing interface
1MB.png, 5MB.png,
10MB.png, 20MB.png      Transfer fixtures
requirements.txt       Historical dependency versions
```

## Development and contributions

For a proposed change, state whether it affects browser timing or server timing. Include the route, HTTP status, expected payload size and calculation in bug reports. Separate local route checks from network benchmarks, and avoid presenting a successful page render as proof of measurement accuracy.

## License and credits

Distributed under the [MIT license](LICENSE). Flask, Requests, speedtest-cli and external services retain their own licenses and terms.

