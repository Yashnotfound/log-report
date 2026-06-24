import json
from pathlib import Path

REPORT = Path("/app/report.json")


def load_report():
    return json.loads(REPORT.read_text())


def test_output_is_valid_json():
    """Criterion 1: /app/report.json exists and contains a single valid JSON object."""
    assert REPORT.exists(), "no /app/report.json found"
    assert isinstance(load_report(), dict), "report.json is not a JSON object"


def test_total_requests():
    """Criterion 2: total_requests equals the count of non-empty lines in access.log."""
    assert load_report()["total_requests"] == 6


def test_unique_ips():
    """Criterion 3: unique_ips equals the number of distinct client IPs."""
    assert load_report()["unique_ips"] == 3


def test_top_path():
    """Criterion 4: top_path equals the most frequently requested path."""
    assert load_report()["top_path"] == "/index.html"
