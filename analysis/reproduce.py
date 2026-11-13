"""Synthetic demonstration only."""
import csv
from pathlib import Path
p = Path(__file__).resolve().parents[1] / "data/synthetic.csv"
with p.open() as f:
    assert all(int(r["y"]) == 2 * int(r["x"]) for r in csv.DictReader(f))
print("SYNTHETIC CHECK PASS")
