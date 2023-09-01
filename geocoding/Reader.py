"""Read data from JSONlines format in ../data."""

from pathlib import Path

import jsonlines

ROOT = Path(__file__).parent.parent
DATAPATH = ROOT / "data"


class Reader:
    """Read data."""
    pass
