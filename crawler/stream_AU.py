#!/usr/bin/python3

from subprocess import Popen
import sys
from datetime import datetime
import argparse
import os


filename = "streamTwitter.py"

while True:
    parser = argparse.ArgumentParser(description='tweets crawler')
    process = Popen("python3 " + filename, shell=True)
    process.wait()
    print('error occur at ' + str(datetime.now()) + ' and is restarting now\n')
