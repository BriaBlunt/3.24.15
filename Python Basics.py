#Dim arrStart, arrEnd
#arrStart = Rhino.GetPoint("Start of line")
#If IsArray(arrStart) Then
#arrEnd = Rhino.GetPoint("End of line")
#If IsArray(arrEnd) Then
#Rhino.AddLine arrStart, arrEnd
#End If
#End If



import rhinoscriptsyntax as rs
import random

#rs.AddLine ( [6,7,8], [12,13,14] )

#pointArray = [ (0,0,0), (4,0,0), (4,5,0), (0,5,0), (0,0,6), (4,0,6), (4,5,6), (0,5,6) ]
#rs.AddBox ( pointArray )

#Points = rs.GetPoints(True, True, "Select points")
#rs.AddPoints ( Points )

#print (random.uniform (0,100))
#print (random.randint (0,100))
#print (random.random ())

for i in range(0,10):

    #x = random.uniform(0,10)
    #y = random.uniform(0,10)
    #z = random.uniform(0,10)

    #x = 9
    #y = 4
    #z = 8


    #r = random.randint(0,255)
    #g = random.randint(0,255)
    #b = random.randint(0,255)

    #color = [r,g,b]

    #pt = rs.AddPoint(x,y,z)
    #rs.ObjectColor(pt, color)


    a = random.randint(0,10)
    b = random.randint(0,10)
    c = random.randint(0,10)

    d = random.randint(0,10)
    e = random.randint(0,10)
    f = random.randint(0,10)

    start = [a,b,c]
    end = [d,e,f]


    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    color = [r,g,b]

    line = rs.AddLine(start, end)
    rs.ObjectColor(line, color)
