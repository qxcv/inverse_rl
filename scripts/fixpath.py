"""Fix the Python library path so that it uses this thing's inverse_rl
module. Import this from the other scripts to make them work."""

import sys
import os

this_path = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../inverse_rl/'))
assert os.path.isdir(this_path)
sys.path.insert(0, this_path)
