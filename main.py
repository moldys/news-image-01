#!/usr/bin/env python3
"""news-image-01 entry: copy the pre-rendered news collage to /output/entry.png.

The image (entry.png) is a 1024x1024 editorial front page summarising the world
news of Friday 13 November 2026: the Nvidia CEO resignation, the FAA ground stop,
Iran-U.S. tensions, the U.S. midterm results, the Russia-Ukraine prisoner
exchange and the New Orleans boat rescue.
"""
import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
OUT = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.png")
# ensure the output directory exists before copying
os.makedirs(os.path.dirname(OUT), exist_ok=True)
shutil.copyfile(SRC, OUT)
print("wrote", OUT)
