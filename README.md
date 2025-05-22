# SCADA Web Application

This repository contains a minimal example of a web-based SCADA application
implemented using only the Python standard library. It simulates sensor data and
serves a dashboard page that updates in real time using Server-Sent Events (SSE).

## Running the application

```
python3 -m scada_app.server
```

Then open `http://localhost:8000` in a browser.

## Testing

The tests can be run with `python3 -m pytest`.
