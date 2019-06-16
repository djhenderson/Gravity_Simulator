# Gravity Simulator
Albin Jaldevik's (albinjal) attempt at simulating gravity via
classical mechanics and specifically
[Newtons law of universal gravitation](https://en.wikipedia.org/wiki/Newton%27s_law_of_universal_gravitation):

![](https://wikimedia.org/api/rest_v1/media/math/render/svg/48f74b3b4d591ba1996c4d481f74ac3ab7e279d7)

Forked with additions and updates by Doug Henderson (djhenderson).

## Example
Earth and Moon 28,6 Days

![Earth and Moon](/moon_and_earth.gif)

This Gif shows a simulated trip for the moon (orange) around the earth (blue).
The red vector shows the direction of the applied force
while the blue one shows the velocity of the object.

**Config :**
Frames: 686,
Seconds/Frame: 3600 (1 Hour / Frame),

**Objects:**

| Data   | Earth              | Moon          | Unit          |
| ------ |:------------------:| ----------:   | ------------- |
| X-Pos  | 0                  | 0             | meter         |
| Y-Pos  | 0                  | 369671000     | meter         |
| X-Vel  | 0                  |    1082       | meter/second  |
| Y-Vel  | 0                  |    0          | meter/second  |
| Mass   | 5.9722 * 10 ** 24  |7.3 * 10 ** 22 | kilogram      |


## Run ##
1. Clone this repo
2. Make sure your python env has the required dependencies,
   otherwise install with pip install <Package>
    * imageio
    * typing
    * matplotlib
3. Configure setting and indata in Simulation.py
4. Run Simulation.py with: Python3 Simulation.py
5. Simulation gif should be in the "Gifs" folder

This project was made to practice object oriented programming in Python.
