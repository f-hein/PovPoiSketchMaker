# Python POV Poi Creator
Python script creating an Arduino sketch for POV poi. Example of POV poi may be found here: https://www.youtube.com/watch?v=5-xLDVILtMY
General purpose of this script was to automate writing Arduino code and not copy-pasting every picture's array.

Advantages of the script:
* Easy to use
* Intuitive
* Automates the process of writing POV poi software
* Compatible with Python2.x and Python3.x

### How to use PPPC
Simply download pictures you want to display on your device (they must be in *.bmp* extension), run the script (python PovPoiSketchMaker.py), provide the number of LEDs and number of slices, finally add paths to pictures as arguments.
Example of use:

*python PovPoiSketchMaker.py 150 72 mario.png biohazard.png*

X - 150 - how wide the picture has to be

Y - 70 - how tall the picture has to be (number of LEDs in your poi)


### How does it work

The script takes every picture user provided separately, rescales it to X by Y picture, reads RGB values from every pixel, 
converts it to hexadecimal number, and then adds it to the array named after the filename. The display algorithm itself in loop() runs perfectly fine.

Finally, the file sketch.ino is created in the script's directory. All you have to do is to make sure that everything matches your
expectations, and then you are ready to upload this sketch into your Arduino.

### What the user may have to change manually?

* Data, clock and button pins
* Color order (BGR is for APA102 LED strip)
* Maximum brightness (0-255)
* Button functionality
* How a program cycles through picture arrays
