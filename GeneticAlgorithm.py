import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as intrp
from pymoo.core.problem import ElementwiseProblem
from pymoo.core.variable import Real, Integer, Choice

class optimize_design_pymoo(ElementwiseProblem):
    def __init__(self, **kwargs):
        vars = {
            "M_inlet": Real(bounds=(0.55, 0.65)),
            "AR_rotor": Real(bounds=(2, 5)),
            "AR_stator": Real(bounds=(2, 5)),
            "taper_rotor": Real(bounds=(0.5, 1.0)),
            "taper_stator": Real(bounds=(0.25, 1.0)),
            "n": Real(bounds=(0.2, 1.0)),
            "N_R": Integer(bounds=(20, 40)),
            "N_S": Integer(bounds=(20, 40)),
            "hub_tip_ratio": Real(bounds=(0.1, 0.4)),
            "methodology": Choice(options=['controlled vortex', 'free vortex']),
            "profile": Choice(options=['NACA-65', 'DCA']),
            "t_c_rotor": Integer(bounds=(6, 12)),
            "t_c_stator": Integer(bounds=(8, 12)),
        }

        super().__init__(vars=vars,
                         n_obj=3,
                         n_ieq_constr=8,
                         **kwargs)

    def _evaluate(self, X, out, *args, **kwargs):
        # input_vector = [Mach_inlet, AR_rotor, AR_stator, taper_rotor, taper_stator, n, N_R, N_S, hub_tip_ratio]

        design = Fan(Mach_inlet=X["M_inlet"], AR_rotor=X["AR_rotor"], AR_stator=X["AR_stator"],
                     taper_rotor=X["taper_rotor"], taper_stator=X["taper_stator"], n=X["n"], no_blades_rotor=X["N_R"],
                     no_blades_stator=X["N_S"], beta_tt=1.6, P0_cruise=39513.14, T0_cruise=250.13, mdot=80, omega=5000,
                     hub_tip_ratio=X["hub_tip_ratio"],gamma=1.4, R_air=287, eta_tt_estimated=0.9, row_chord_spacing_ratio=0.5,
                     lieblein_model=Lieblein_Model(), profile=X["profile"], methodology=X["methodology"], t_c_rotor=X["t_c_rotor"],
                     t_c_stator=X["t_c_stator"])

        # Objective functions
        obj1 = 1 - design.eta_tt_estimated  # Minimise (1 - eta_tt_estimated) / Maximise eta_tt_estimated
        obj2 = np.pi * design.r_tip ** 2  # Minimise frontal area
        obj3 = design.volume_value * design.titanium_blade_density  # Minimise weight

        # Constraints, default orientation of constraints being met is < 0
        const1 = max(design.delta_rotor) - 11
        const2 = max(design.delta_stator) - 11
        const3 = max(design.Mach_rotor) - 1.4
        const4 = max(design.solidity_rotor_distribution) - 1.6
        const5 = max(design.solidity_stator_distribution) - 1.6
        const6 = max(design.DF_rotor_distribution) - 0.6
        const7 = max(design.DF_stator_distribution) - 0.6
        const8 = design.max_stress_rotor - 880e6

        # const1 = np.abs(design.CV_residual_rotor) - 1e-6 # residual of C.Freeman CV should be smaller than 1e-6 to have design that does not have choking.
        # const2 = np.abs(design.CV_residual_stator) - 1e-6

        # Stacking Objectives to "F" and Constraints to "G"
        out["F"] = np.column_stack([obj1, obj2, obj3])
        out["G"] = np.column_stack([const1, const2, const3, const4, const5, const6, const7, const8])

# Optimiser Section of run_meanline.py
fan_optimisation_problem = ml.optimize_design_elementwise()

algorithm = MixedVariableGA(pop_size=1000, survival=RankAndCrowdingSurvival())
termination = get_termination("n_gen", 100)

result = minimize(problem=fan_optimisation_problem,
                  algorithm=algorithm,
                  termination=termination,
                  seed=1,
                  verbose=True)

X = result.X
F = result.F
print(X)
print(F)

def write_array_to_file(file_path, array):
    try:
        with open(file_path, 'w') as file:
            for item in array:
                file.write(str(item) + '\n')
        print("Array successfully written to", file_path)
    except Exception as e:
        print("Error occurred while writing to file:", str(e))


file_path_1 = "Variable_Optimisation_Output.txt"
file_path_2 = "Objective_Optimisation_Output.txt"
write_array_to_file(file_path_1, X)
write_array_to_file(file_path_2, F)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.scatter3D(1-F[:, 0], F[:, 1], F[:, 2])
ax.set_title("Pareto Front of Fan Optimisation")
ax.set_xlabel("Total to Total Efficiency [-]")
ax.set_ylabel("Frontal Area [m^2]")
ax.set_zlabel("Weight [kg]")
plt.show()