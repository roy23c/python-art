

# Python Art

Collection of experiments using python to generate art 

## Getting Started

### Prerequisites
```
Python 3
```

### Installing and Running

Steps for setting up the various .py files

#### angle-art.py

The program will draw lines with increasing length. An input angle will change the direction the line is drawn. Each line color is a randomly generated RGB image.

<img src="https://github.com/roycechung/python-art/blob/master/examples/line-art_01.png" width="50%">
<img src="https://github.com/roycechung/python-art/blob/master/examples/line-art_02.png" width="50%">

run angle-art by typing the following command into terminal

```
python3 line-art.py 
```

draw_specific_pattern will draw a pattern with a specified angle and number of lines 

```
draw_specific_pattern(angle, iterations)
```
draw_random_pattern will draw a pattern with a random angle 

```
draw_random_pattern()
```

