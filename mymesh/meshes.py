import gmsh

def CreateShellMesh(inner_center=[0,0,0], inner_radius=0.8, outer_radius=1.0, mesh_size=0.02, path='mesh.msh'):
    # inner and outer radius
    r1 = inner_radius
    r0 = outer_radius

    # center of outer circle
    x0 = 0
    y0 = 0
    z0 = 0

    # center of the inner circle
    x1 = inner_center[0]
    y1 = inner_center[1]
    z1 = inner_center[2]

    # node density
    ndens = mesh_size

    # initialize
    gmsh.initialize()

    # get mesh name from path
    filename = path.split('/')[-1]
    if filename[-4:] != '.msh':
        raise ValueError
    name = filename[:-4]

    # set up model
    gmsh.model.add(name)

    # add points for outer shell
    gmsh.model.geo.addPoint(x0, y0, z0, ndens, 1)
    gmsh.model.geo.addPoint(x0+r0, y0, z0, ndens, 2)
    gmsh.model.geo.addPoint(x0-r0, y0, z0, ndens, 3)
    gmsh.model.geo.addPoint(x0, y0+r0, z0, ndens, 4)
    gmsh.model.geo.addPoint(x0, y0-r0, z0, ndens, 5)
    gmsh.model.geo.addPoint(x0, y0, z0+r0, ndens, 6)
    gmsh.model.geo.addPoint(x0, y0, z0-r0, ndens, 7)

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

    # add surfaces for outer shell
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

    # add points for inner shell
    gmsh.model.geo.addPoint(x1, y1, z1, ndens, 14)
    gmsh.model.geo.addPoint(x1+r1, y1, z1, ndens, 8)
    gmsh.model.geo.addPoint(x1-r1, y1, z1, ndens, 9)
    gmsh.model.geo.addPoint(x1, y1+r1, z1, ndens, 10)
    gmsh.model.geo.addPoint(x1, y1-r1, z1, ndens, 11)
    gmsh.model.geo.addPoint(x1, y1, z1+r1, ndens, 12)
    gmsh.model.geo.addPoint(x1, y1, z1-r1, ndens, 13)

    # add circles for inner shell
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

    # add surfaces for inner shell
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

    # add surface loops and volume
    gmsh.model.geo.addSurfaceLoop([1, 2, 3, 4, 5, 6, 7, 8], 1)
    gmsh.model.geo.addSurfaceLoop([9, 10, 11, 12, 13, 14, 15, 16], 2)
    gmsh.model.geo.addVolume([1, 2], 1)

    # must synchronize in order to properly generate mesh
    gmsh.model.geo.synchronize()

    # add physical groups
    gmsh.model.addPhysicalGroup(2, [1, 2, 3, 4, 5, 6, 7, 8], 101)
    gmsh.model.addPhysicalGroup(2, [9, 10, 11, 12, 13, 14, 15, 16], 102)
    gmsh.model.addPhysicalGroup(3, [1], 103)

    # generate 3d mesh
    gmsh.model.mesh.generate(3)

    # write to disk
    gmsh.write(path)
    
    # done
    gmsh.finalize()