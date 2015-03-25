#WHAT IS RANDOM??
#Example of how to randomize variables

import rhinoscriptsyntax as rs
import random

for i in range(0,10):

    a = random.randint (0,10)
    b = random.randint (0,10)
    c = 0

    StartPoint = (a,b,c)
    NewVecEnd = (40,40,40)
    NewVecStart = (0,0,0)
    origin = StartPoint

    r = random.randint(0,255)
    b = random.randint(0,255)
    g = random.randint(0,255)
    color = [r,g,b]

    vector = rs.VectorCreate(NewVecEnd, NewVecStart)
    line = rs.AddLine(StartPoint, vector)
    #line = rs.ScaleObject(line, origin, (0.5,0.5,0.5))

    rs.ObjectColor (line, color)
    rs.DivideCurveLength(line,9)

print (vector)
