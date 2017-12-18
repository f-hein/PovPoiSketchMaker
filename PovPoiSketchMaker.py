import cv2
import numpy as np
import sys
import datetime

def rgb2hex(r,g,b):
    if (r==0):
        if (g==0):
            hex = "0x{:02x}".format(b)
        else:
            hex = "0x{:02x}{:02x}".format(g, b)
    else:
        hex = "0x{:02x}{:02x}{:02x}".format(r,g,b)
    return hex

numberOfSlices = int(sys.argv[1])
ledNums = int(sys.argv[2])
pictures = sys.argv[3:]
print(pictures)
file = open('sketch.ino','w')
file.write("//File created by PPPC - Python POV POI Creator 0.1a\n"
           "//Author: Filip Hein\n"
           "//Date of creation: {}\n\n".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M")))
file.write("//---------------------\n"
           '#include "FastLED.h"\n'
           "#define DATA_PIN 7 //LEDs data pin\n"
           "#define CLOCK_PIN 14 //LEDs clock pin\n"
           "#define COLOR_ORDER BGR //Blue Green Red\n"
           "#define LED_TYPE APA102\n"
           "#define NUM_LEDS {} //number of LEDs in a strip\n\n".format(ledNums))
file.write("uint8_t buttonPin = 12;\n"
           "uint8_t buttonState = 0;\n"
           "uint8_t licznik = 0;\n"
           "uint8_t max_bright = 25; // Overall brightness. Changeable.\n"
           "struct CRGB leds[NUM_LEDS];\n"
           "int numberOfSlices = {};\n\n".format(numberOfSlices))
file.write("void setup(){\n delay(200);\n"
           " pinMode(buttonPin,INPUT);\n"
           " attachInterrupt(digitalPinToInterrupt(buttonPin),buttonPushed,RISING); //interrupt\n"
           " FastLED.addLeds<LED_TYPE, DATA_PIN, CLOCK_PIN, COLOR_ORDER>(leds, NUM_LEDS).setCorrection(TypicalPixelString);\n"
           " Serial.begin(9600); // For testing purposes\n"
           "}\n\n")


imageSize = (numberOfSlices, ledNums)
for i in range(len(pictures)):
    img = cv2.imread(pictures[i])
    resized = cv2.resize(img,imageSize, interpolation = cv2.INTER_AREA)
    x, y = resized.shape[:2]
    tablica = []

    for j in range(x):
        for k in range(y):
            tablica.append(rgb2hex(resized[j,k,0],resized[j,k,1],resized[j,k,2]))

    file.write("const unsigned int {}[] = ".format(pictures[i].split(".")[0])+"{")
    for i in range(len(tablica)):
        file.write(' {},'.format(tablica[i]))
    file.write('};\n')

file.write("\nvoid loop(){\n"
           " for (int x=0;x<numberOfSlices;x++){\n"
           "  for(int counter=0;counter<NUM_LEDS;counter++){\n"
           "    leds[counter]=ergebe[counter+NUM_LEDS*x];\n"
           "  }\n }\n}\n")

file.write("\nvoid buttonPushed(){ //interrupt handler\n"
           " static unsigned long lastTime;\n"
           " unsigned long timeNow = millis();\n"
           " if (timeNow - lastTime < 50)\n"
           "  return;\n"
           " licznik++;\n"
           " lastTime = timeNow;\n}\n")
file.close()




