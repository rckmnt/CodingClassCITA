# GhPython code meant to live inside Grasshopper

import Rhino

perpPlane = []
sectionsOut = []
floorCrvsOut = []
loft = []

length = path.Domain[1]             # get length of the curve
stepSize = length/(num-1)           # divide length to get step size

rotate = Rhino.Geometry.Transform.Rotation(r, cnt)
sectionPlane = Rhino.Geometry.Plane(cnt, Rhino.Geometry.Vector3d(0,0,1))

for i in range(num):
    section.Transform(rotate)       #rotate profile input
    
    transCrv = section.Duplicate()  # create new curve to rotate
    
    framePlane = path.PerpendicularFrameAt(stepSize*i)[1]   # get planes to orient to
    
    #perpPlane.append(framePlane)    # viz purposes only
    
    orient = Rhino.Geometry.Transform.PlaneToPlane(sectionPlane, framePlane)
    
    transCrv.Transform(orient)       # orient rotated curve
    sectionsOut.append(transCrv)    # send to output
    
    floorCrvsOut.append(Rhino.Geometry.Intersect.Intersection.CurvePlane(transCrv, floorPlane, 0.01))

# LOFT CROSS SECTIONS

start = Rhino.Geometry.Curve.PointAtEnd.GetValue(path)
end = Rhino.Geometry.Curve.PointAtStart.GetValue(path)

loft.append(Rhino.Geometry.Brep.CreateFromLoft(sectionsOut, start, end, 0, 0))

print floorCrvsOut