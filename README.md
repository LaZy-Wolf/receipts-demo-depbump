# receipts-demo-depbump

`pkgreport` turns package release records into the lines of our weekly platform report.

It uses three libraries, and only these functions from them:

| Library | Functions used |
| --- | --- |
| `python-dateutil` | `dateutil.parser.isoparse` |
| `packaging` | `packaging.version.parse` |
| `receipts-demo-fmtlib` | `fmtlib.human_bytes`, `fmtlib.percent` |

Dependencies are pinned in `requirements.txt`.

## Development

```bash
pip install -r requirements-dev.txt
pytest
```
