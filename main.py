#!/usr/bin/env python3
"""
Entry for make.fun's "Sum up 19 November's world news in one image".

The repository holds the finished front-page image as entry.png (drawn by
draw-frontpage.py, kept in the project workspace and in the build
transcripts). This program's only job is to deliver those exact bytes to
the output location, using nothing but the Python standard library, so it
runs identically in any sandbox: no network, no third-party packages, and
the same bytes on every run.
"""
import os
import shutil


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        out_dir = "/output" if os.path.isdir("/output") else here
    out = os.path.join(out_dir, "entry.png")

    if os.path.abspath(src) != os.path.abspath(out):
        shutil.copyfile(src, out)
    print("wrote", out)


if __name__ == "__main__":
    main()
