import sys
import os 
import typing
from os import listdir
from os.path import isfile, join


def read_file(f_path:str) -> str:
    with open(f_path, "r") as f: 
        txt = f.read()
    return txt

def get_all_files_in_dir(path:str) -> typing.List[str]:
    return [f for f in listdir(path) if isfile(join(path, f))]

def write(to_file:str):
    pass 

def parse(html:str)->str:
    html = html.replace("\n", " ").replace("  ", " ")
    repl = None 
    found = None
    for word in html.split(" "):
        if word == "": continue
        if "{{" in word and "}}" in word: 
            found = word
            word = word.replace("{", "").replace("}","")
            if os.path.isfile(word) and ".html" in word: 
                word = parse(read_file(word))
                repl = f"\n{word}\n" 
                html.replace(found, repl)
    return html


def build(dir_path:str):
    assert os.path.isdir(dir_path), "build got a none dir path as argument"
    if dir_path[-1] != "/":
        dir_path += "/"
    for file in get_all_files_in_dir(dir_path):
        p = parse(read_file(dir_path + file))
        if "a." in file:
            print(p)

if __name__ == "__main__":
    _argv = sys.argv
    assert len(_argv) > 1, "Needs path argument"
    assert os.path.isdir(_argv[1]), "Needs a exsting dir as argument"
    build(_argv[1])


