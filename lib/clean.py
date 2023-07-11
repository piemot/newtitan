from pathlib import Path
import shutil as sh
import os

DIST = Path("dist")


def run_clean(args):
    if os.path.exists(DIST):
        sh.rmtree(DIST)
