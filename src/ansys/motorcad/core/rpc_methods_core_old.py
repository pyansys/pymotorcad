"""Contains all the JSON-RPC API calls for Motor-CAD with the old CamelCase function names.

For backwards compatibility.
Not for direct use. Inherited by
"""
from sys import _getframe
from warnings import warn

from ansys.motorcad.core.rpc_methods_core import _RpcMethodsCore
from ansys.motorcad.core.rpc_methods_internal import _RpcMethodsInternal


def deprecation_warning(old_name, new_name):
    """Output deprecation warning for old method names."""
    warn(
        "Function: " + old_name + " is deprecated and has been replaced by: " + new_name + "."
        "\nThis function will be removed in version.....",
        DeprecationWarning,
    )


class _RpcMethodsCoreOld:
    def __init__(self, mc_connection):
        self.new_methods = _RpcMethodsCore(mc_connection)
        self.internal_methods = _RpcMethodsInternal(mc_connection)

    # ------------------------------------ Variables ------------------------------------
    def GetArrayVariable_2d(self, *args):
        replacement_function = self.new_methods.get_array_variable_2d
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def SetArrayVariable_2d(self, *args):
        replacement_function = self.new_methods.set_array_variable_2d
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def RestoreCompatibilitySettings(self):
        replacement_function = self.new_methods.restore_compatibility_settings
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function()

    def GetVariable(self, *args):
        replacement_function = self.new_methods.get_variable
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def GetArrayVariable(self, *args):
        replacement_function = self.new_methods.get_array_variable
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def SetVariable(self, *args):
        replacement_function = self.new_methods.set_variable
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def SetArrayVariable(self, *args):
        replacement_function = self.new_methods.set_array_variable
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    # ------------------------------------ UI ------------------------------------

    def IsStopRequested(self):
        replacement_function = self.internal_methods.is_stop_requested
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function()

    def DisableErrorMessages(self, *args):
        replacement_function = self.new_methods.disable_error_messages
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def GetMessages(self, *args):
        replacement_function = self.new_methods.get_messages
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def UpdateInterface(self):
        replacement_function = self.internal_methods.update_interface
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function()

    def InitialiseTabNames(self):
        replacement_function = self.new_methods.initialise_tab_names
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function()

    def SaveMotorCADScreenToFile(self, *args):
        replacement_function = self.new_methods.save_motorcad_screen_to_file
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def GetLicence(self):
        replacement_function = self.new_methods.get_license
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function()

    def SetVisible(self, *args):
        replacement_function = self.new_methods.set_visible
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def AvoidImmediateUpdate(self, *args):
        replacement_function = self.internal_methods.avoid_immediate_update
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def ClearMessageLog(self):
        replacement_function = self.new_methods.clear_message_log
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function()

    def ShowMessage(self, *args):
        replacement_function = self.new_methods.show_message
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def showmessage(self, *args):
        replacement_function = self.new_methods.show_message
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def ShowMagneticContext(self):
        replacement_function = self.new_methods.show_magnetic_context
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function()

    def ShowMechanicalContext(self):
        replacement_function = self.new_methods.show_mechanical_context
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function()

    def ShowThermalContext(self):
        replacement_function = self.new_methods.show_thermal_context
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function()

    def DisplayScreen(self, *args):
        replacement_function = self.new_methods.display_screen
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def Quit(self):
        replacement_function = self.new_methods.quit
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function()

    def set_free(self):
        replacement_function = self.new_methods.set_free
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function()

    def SaveScreenToFile(self, *args):
        replacement_function = self.new_methods.save_screen_to_file
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    # ------------------------------------ Files ------------------------------------

    def LoadDutyCycle(self, *args):
        replacement_function = self.new_methods.load_duty_cycle
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def SaveDutyCycle(self, *args):
        replacement_function = self.new_methods.save_duty_cycle
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def ExportMatrices(self, *args):
        replacement_function = self.new_methods.export_matrices
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def LoadCustomDriveCycle(self, *args):
        replacement_function = self.new_methods.load_custom_drive_cycle
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def LoadFEAResult(self, *args):
        replacement_function = self.new_methods.load_fea_result
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def ExportToAnsysElectronicsDesktop(self, *args):
        replacement_function = self.new_methods.export_to_ansys_electronics_desktop
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def ExportResults(self, *args):
        replacement_function = self.new_methods.export_results
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def LoadDXFFile(self, *args):
        replacement_function = self.new_methods.load_dxf_file
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def CreateReport(self, *args):
        replacement_function = self.new_methods.create_report
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def LoadReportStructure(self, *args):
        replacement_function = self.new_methods.load_report_structure
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def ExportForceAnimation(self, *args):
        replacement_function = self.new_methods.export_force_animation
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def LoadReportTree(self):
        replacement_function = self.new_methods.load_report_tree
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function()

    def LoadTemplate(self, *args):
        replacement_function = self.new_methods.load_template
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def SaveTemplate(self, *args):
        replacement_function = self.new_methods.save_template
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def LoadWindingPattern(self, *args):
        replacement_function = self.new_methods.load_winding_pattern
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def SaveWindingPattern(self, *args):
        replacement_function = self.new_methods.save_winding_pattern
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def ExportMultiForceData(self, *args):
        replacement_function = self.new_methods.export_multi_force_data
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def GeometryExport(self):
        replacement_function = self.new_methods.geometry_export
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function()

    def ExportToAnsysDiscovery(self, *args):
        replacement_function = self.new_methods.export_to_ansys_discovery
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def ExportNVHResultsData(self, *args):
        replacement_function = self.new_methods.export_nvh_results_data
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def LoadFromFile(self, *args):
        replacement_function = self.new_methods.load_from_file
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def SaveToFile(self, *args):
        replacement_function = self.new_methods.save_to_file
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    # ------------------------------------ Internal Scripting ------------------------------------

    def SaveScript(self, *args):
        replacement_function = self.new_methods.save_script
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def LoadScript(self, *args):
        replacement_function = self.new_methods.load_script
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def RunScript(self):
        replacement_function = self.new_methods.run_script
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function()

    # ------------------------------------ Calculations ------------------------------------

    def ClearDutyCycle(self):
        replacement_function = self.new_methods.clear_duty_cycle
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function()

    def DoMagneticThermalCalculation(self):
        replacement_function = self.new_methods.do_magnetic_thermal_calculation
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function()

    def GetIMIronLoss(self, *args):
        replacement_function = self.internal_methods.get_im_iron_loss
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def Set3DComponentVisibility(self, *args):
        replacement_function = self.new_methods.set_3d_component_visibility
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def SetAllEmagCalculations(self, *args):
        replacement_function = self.internal_methods.set_all_emag_calculations
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def CalculateSaturationMap(self):
        replacement_function = self.new_methods.calculate_saturation_map
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function()

    def CalculateTorqueEnvelope(self):
        replacement_function = self.new_methods.calculate_torque_envelope
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function()

    def SaveResults(self, *args):
        replacement_function = self.new_methods.save_results
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def LoadResults(self, *args):
        replacement_function = self.new_methods.load_results
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def CalculateIMSaturationModel(self):
        replacement_function = self.new_methods.calculate_im_saturation_model
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function()

    def CalculateForceHarmonics_Spatial(self):
        replacement_function = self.new_methods.calculate_force_harmonics_spatial
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function()

    def CalculateForceHarmonics_Temporal(self):
        replacement_function = self.new_methods.calculate_force_harmonics_temporal
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function()

    def GetForceFrequencyDomainAmplitude(self, *args):
        replacement_function = self.new_methods.get_force_frequency_domain_amplitude
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def UpdateForceAnalysisResults(self, *args):
        replacement_function = self.new_methods.update_force_analysis_results
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def DoMultiForceCalculation(self):
        replacement_function = self.new_methods.do_multi_force_calculation
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function()

    def DoSteadyStateAnalysis(self):
        replacement_function = self.new_methods.do_steady_state_analysis
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function()

    def DoTransientAnalysis(self):
        replacement_function = self.new_methods.do_transient_analysis
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function()

    def DoMagneticCalculation(self):
        replacement_function = self.new_methods.do_magnetic_calculation
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function()

    def DoWeightCalculation(self):
        replacement_function = self.new_methods.do_weight_calculation
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function()

    def DoMechanicalCalculation(self):
        replacement_function = self.new_methods.do_mechanical_calculation
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function()

    # ------------------------------------ Lab ------------------------------------

    def CalculateTestPerformance_Lab(self):
        replacement_function = self.new_methods.calculate_test_performance_lab
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function()

    def ExportDutyCycle_Lab(self):
        replacement_function = self.new_methods.export_duty_cycle_lab
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function()

    def GetModelBuilt_Lab(self):
        replacement_function = self.new_methods.get_model_built_lab
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function()

    def ShowResultsViewer_Lab(self, *args):
        replacement_function = self.new_methods.show_results_viewer_lab
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def ExportFigure_Lab(self, *args):
        replacement_function = self.new_methods.export_figure_lab
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def CalculateGenerator_Lab(self):
        replacement_function = self.new_methods.calculate_generator_lab
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function()

    def LoadExternalModel_Lab(self, *args):
        replacement_function = self.new_methods.load_external_model_lab
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def ClearModelBuild_Lab(self):
        replacement_function = self.new_methods.clear_model_build_lab
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function()

    def SetMotorLABContext(self):
        replacement_function = self.new_methods.set_motorlab_context
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function()

    def BuildModel_Lab(self):
        replacement_function = self.new_methods.build_model_lab
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function()

    def CalculateOperatingPoint_Lab(self):
        replacement_function = self.new_methods.calculate_operating_point_lab
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function()

    def CalculateMagnetic_Lab(self):
        replacement_function = self.new_methods.calculate_magnetic_lab
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function()

    def CalculateThermal_Lab(self):
        replacement_function = self.new_methods.calculate_thermal_lab
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function()

    def CalculateDutyCycle_Lab(self):
        replacement_function = self.new_methods.calculate_duty_cycle_lab
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function()

    # ------------------------------------ Geometry ------------------------------------

    def SetWindingCoil(self, *args):
        replacement_function = self.new_methods.set_winding_coil
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def GetWindingCoil(self, *args):
        replacement_function = self.new_methods.get_winding_coil
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def CheckIfGeometryIsValid(self, *args):
        replacement_function = self.new_methods.check_if_geometry_is_valid
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    # ------------------------------------ Graphs ------------------------------------

    def LoadMagnetisationCurves(self, *args):
        replacement_function = self.new_methods.load_magnetisation_curves
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def SaveMagnetisationCurves(self, *args):
        replacement_function = self.new_methods.save_magnetisation_curves
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def GetMagneticGraphPoint(self, *args):
        replacement_function = self.new_methods.get_magnetic_graph_point
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def GetTemperatureGraphPoint(self, *args):
        replacement_function = self.new_methods.get_temperature_graph_point
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def GetPowerGraphPoint(self, *args):
        replacement_function = self.new_methods.get_power_graph_point
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def GetMagnetic3DGraphPoint(self, *args):
        replacement_function = self.new_methods.get_magnetic_3d_graph_point
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def GetFEAGraphPoint(self, *args):
        replacement_function = self.new_methods.get_fea_graph_point
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    # ------------------------------------ FEA ------------------------------------

    def SetPowerInjectionValue(self, *args):
        replacement_function = self.new_methods.set_power_injection_value
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def SetFixedTemperatureValue(self, *args):
        replacement_function = self.new_methods.set_fixed_temperature_value
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def ClearFixedTemperatureValue(self, *args):
        replacement_function = self.new_methods.clear_fixed_temperature_value
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def DoSlotFiniteElement(self):
        replacement_function = self.new_methods.do_slot_finite_element
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function()

    def ClearAllData(self):
        replacement_function = self.new_methods.clear_all_data
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function()

    def AddLine_XY(self, *args):
        replacement_function = self.new_methods.add_line_xy
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def SetBndCond(self, *args):
        replacement_function = self.internal_methods.set_bnd_cond
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def StoreProblemData(self, *args):
        replacement_function = self.internal_methods.store_problem_data
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def Add_Region_Thermal_A(self, *args):
        replacement_function = self.internal_methods.add_region_thermal_a
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def AddPoint_XY(self, *args):
        replacement_function = self.internal_methods.add_point_xy
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def CreateOptimisedMesh(self):
        replacement_function = self.new_methods.create_optimised_mesh
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function()

    def CreateOptimisedMesh_Thermal(self, *args):
        replacement_function = self.internal_methods.create_optimised_mesh_thermal
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def SetMeshGeneratorParam(self, *args):
        replacement_function = self.internal_methods.set_mesh_generator_param
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def SolveProblem(self):
        replacement_function = self.internal_methods.solve_problem
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function()

    def Add_Region_Thermal(self, *args):
        replacement_function = self.internal_methods.add_region_thermal
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def AddCircularConductor_A(self, *args):
        replacement_function = self.internal_methods.add_circular_conductor_a
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def AddRectangularConductor_A(self, *args):
        replacement_function = self.internal_methods.add_rectangular_conductor_a
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def AddArc_XY(self, *args):
        replacement_function = self.new_methods.add_arc_xy
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def SetRegionColour(self, *args):
        replacement_function = self.internal_methods.set_region_colour
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def AddPoint_RT(self, *args):
        replacement_function = self.internal_methods.add_point_rt
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def AddLine_RT(self, *args):
        replacement_function = self.new_methods.add_line_rt
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def AddArc_RT(self, *args):
        replacement_function = self.new_methods.add_arc_rt
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def AddArc_Boundary_RT(self, *args):
        replacement_function = self.new_methods.add_arc_boundary_rt
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def AddArc_Boundary_XY(self, *args):
        replacement_function = self.new_methods.add_arc_boundary_xy
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def AddLine_Boundary_RT(self, *args):
        replacement_function = self.new_methods.add_line_boundary_rt
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def AddLine_Boundary_XY(self, *args):
        replacement_function = self.new_methods.add_line_boundary_xy
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def InitiateGeometryFromScript(self):
        replacement_function = self.new_methods.initiate_geometry_from_script
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function()

    def AddPoint_Magnetic_RT(self, *args):
        replacement_function = self.new_methods.add_point_magnetic_rt
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def AddPoint_Magnetic_XY(self, *args):
        replacement_function = self.new_methods.add_point_magnetic_xy
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def AddArc_CentreStartEnd_RT(self, *args):
        replacement_function = self.new_methods.add_arc_centre_start_end_rt
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def AddArc_CentreStartEnd_XY(self, *args):
        replacement_function = self.new_methods.add_arc_centre_start_end_xy
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def SetFEAPathPoint(self, *args):
        replacement_function = self.new_methods.set_fea_path_point
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def SetFEAPathArc(self, *args):
        replacement_function = self.new_methods.set_fea_path_arc
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def SetFEAPathLine(self, *args):
        replacement_function = self.new_methods.set_fea_path_line
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def SaveFEAData(self, *args):
        replacement_function = self.new_methods.save_fea_data
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def AddPoint_CustomMaterial_XY(self, *args):
        replacement_function = self.new_methods.add_point_custom_material_xy
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def GetRegionValue(self, *args):
        replacement_function = self.new_methods.get_region_value
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def GetRegionLoss(self, *args):
        replacement_function = self.new_methods.get_region_loss
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def EditMagnetRegion(self, *args):
        replacement_function = self.new_methods.edit_magnet_region
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def AddRegion_XY(self, *args):
        replacement_function = self.new_methods.add_region_xy
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def AddRegion_RT(self, *args):
        replacement_function = self.new_methods.add_region_rt
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def DeleteRegions(self, *args):
        replacement_function = self.new_methods.delete_regions
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def ResetRegions(self):
        replacement_function = self.new_methods.reset_regions
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function()

    def AddMagnetRegion_RT(self, *args):
        replacement_function = self.new_methods.add_magnet_region_rt
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def AddMagnetRegion_XY(self, *args):
        replacement_function = self.new_methods.add_magnet_region_xy
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def GetPointValue(self, *args):
        replacement_function = self.new_methods.get_point_value
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    # ------------------------------------ Thermal ------------------------------------

    def SetResistanceValue(self, *args):
        replacement_function = self.new_methods.set_resistance_value
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def SetResistanceMultiplier(self, *args):
        replacement_function = self.new_methods.set_resistance_multiplier
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def ClearExternalCircuit(self):
        replacement_function = self.new_methods.clear_external_circuit
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function()

    def CreateNewNode(self, *args):
        replacement_function = self.new_methods.create_new_node
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def ModifyNode(self, *args):
        replacement_function = self.new_methods.modify_node
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def SetCapacitanceValue(self, *args):
        replacement_function = self.new_methods.set_capacitance_value
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def SetPowerSourceValue(self, *args):
        replacement_function = self.new_methods.set_power_source_value
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def LoadExternalCircuit(self, *args):
        replacement_function = self.new_methods.load_external_circuit
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def SaveExternalCircuit(self, *args):
        replacement_function = self.new_methods.save_external_circuit
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def SaveTransientPowerValues(self, *args):
        replacement_function = self.new_methods.save_transient_power_values
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def SaveTransientTemperatures(self, *args):
        replacement_function = self.new_methods.save_transient_temperatures
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def RemoveExternalComponent(self, *args):
        replacement_function = self.new_methods.remove_external_component
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def GetNodeTemperature(self, *args):
        replacement_function = self.new_methods.get_node_temperature
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def GetNodeCapacitance(self, *args):
        replacement_function = self.new_methods.get_node_capacitance
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def GetNodePower(self, *args):
        replacement_function = self.new_methods.get_node_power
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def GetNodeToNodeResistance(self, *args):
        replacement_function = self.new_methods.get_node_to_node_resistance
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def GetNodeExists(self, *args):
        replacement_function = self.new_methods.get_node_exists
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def GetOffsetNodeNumber(self, *args):
        replacement_function = self.new_methods.get_offset_node_number
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    # ------------------------------------ Materials ------------------------------------

    def SetFluid(self, *args):
        replacement_function = self.new_methods.set_fluid
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def SetComponentMaterial(self, *args):
        replacement_function = self.new_methods.set_component_material
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def GetComponentMaterial(self, *args):
        replacement_function = self.new_methods.get_component_material
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def ImportSolidMaterial(self, *args):
        replacement_function = self.new_methods.import_solid_material
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def ExportSolidMaterial(self, *args):
        replacement_function = self.new_methods.export_solid_material
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def DeleteSolidMaterial(self, *args):
        replacement_function = self.new_methods.delete_solid_material
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def CalculateIronLossCoefficients(self, *args):
        replacement_function = self.new_methods.calculate_iron_loss_coefficients
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def SaveIronLossCoefficients(self, *args):
        replacement_function = self.new_methods.save_iron_loss_coefficients
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def CalculateMagnetParameters(self, *args):
        replacement_function = self.new_methods.calculate_magnet_parameters
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)

    def SaveMagnetParameters(self, *args):
        replacement_function = self.new_methods.save_magnet_parameters
        deprecation_warning(_getframe().f_code.co_name, replacement_function.__name__)
        return replacement_function(*args)
