import os, sys
from squirrel import build_dir, build_file

if __name__ == "__main__":
    _argv = sys.argv
    assert len(_argv) > 1, "Needs path argument"
    if os.path.isdir(_argv[1]):
        build_dir(_argv[1])
    elif os.path.isdir(_argv[1]):
        build_file(_argv[1])
    else: 
        raise ValueError("Needs a file or a dir as an argument")
