import pyvista as pv
import numpy as np

L = 0.5        # λ/2
radius = 0.005 # 절연선 반경(λ)

p0 = np.array([0, 0, -L/2])
p1 = np.array([0, 0,  L/2])

cylinder = pv.Cylinder(center=(0,0,0),
                       direction=(0,0,1),
                       radius=radius,
                       height=L)

mesh = pv.wrap(cylinder)
mesh.save("dipole.stl")   # FDTD/FEM용 내보내기
mesh.plot(line_width=3)
