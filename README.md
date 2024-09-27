# squirrel
A smiple way of build static website. 

<img src="./doc/squirrel.jpg" alt="drawing" style="width:300px;">

## install 

All that is needed is that `squirrel/squirrel.py` [file](https://github.com/AxelGard/squirrel/blob/master/squirrel/squirrel.py).
It only uses the standard lib from python. 
I would recomend a python version `=>3.8`. 


## usage 

```bash
python3 squirrel.py ./some/dir/with/html/files
```

In **a** file `./some/dir/with/html/files/a.html`
```html
<p> Hi from A file </p>
{{./some/dir/with/html/files/b.html}}
<p> Hi after B file </p>
```

In **b** file `./some/dir/with/html/files/b.html`
```html
<p> Hi from B file </p>
```

This will become: 

In **a** file `./build/a.html`

```html
<p> Hi from A file </p>
<p> Hi from B file </p>
<p> Hi after B file </p>
```
