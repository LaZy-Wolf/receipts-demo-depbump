from pkgreport import latest_version, report, summarize

RECORD = {"name": "requests", "versions": ["2.9.0", "2.10.0"], "size": 2048, "share": 0.4, "released": "2026-09-01T12:00:00Z"}


def test_latest_version_uses_pep440_order():
    assert latest_version(["1.9", "1.10", "1.10rc1"]) == "1.10"


def test_summarize():
    line = summarize(RECORD)
    assert line.startswith("requests 2.10.0: 2.0 KB, ")
    assert line.endswith(" of downloads, released 2026-09-01")


def test_report_sorted_by_share():
    small = dict(RECORD, name="tiny", share=0.01)
    assert report([small, RECORD]).splitlines()[0].startswith("requests")
