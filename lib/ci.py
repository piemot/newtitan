from sys import argv
from lib.build import run_build

if __name__ == "__main__":
    run_build({"version": argv[1], "export": "Titan"})
