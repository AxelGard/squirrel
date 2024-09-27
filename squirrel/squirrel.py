#!/usr/bin/env python3
import sys
import os
import typing
from os import listdir
from os.path import isfile, join
import re


def read_file(f_path: str) -> str:
    with open(f_path, "r") as f:
        txt = f.read()
    return txt


def get_all_files_in_dir(path: str) -> typing.List[str]:
    return [f for f in listdir(path) if isfile(join(path, f))]


def write_to_file(to_file: str, text: str):
    with open(to_file, "w") as f:
        f.write(text)


def parse(html: str) -> str:
    pattern = r"\{\{(.*?)\}\}"
    for word in re.findall(pattern, html):
        if os.path.isfile(word) and ".html" in word:
            new_html = parse(read_file(word))
            html = html.replace("{{" + word + "}}", new_html)
    return html


def build(dir_path: str):
    assert os.path.isdir(dir_path), "build got a none dir path as argument"
    if dir_path[-1] != "/":
        dir_path += "/"
    build_path = "./build/"
    if not os.path.exists(build_path):
        os.makedirs(build_path)
    for file in get_all_files_in_dir(dir_path):
        p = parse(read_file(dir_path + file))
        write_to_file("./build/" + file, p)


if __name__ == "__main__":
    _argv = sys.argv
    assert len(_argv) > 1, "Needs path argument"
    assert os.path.isdir(_argv[1]), "Needs a exsting dir as argument"
    build(_argv[1])
