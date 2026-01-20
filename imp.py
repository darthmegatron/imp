#!/usr/bin/env python3

import sys
import os
from pathlib import Path

# --- AUTO-VENV MAGIC ---
# Check if we are running inside the venv. If not, restart!
def ensure_venv():
    # Get the path to the 'venv' folder in the root
    venv_python = Path(__file__).resolve().parent / "venv" / "bin" / "python3"
    
    # If the venv python exists, and we aren't already using it...
    if venv_python.exists() and sys.executable != str(venv_python):
        # Re-execute this script using the venv python
        os.execv(str(venv_python), [str(venv_python)] + sys.argv)

ensure_venv()
# -----------------------

# Add src to path
root_dir = Path(__file__).resolve().parent
sys.path.insert(0, str(root_dir / "src"))

import main

if __name__ == "__main__":
    main.main()
