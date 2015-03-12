#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import sys

led = 21
buzzer = 23
freq = 900

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(buzzer, GPIO.OUT)

LONG = 0.3
SHORT = 0.1
PAUSE_SYMBOL = SHORT
PAUSE_CHAR = LONG


morseDict = dict()
morseDict['A'] = [SHORT, LONG]
morseDict['B'] = [LONG, SHORT, SHORT, SHORT]
morseDict['C'] = [LONG, SHORT, LONG, SHORT]
morseDict['D'] = [LONG, SHORT, SHORT]
morseDict['E'] = [SHORT]
morseDict['F'] = [SHORT, SHORT, LONG, SHORT]
morseDict['G'] = [LONG, LONG, SHORT]
morseDict['H'] = [SHORT, SHORT, SHORT, SHORT]
morseDict['I'] = [SHORT, SHORT]
morseDict['J'] = [SHORT, LONG, LONG, LONG]
morseDict['K'] = [LONG, SHORT, LONG]
morseDict['L'] = [SHORT, LONG, SHORT, SHORT]
morseDict['M'] = [LONG, LONG]
morseDict['N'] = [LONG, SHORT]
morseDict['O'] = [LONG, LONG, LONG]
morseDict['P'] = [SHORT, LONG, LONG, SHORT]
morseDict['Q'] = [LONG, LONG, SHORT, LONG]
morseDict['R'] = [SHORT, LONG, SHORT]
morseDict['S'] = [SHORT, SHORT, SHORT]
morseDict['T'] = [LONG]
morseDict['U'] = [SHORT, SHORT, LONG]
morseDict['V'] = [SHORT, SHORT, SHORT, LONG]
morseDict['W'] = [SHORT, LONG, LONG]
morseDict['X'] = [LONG, SHORT, SHORT, LONG]
morseDict['Y'] = [LONG, SHORT, LONG, LONG]
morseDict['Z'] = [LONG, LONG, SHORT, SHORT]

p = GPIO.PWM(buzzer, freq)  # channel=pin frequency=freq


def outputSound(c):
	
	for i in morseDict[c]:
		p.start(1)
		time.sleep(i)
		p.stop()
		time.sleep(PAUSE_SYMBOL)
	
	time.sleep(PAUSE_CHAR)


def outputLed(c):
	
	for i in morseDict[c]:
		GPIO.output(led, True)
		time.sleep(i)
		GPIO.output(led, False)
		time.sleep(PAUSE_SYMBOL)
	
	time.sleep(PAUSE_CHAR)



def outputLedAndSound(c):
	
	for i in morseDict[c]:
		GPIO.output(led, True)
		p.start(1)
		time.sleep(i)
		GPIO.output(led, False)
		p.stop()
		time.sleep(PAUSE_SYMBOL)
	
	time.sleep(PAUSE_CHAR)

while 1 :
	
	print 'Inserisci la parola che vuoi venga emessa in codice morse'
	input = sys.stdin.readline().upper()

	for c in input:
		if c in morseDict:
			outputLedAndSound(c)