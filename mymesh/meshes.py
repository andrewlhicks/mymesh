import gmsh

def CreateShellMesh():
    # inner and outer radius
    r1 = 0.8
    r2 = 1
    # center of outer circle
    x = 0
    y = 0
    z = 0
    # center of the inner circle
    x1 = 0
    y1 = 0
    z1 = 0.1
    ndens = 0.02
    gmsh.initialize()
    gmsh.model.add('ShellMesh')

    # add points for outer shell
    gmsh.model.geo.addPoint(x, y, z, ndens, 1)
    gmsh.model.geo.addPoint(x+r2, y, z, ndens, 2)
    gmsh.model.geo.addPoint(x-r2, y, z, ndens, 3)
    gmsh.model.geo.addPoint(x, y+r2, z, ndens, 4)
    gmsh.model.geo.addPoint(x, y-r2, z, ndens, 5)
    gmsh.model.geo.addPoint(x, y, z+r2, ndens, 6)
    gmsh.model.geo.addPoint(x, y, z-r2, ndens, 7)

    # add circles for outer shell
    gmsh.model.geo.addCircleArc(2, 1, 4, 1)
    gmsh.model.geo.addCircleArc(4, 1, 3, 2)
    gmsh.model.geo.addCircleArc(3, 1, 5, 3)
    gmsh.model.geo.addCircleArc(5, 1, 2, 4)
    gmsh.model.geo.addCircleArc(2, 1, 6, 5)
    gmsh.model.geo.addCircleArc(6, 1, 3, 6)
    gmsh.model.geo.addCircleArc(3, 1, 7, 7)
    gmsh.model.geo.addCircleArc(7, 1, 2, 8)
    gmsh.model.geo.addCircleArc(4, 1, 6, 9)
    gmsh.model.geo.addCircleArc(6, 1, 5, 10)
    gmsh.model.geo.addCircleArc(5, 1, 7, 11)
    gmsh.model.geo.addCircleArc(7, 1, 4, 12)

    gmsh.model.geo.addCurveLoop([2, 7, 12], 1)
    gmsh.model.geo.addSurfaceFilling([1], 1)

    gmsh.model.geo.addCurveLoop([2, -6, -9], 2)
    gmsh.model.geo.addSurfaceFilling([2], 2)

    gmsh.model.geo.addCurveLoop([3, -10, 6], 3)
    gmsh.model.geo.addSurfaceFilling([3], 3)

    gmsh.model.geo.addCurveLoop([3, 11, -7], 4)
    gmsh.model.geo.addSurfaceFilling([4], 4)

    gmsh.model.geo.addCurveLoop([4, -8, -11], 5)
    gmsh.model.geo.addSurfaceFilling([5], 5)

    gmsh.model.geo.addCurveLoop([4, 5, 10], 6)
    gmsh.model.geo.addSurfaceFilling([6], 6)

    gmsh.model.geo.addCurveLoop([1, 9, -5], 7)
    gmsh.model.geo.addSurfaceFilling([7], 7)

    gmsh.model.geo.addCurveLoop([1, -12, 8], 8)
    gmsh.model.geo.addSurfaceFilling([8], 8)

    gmsh.model.geo.addPoint(x1, y1, z1, ndens, 14)
    gmsh.model.geo.addPoint(x1+r1, y1, z1, ndens, 8)
    gmsh.model.geo.addPoint(x1-r1, y1, z1, ndens, 9)
    gmsh.model.geo.addPoint(x1, y1+r1, z1, ndens, 10)
    gmsh.model.geo.addPoint(x1, y1-r1, z1, ndens, 11)
    gmsh.model.geo.addPoint(x1, y1, z1+r1, ndens, 12)
    gmsh.model.geo.addPoint(x1, y1, z1-r1, ndens, 13)

    gmsh.model.geo.addCircleArc(8, 14, 10, 13)
    gmsh.model.geo.addCircleArc(10, 14, 9, 14)
    gmsh.model.geo.addCircleArc(9, 14, 11, 15)
    gmsh.model.geo.addCircleArc(11, 14, 8, 16)
    gmsh.model.geo.addCircleArc(8, 14, 12, 17)
    gmsh.model.geo.addCircleArc(12, 14, 9, 18)
    gmsh.model.geo.addCircleArc(9, 14, 13, 19)
    gmsh.model.geo.addCircleArc(13, 14, 8, 20)
    gmsh.model.geo.addCircleArc(10, 14, 12, 21)
    gmsh.model.geo.addCircleArc(12, 14, 11, 22)
    gmsh.model.geo.addCircleArc(11, 14, 13, 23)
    gmsh.model.geo.addCircleArc(13, 14, 10, 24)

    gmsh.model.geo.addCurveLoop([14, 19, 24], 9)
    gmsh.model.geo.addSurfaceFilling([9], 9)

    gmsh.model.geo.addCurveLoop([14, -18, -21], 10)
    gmsh.model.geo.addSurfaceFilling([10], 10)

    gmsh.model.geo.addCurveLoop([15, -22, 18], 11)
    gmsh.model.geo.addSurfaceFilling([11], 11)

    gmsh.model.geo.addCurveLoop([15, 23, -19], 12)
    gmsh.model.geo.addSurfaceFilling([12], 12)

    gmsh.model.geo.addCurveLoop([16, -20, -23], 13)
    gmsh.model.geo.addSurfaceFilling([13], 13)

    gmsh.model.geo.addCurveLoop([16, 17, 22], 14)
    gmsh.model.geo.addSurfaceFilling([14], 14)

    gmsh.model.geo.addCurveLoop([13, 21, -17], 15)
    gmsh.model.geo.addSurfaceFilling([15], 15)

    gmsh.model.geo.addCurveLoop([13, -24, 20], 16)
    gmsh.model.geo.addSurfaceFilling([16], 16)

    gmsh.model.geo.addSurfaceLoop([1, 2, 3, 4, 5, 6, 7, 8], 1)
    gmsh.model.geo.addSurfaceLoop([9, 10, 11, 12, 13, 14, 15, 16], 2)
    gmsh.model.geo.addVolume([1, 2], 1)

    gmsh.model.geo.synchronize()

    gmsh.model.geo.addPhysicalGroup(2, [1, 2, 3, 4, 5, 6, 7, 8], 101)
    gmsh.model.geo.addPhysicalGroup(2, [9, 10, 11, 12, 13, 14, 15, 16], 102)
    gmsh.model.geo.addPhysicalGroup(3, [1], 103)

    gmsh.model.mesh.generate(3)

    gmsh.write('ShellMesh.msh')
    
    gmsh.finalize()
