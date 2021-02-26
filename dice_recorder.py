#!/usr/bin/env python

import os
from csv import writer
from tqdm import tqdm

def record():
    with open("dice.csv", "+a", newline="") as f:
        csv_writer = writer(f)
        csv_writer.writerow(input("Input Row: ").split())
    os.system("clear")

if __name__ == "__main__":
    for x in tqdm(range(500)):
        record()
        pass
