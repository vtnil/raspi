#!/usr/bin/env python
 
# Import required libraries
import time
import RPi.GPIO as GPIO
import sys
 
if len(sys.argv) <2:
  exit();
else:
  turn=sys.argv[1]
# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)
 
# Define GPIO signals to use
# GPIO24,GPIO25,GPIO8,GPIO7
StepPins = [17,27,22,23]
 
# Set all pins as output
for pin in StepPins:
  print ";Setup pins";
  GPIO.setup(pin,GPIO.OUT)
  GPIO.output(pin, False)
 
# Define some settings
StepCounter = 0
WaitTime = 0.1 if len(sys.argv)<3 else float(sys.argv[2])
 
# Define simple sequence
StepCount = 4
Seqr = []
Seqr = range(0, StepCount)
Seqr[0] = [1,0,0,0]
Seqr[1] = [0,1,0,0]
Seqr[2] = [0,0,1,0]
Seqr[3] = [0,0,0,1]
 
Seql = []
Seql = range(0, StepCount)
Seql[0] = [0,0,0,1]
Seql[1] = [0,0,1,0]
Seql[2] = [0,1,0,0]
Seql[3] = [1,0,0,0]
 
# Define advanced sequence
# as shown in manufacturers datasheet
#StepCount2 = 8
#Seq2 = []
#Seq2 = range(0, StepCount2)
#Seq2[0] = [1,0,0,0]
#Seq2[1] = [1,1,0,0]
#Seq2[2] = [0,1,0,0]
#Seq2[3] = [0,1,1,0]
#Seq2[4] = [0,0,1,0]
#Seq2[5] = [0,0,1,1]
#Seq2[6] = [0,0,0,1]
#Seq2[7] = [1,0,0,1]
 
# Choose a sequence to use
if turn == 'l':
  Seq=Seql
elif turn == 'r':
  Seq=Seqr
else: 
  exit()
StepCount = StepCount
 
# Start main loop
while 1==1:
 
  for pin in range(0, 4):
    xpin = StepPins[pin]
    step = StepCounter % StepCount
    if Seq[step][pin]!=0:
      #print " Step %i Enable %i" %(StepCounter,xpin)
      GPIO.output(xpin, True)
    else:
      GPIO.output(xpin, False)
 
  StepCounter += 1
 
  # Wait before moving on
  time.sleep(WaitTime)
  if StepCounter % 10 == 0:
    print "Step %i" % StepCounter
