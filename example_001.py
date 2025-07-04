
import pyvista as pv

cyl = pv.Cylinder()
arrow = pv.Arrow()
sphere = pv.Sphere()
plane = pv.Plane()
line = pv.Line()
box = pv.Box()
cone = pv.Cone()
poly = pv.Polygon()
disc = pv.Disc()

p = pv.Plotter(shape=(3, 3))
# Top row
p.subplot(0, 0)
p.add_mesh(cyl, color='lightblue', show_edges=True)
p.subplot(0, 1)
p.add_mesh(arrow, color='lightblue', show_edges=True)
p.subplot(0, 2)
p.add_mesh(sphere, color='lightblue', show_edges=True)
# Middle row
p.subplot(1, 0)
p.add_mesh(plane, color='lightblue', show_edges=True)
p.subplot(1, 1)
p.add_mesh(line, color='lightblue', line_width=3)
p.subplot(1, 2)
p.add_mesh(box, color='lightblue', show_edges=True)
# Bottom row
p.subplot(2, 0)
p.add_mesh(cone, color='lightblue', show_edges=True)
p.subplot(2, 1)
p.add_mesh(poly, color='lightblue', show_edges=True)
p.subplot(2, 2)
p.add_mesh(disc, color='lightblue', show_edges=True)
# Render all of them
p.show()