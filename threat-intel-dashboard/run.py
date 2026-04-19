#!/usr/bin/env python3
"""
Entry point for Threat Intel Dashboard.
Runs src/app.py from the correct working directory so relative imports
and config path resolution (../config.yaml) work as expected.
"""

import subprocess
import sys
import os

if __name__ == '__main__':
    src_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src')
    subprocess.run([sys.executable, 'app.py'], cwd=src_dir)
