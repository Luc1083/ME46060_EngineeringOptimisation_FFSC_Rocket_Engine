import time
import numpy as np
import matplotlib.pyplot as plt
import cycles as RC
import pyfluids

# def compare2variables(var1, var2, P_var):
#
# def compare1variable(var1):

# Start timer
start = time.time()

# # Explore Effect of OF Ratio on IspSea_real
# OF = np.arange(1, 5.1, 0.1)
# ISP = np.zeros_like(OF)
#
# for i in range(len(OF)):
#     Engine = RC.FFSC_LRE(OF=OF[i], oxidizer=pyfluids.FluidsList.Oxygen, fuel=pyfluids.FluidsList.Methane,
#                          fuel_CEA_name="CH4(L)", oxidizer_CEA_name="O2(L)", T_oxidizer=80, T_fuel=100, P_oxidizer=4,
#                          P_fuel=4, eta_isotropic_OP=0.87, eta_isotropic_FP=0.84,
#                          eta_polytropic_OT=0.9, eta_polytropic_FT=0.9, eta_FPB=0.99, eta_OPB=0.99, eta_cstar=0.99,
#                          eta_isp=0.95, Ps_Pt_FT=0.9, Ps_Pt_OT=0.9, dP_over_Pinj_CC=0.15, dP_over_Pinj_OPB=0.15,
#                          dP_over_Pinj_FPB=0.15, CR_CC=2.5, CR_FPB=4, CR_OPB=4, eps_CC=35, mdot_film_over_mdot_fuel=0.05,
#                          cooling_channels_pressure_drop=190, cooling_channels_temperature_rise=100,
#                          axial_velocity_OT=200,
#                          axial_velocity_FT=300, mdot_total_0=710, mdot_crossflow_ox_over_mdot_ox_0=0.075,
#                          mdot_crossflow_f_over_mdot_f_0=0.045, dP_FP_0=880, dP_OP_0=690, mode="analysis")
#     ISP[i] = Engine.CP.IspSea_real
#
# plt.plot(OF, ISP)
# plt.xlabel("OF")
# plt.ylabel("ISP [s]")
# plt.show()
# #
# # Explore Effect of mdot_total_0 on IspSea_real
# mdot = np.arange(500, 900, 5)
# ISP = np.zeros_like(mdot)
#
# for i in range(len(mdot)):
#     Engine = RC.FFSC_LRE(OF=3.4, oxidizer=pyfluids.FluidsList.Oxygen, fuel=pyfluids.FluidsList.Methane,
#                          fuel_CEA_name="CH4(L)", oxidizer_CEA_name="O2(L)", T_oxidizer=80, T_fuel=100, P_oxidizer=4,
#                          P_fuel=4, eta_isotropic_OP=0.87, eta_isotropic_FP=0.84,
#                          eta_polytropic_OT=0.9, eta_polytropic_FT=0.9, eta_FPB=0.99, eta_OPB=0.99, eta_cstar=0.99,
#                          eta_isp=0.95, Ps_Pt_FT=0.9, Ps_Pt_OT=0.9, dP_over_Pinj_CC=0.15, dP_over_Pinj_OPB=0.15,
#                          dP_over_Pinj_FPB=0.15, CR_CC=2.5, CR_FPB=4, CR_OPB=4, eps_CC=35, mdot_film_over_mdot_fuel=0.05,
#                          cooling_channels_pressure_drop=190, cooling_channels_temperature_rise=100,
#                          axial_velocity_OT=200,
#                          axial_velocity_FT=300, mdot_total_0=mdot[i], mdot_crossflow_ox_over_mdot_ox_0=0.075,
#                          mdot_crossflow_f_over_mdot_f_0=0.045, dP_FP_0=880, dP_OP_0=690, mode="analysis")
#     ISP[i] = Engine.CP.IspSea_real
#
# plt.plot(mdot, ISP)
# plt.xlabel("Mass Flow")
# plt.ylabel("ISP [s]")
# plt.show()

# # Initialise variables OF, MDOT & engine performance arrays
# OFc = np.arange(2.5, 4, 0.1)
# mdotc = np.arange(600, 800, 20)
# ISPc = np.zeros((len(mdotc), len(OFc)))
# Thrust = np.zeros((len(mdotc), len(OFc)))
#
# for i in range(len(mdotc)):
#     for j in range(len(OFc)):
#         Engine = RC.FFSC_LRE(
#             OF=OFc[j], oxidizer=pyfluids.FluidsList.Oxygen, fuel=pyfluids.FluidsList.Methane,
#             fuel_CEA_name="CH4(L)", oxidizer_CEA_name="O2(L)", T_oxidizer=80, T_fuel=100, P_oxidizer=4,
#             P_fuel=4, eta_isotropic_OP=0.87, eta_isotropic_FP=0.84,
#             eta_polytropic_OT=0.9, eta_polytropic_FT=0.9, eta_FPB=0.99, eta_OPB=0.99, eta_cstar=0.99,
#             eta_isp=0.95, Ps_Pt_FT=0.9, Ps_Pt_OT=0.9, dP_over_Pinj_CC=0.15, dP_over_Pinj_OPB=0.15,
#             dP_over_Pinj_FPB=0.15, CR_CC=2.5, CR_FPB=4, CR_OPB=4, eps_CC=35, mdot_film_over_mdot_fuel=0.05,
#             cooling_channels_pressure_drop=190, cooling_channels_temperature_rise=100,
#             axial_velocity_OT=200, axial_velocity_FT=300, mdot_total_0=mdotc[i],
#             mdot_crossflow_ox_over_mdot_ox_0=0.075, mdot_crossflow_f_over_mdot_f_0=0.045,
#             dP_FP_0=880, dP_OP_0=690, mode="analysis"
#         )
#         ISPc[i, j] = Engine.CP.IspSea_real
#         Thrust[i, j] = Engine.CP.ThrustSea
#
# # Create meshgrid for contour plot
# OFc_grid, mdotc_grid = np.meshgrid(OFc, mdotc)
#
# # Contour plot of ISP with OF & MDOT variation
# plt.figure(figsize=(10, 6))
# levels = np.linspace(np.min(ISPc), np.max(ISPc), 20)  # Adjust levels based on ISPc range
# contour = plt.contourf(OFc_grid, mdotc_grid, ISPc, levels=levels, cmap='viridis')
# plt.colorbar(contour, label='ISP')
# plt.xlabel('OFc')
# plt.ylabel('mdotc')
# plt.title('Contour Plot of ISP vs OFc and mdotc')
# plt.show()
#
# # Contour plot of Thrust with OF & MDOT variation
# plt.figure(figsize=(10, 6))
# levels = np.linspace(np.min(Thrust), np.max(Thrust), 20)  # Adjust levels based on ISPc range
# contour = plt.contourf(OFc_grid, mdotc_grid, Thrust, levels=levels, cmap='viridis')
# plt.colorbar(contour, label='Thrust')
# plt.xlabel('OFc')
# plt.ylabel('mdotc')
# plt.title('Contour Plot of Thrust vs OFc and mdotc')
# plt.show()

# Initialise variables mdot_crossflow & engine performance arrays
mdot_crossflow_ox = np.arange(0.03, 0.2, 0.005)
mdot_crossflow_f = np.arange(0.03, 0.1, 0.005)
ISPc = np.zeros((len(mdot_crossflow_ox), len(mdot_crossflow_f)))
Thrust = np.zeros((len(mdot_crossflow_ox), len(mdot_crossflow_f)))
T_FPB = np.zeros((len(mdot_crossflow_ox), len(mdot_crossflow_f)))
T_OPB = np.zeros((len(mdot_crossflow_ox), len(mdot_crossflow_f)))

for i in range(len(mdot_crossflow_ox)):
    for j in range(len(mdot_crossflow_f)):
        Engine = RC.FFSC_LRE(
            OF=3.4, oxidizer=pyfluids.FluidsList.Oxygen, fuel=pyfluids.FluidsList.Methane,
            fuel_CEA_name="CH4(L)", oxidizer_CEA_name="O2(L)", T_oxidizer=80, T_fuel=100, P_oxidizer=4,
            P_fuel=4, eta_isotropic_OP=0.87, eta_isotropic_FP=0.84,
            eta_polytropic_OT=0.9, eta_polytropic_FT=0.9, eta_FPB=0.99, eta_OPB=0.99, eta_cstar=0.99,
            eta_isp=0.95, Ps_Pt_FT=0.9, Ps_Pt_OT=0.9, dP_over_Pinj_CC=0.15, dP_over_Pinj_OPB=0.15,
            dP_over_Pinj_FPB=0.15, CR_CC=2.5, CR_FPB=4, CR_OPB=4, eps_CC=35, mdot_film_over_mdot_fuel=0.05,
            cooling_channels_pressure_drop=190, cooling_channels_temperature_rise=100,
            axial_velocity_OT=200, axial_velocity_FT=300, mdot_total_0=700,
            mdot_crossflow_ox_over_mdot_ox_0=mdot_crossflow_ox[i],
            mdot_crossflow_f_over_mdot_f_0=mdot_crossflow_f[j],
            dP_FP_0=880, dP_OP_0=690, mode="analysis"
        )
        ISPc[i, j] = Engine.CP.IspSea_real
        Thrust[i, j] = Engine.CP.ThrustSea
        if Engine.CP.FPB_products.Tt > 1100:
            T_FPB[i, j] = 0
        if Engine.CP.FPB_products.Tt < 1100:
            T_FPB[i, j] = 1
        if Engine.CP.OPB_products.Tt > 1100:
            T_OPB[i, j] = 0
        if Engine.CP.OPB_products.Tt < 1100:
            T_OPB[i, j] = 1

# Create meshgrid for contour plot
mdot_crossflow_f_grid, mdot_crossflow_ox_grid = np.meshgrid(mdot_crossflow_f, mdot_crossflow_ox)

# Contour plot of ISP with crossflow variables variation
plt.figure(figsize=(10, 6))
levels = np.linspace(np.min(ISPc), np.max(ISPc), 20)  # Adjust levels based on ISPc range
contour = plt.contourf(mdot_crossflow_f_grid, mdot_crossflow_ox_grid, ISPc, levels=levels, cmap='viridis')
plt.colorbar(contour, label='ISP')
plt.xlabel('mdot_crossflow_f_over_mdot_f_0')
plt.ylabel('mdot_crossflow_ox_over_mdot_ox_0')
plt.title('Contour Plot of ISP vs mdot_crossflow_f and mdot_crossflow_ox')

# Overlay the regions where T_FPB or T_OPB are 0 with a light red color
mask = (T_FPB == 0) | (T_OPB == 0)
plt.contourf(mdot_crossflow_f_grid, mdot_crossflow_ox_grid, mask, levels=[0.5, 1], colors='red', alpha=0.3)

plt.show()

# # Contour plot of Thrust with crossflow variables variation
# plt.figure(figsize=(10, 6))
# levels = np.linspace(np.min(Thrust), np.max(Thrust), 20)  # Adjust levels based on Thrust range
# contour = plt.contourf(mdot_crossflow_ox_grid, mdot_crossflow_f_grid, Thrust, levels=levels, cmap='viridis')
# plt.colorbar(contour, label='Thrust')
# plt.xlabel('mdot_crossflow_ox_over_mdot_ox_0')
# plt.ylabel('mdot_crossflow_f_over_mdot_f_0')
# plt.title('Contour Plot of Thrust vs mdot_crossflow_ox and mdot_crossflow_f')
# plt.show()
#
# # Initialise variables dP_FP, dP_OP & engine performance arrays
# dP_FP = np.arange(600, 900, 20)
# dP_OP = np.arange(500, 800, 20)
# ISPc = np.zeros((len(dP_FP), len(dP_OP)))
# Thrust = np.zeros((len(dP_FP), len(dP_OP)))
#
# for i in range(len(dP_FP)):
#     for j in range(len(dP_OP)):
#         Engine = RC.FFSC_LRE(
#             OF=3.4, oxidizer=pyfluids.FluidsList.Oxygen, fuel=pyfluids.FluidsList.Methane,
#             fuel_CEA_name="CH4(L)", oxidizer_CEA_name="O2(L)", T_oxidizer=80, T_fuel=100, P_oxidizer=4,
#             P_fuel=4, eta_isotropic_OP=0.87, eta_isotropic_FP=0.84,
#             eta_polytropic_OT=0.9, eta_polytropic_FT=0.9, eta_FPB=0.99, eta_OPB=0.99, eta_cstar=0.99,
#             eta_isp=0.95, Ps_Pt_FT=0.9, Ps_Pt_OT=0.9, dP_over_Pinj_CC=0.15, dP_over_Pinj_OPB=0.15,
#             dP_over_Pinj_FPB=0.15, CR_CC=2.5, CR_FPB=4, CR_OPB=4, eps_CC=35, mdot_film_over_mdot_fuel=0.05,
#             cooling_channels_pressure_drop=190, cooling_channels_temperature_rise=100,
#             axial_velocity_OT=200, axial_velocity_FT=300, mdot_total_0=700,
#             mdot_crossflow_ox_over_mdot_ox_0=0.075,
#             mdot_crossflow_f_over_mdot_f_0=0.045,
#             dP_FP_0=dP_FP[i],  # Varying dP_FP
#             dP_OP_0=dP_OP[j],  # Varying dP_OP
#             mode="analysis"
#         )
#         ISPc[i, j] = Engine.CP.IspSea_real
#         Thrust[i, j] = Engine.CP.ThrustSea
#
# # Create meshgrid for contour plot
# dP_FP_grid, dP_OP_grid = np.meshgrid(dP_FP, dP_OP)
#
# # Contour plot of ISP with dP_FP and dP_OP variation
# plt.figure(figsize=(10, 6))
# levels = np.linspace(np.min(ISPc), np.max(ISPc), 20)  # Adjust levels based on ISPc range
# contour = plt.contourf(dP_FP_grid, dP_OP_grid, ISPc, levels=levels, cmap='viridis')
# plt.colorbar(contour, label='ISP')
# plt.xlabel('dP_FP')
# plt.ylabel('dP_OP')
# plt.title('Contour Plot of ISP vs dP_FP and dP_OP')
# plt.show()
#
# # Contour plot of Thrust with dP_FP and dP_OP variation
# plt.figure(figsize=(10, 6))
# levels = np.linspace(np.min(Thrust), np.max(Thrust), 20)  # Adjust levels based on Thrust range
# contour = plt.contourf(dP_FP_grid, dP_OP_grid, Thrust, levels=levels, cmap='viridis')
# plt.colorbar(contour, label='Thrust')
# plt.xlabel('dP_FP')
# plt.ylabel('dP_OP')
# plt.title('Contour Plot of Thrust vs dP_FP and dP_OP')
# plt.show()

# Stop timer
finish = time.time()

# Calculate runtime
runtime = finish - start

# Print runtime
print(f"The program took {runtime:.2f} seconds to run.")