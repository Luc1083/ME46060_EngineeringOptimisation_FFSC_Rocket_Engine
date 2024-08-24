import time
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
import cycles as RC
import pyfluids

# Define Optimization Function
def UnconstrainedWithPenalty(x):

    penalty = 0

    Engine = RC.FFSC_LRE(OF=x[0], oxidizer=pyfluids.FluidsList.Oxygen, fuel=pyfluids.FluidsList.Methane,
                                                  fuel_CEA_name="CH4(L)", oxidizer_CEA_name="O2(L)", T_oxidizer=80, T_fuel=100, P_oxidizer=4,
                                                  P_fuel=4, eta_isotropic_OP=0.87, eta_isotropic_FP=0.84,
                                                  eta_polytropic_OT=0.9, eta_polytropic_FT=0.9, eta_FPB=0.99, eta_OPB=0.99, eta_cstar=0.99,
                                                  eta_isp=0.95, Ps_Pt_FT=0.9, Ps_Pt_OT=0.9, dP_over_Pinj_CC=0.15, dP_over_Pinj_OPB=0.15,
                                                  dP_over_Pinj_FPB=0.15, CR_CC=2.5, CR_FPB=4, CR_OPB=4, eps_CC=35, mdot_film_over_mdot_fuel=0.05,
                                                  cooling_channels_pressure_drop=190, cooling_channels_temperature_rise=100,
                                                  axial_velocity_OT=200,
                                                  axial_velocity_FT=300, mdot_total_0=x[1], mdot_crossflow_ox_over_mdot_ox_0=x[2],
                                                  mdot_crossflow_f_over_mdot_f_0=x[3], dP_FP_0=x[4], dP_OP_0=x[5], mode="analysis")

    ISP = Engine.CP.IspSea_real
    T_FPB = Engine.CP.FPB_products.Tt
    T_OPB = Engine.CP.OPB_products.Tt
    Thrust = Engine.CP.ThrustSea

    if T_OPB > 1100:
        penalty += 1000
    if T_FPB > 1100:
        penalty += 1000

    ISP.append(ISP)
    obj_history.append(ISP + penalty)

    return ISP + penalty


# Start timer
start = time.time()

# Start Optimization

ISP = []
obj_history = []

result = sp.optimize.minimize(UnconstrainedWithPenalty, [2.5, 600, 0.005, 0.005, 600, 600], method='Nelder-Mead', tol=1e-6)

plt.xlabel("Iteration no. [-]")
plt.ylabel("Objective [kg]")
plt.plot(range(result.nfev),obj_history)
plt.tight_layout()
plt.show()

plt.xlabel("Iteration no. [-]")
plt.ylabel("Objective [kg]")
plt.plot(range(a.nfev), ISP)
plt.tight_layout()
plt.show()






