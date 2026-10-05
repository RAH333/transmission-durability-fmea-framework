import pytest
from src.stress_solver import GearStressSolver

def test_stress_calculations():
    solver = GearStressSolver(torque_nm=200, face_width_mm=20, module=3)
    wt = solver.calculate_tangential_force(pitch_diameter_mm=60)
    assert wt == pytest.approx(6666.67, rel=1e-2)
    
    stress = solver.compute_bending_stress(wt_n=wt, y_form_factor=0.3)
    assert stress > 0

def test_invalid_parameters():
    solver = GearStressSolver(torque_nm=200, face_width_mm=0, module=3)
    with pytest.raises(ValueError):
        solver.compute_bending_stress(wt_n=5000, y_form_factor=0.3)
      
