#!/usr/bin/python3

import os
import sys
import requests
from tqdm import tqdm

modes = []
operation = "G"

for arg in sys.argv:
    if arg.startswith("-"):
        for letter in arg:
            if letter == "x":
                modes.append("EXEC")
            elif letter == "G":
                operation = "G"
            elif letter == "P":
                operation = "P"
            elif letter == "n":
                modes.append("No-Perma-Save")
            elif letter == "H":
                print("GetRaw Download Manager")
                print("Args:")
                print("-G: Set Operation to GET")
                print("-P: Set Operation to POST")
                print("-x: Execute a File after downloading")
                print("-n: Remove the File after Downloading via -x")
    else:
        url = arg   

chunk_size = 1024

if operation == "G":
    r = requests.get(url)
else:
    r = requests.post(url)

with open(url.split("/")[-1],"wb") as f:
    for data in tqdm(r.iter_content(chunk_size)):
        f.write(data)

for arg in modes:
    if arg == "EXEC":
        os.system(url.split("/")[-1])
    if arg == "No-Perma-Save":
        os.remove(url.split("/")[-1])
