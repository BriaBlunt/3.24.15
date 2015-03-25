#WHAT IS RANDOM??
#Example of how to randomize variables

import rhinoscriptsyntax as rs
import random

for i in range(0,10):

    a = random.randint (0,10)
    b = random.randint (0,10)
    c = 0


    VectorStart = (a,b,c)
    VectorEnd = (60,60,60)

    r = random.randint(0,255)
    b = random.randint(0,255)
    g = random.randint(0,255)
    color = [r,g,b]

    #vector = rs.VectorCreate(Vector1, Vector2)


    vector = rs.VectorCreate(VectorEnd, VectorStart)
    #vector = rs.VectorUnitize(vector)
    #vector = rs.VectorScale(vector, 5)
    line = rs.AddLine(VectorStart, vector)

    rs.ObjectColor (line, color)



print (vector)
