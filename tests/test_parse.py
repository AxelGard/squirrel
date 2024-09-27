from squirrel.squirrel import parse, read_file

def test_parse():
    _input_html = read_file("./tests/myweb/a.html")
    p = parse(_input_html)
    _expected_output = "<p> Hi from A file </p><h2> Hi from B html <h2><p> Hi after b file </p>".strip().replace("\n", " ").replace(" ", "") 
    assert p.strip().replace("\n", " ").replace(" ", "")  == _expected_output

