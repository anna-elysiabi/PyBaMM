import pybamm
import numpy as np

# load model
model = pybamm.lithium_ion.SPMe()

# create geometry
geometry = model.default_geometry

# load parameter values and process model and geometry
param = model.default_parameter_values
param.process_model(model)
param.process_geometry(geometry)

# set mesh
mesh = pybamm.Mesh(geometry, model.default_submesh_types, model.default_var_pts)

# discretise model
disc = pybamm.Discretisation(mesh, model.default_spatial_methods)
disc.process_model(model)

# solve model
t_eval1 = np.linspace(0, 0.2, 100)
solution1 = model.default_solver.solve(model, t_eval1)

# process vars
solution1 = model.default_solver.solve(model, t_eval1)
voltage1 = pybamm.ProcessedVariable(
    model.variables["Terminal voltage [V]"], solution1.t, solution1.y, mesh=mesh
)
current1 = pybamm.ProcessedVariable(
    model.variables["Terminal voltage [V]"], solution1.t, solution1.y, mesh=mesh
)

# solve again
model.concatenated_initial_conditons = solution1.y[:,-1][:,np.newaxis]
t_eval2 = np.linspace(solution1.t[-1], 1, 100)
solution2 = model.default_solver.solve(model, t_eval2)
voltage2 = pybamm.ProcessedVariable(
    model.variables["Terminal voltage [V]"], solution2.t, solution2.y, mesh=mesh
)
current2 = pybamm.ProcessedVariable(
    model.variables["Terminal voltage [V]"], solution2.t, solution2.y, mesh=mesh
)




# plot
plot = pybamm.QuickPlot(model, mesh, solution)
plot.dynamic_plot()
