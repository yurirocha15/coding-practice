#!/usr/bin/env python

import glob
import subprocess

"""
Run all python files recursively
"""

if __name__ == "__main__":
    for file in glob.iglob("./src/**/*.py"):
        print(f"Running {file}...")
        process = subprocess.Popen(
            ["python " + file], stdout=subprocess.PIPE, shell=True
        )
        out, err = process.communicate()
