"""Check for the 2026-10-27 --list-values fix. Run from the repo root:
python3 tests/test_list_values_2026_10_27.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "scripts"))
import query_unctad_excel as q
cases = [
    ("SECTOR", "Tertiary - E - Water supply; sewerage, waste management and remediation activities",
     ["Tertiary - E - Water supply; sewerage, waste management and remediation activities"]),
    ("SECTOR", "Tertiary - F - Construction;\nTertiary - L - Real estate activities",
     ["Tertiary - F - Construction", "Tertiary - L - Real estate activities"]),
    ("ARBITRATORS", "Pinto, M. - President; Bull, C. - Claimant",
     ["Pinto, M. - President", "Bull, C. - Claimant"]),
    ("COMMITTEE", "King, B. D.;\nMoreno Rodríguez, J. A.", ["King, B. D.", "Moreno Rodríguez, J. A."]),
    ("LIVE_CHECK", "status pending/unknown at snapshot; follow-on proceeding pending at snapshot",
     ["status pending/unknown at snapshot", "follow-on proceeding pending at snapshot"]),
]
bad = 0
for key, v, want in cases:
    got = q.split_field(key, v)
    print(("PASS" if got == want else "FAIL"), key, got)
    bad += got != want
print(f"{bad} failure(s)"); sys.exit(1 if bad else 0)
