"""
This script models analytical gear stresses (AGMA-derived logic) to evaluate transmission build configurations against structural safety margins.
"""
import numpy as np

class GearStressSolver:
    """
    Analytical evaluation tool for transmission gear bending and contact stresses.
    Assists in validation before physical DVP testing.
    """
    def __init__(self, torque_nm, face_width_mm, module):
        self.torque = torque_nm          # Tangential driving force component metric
        self.b = face_width_mm           # Face width
        self.m = module                  # Gear module (mm)
        
    def calculate_tangential_force(self, pitch_diameter_mm):
        """Calculates tangential load on the tooth."""
        if pitch_diameter_mm <= 0:
            raise ValueError("Pitch diameter must be greater than zero.")
        return (2.0 * self.torque * 1000.0) / pitch_diameter_mm

    def compute_bending_stress(self, wt_n, y_form_factor):
        """
        Computes Lewis bending stress.
        Matches requirement: Knowledge of transmission systems & strength of materials.
        """
        if self.b <= 0 or self.m <= 0:
            raise ValueError("Dimensions must be positive values.")
        sigma_b = wt_n / (self.b * self.m * y_form_factor)
        return round(sigma_b, 2)

    def evaluate_safety_margin(self, calculated_stress, yield_strength_mpa):
        """Returns the structural margin of safety."""
        if calculated_stress <= 0:
            return float('inf')
        margin = (yield_strength_mpa / calculated_stress) - 1.0
        return round(margin, 2)

if __name__ == "__main__":
    # Sample run simulating a low-gear high-torque validation loop
    solver = GearStressSolver(torque_nm=350, face_width_mm=25, module=3.5)
    wt = solver.calculate_tangential_force(pitch_diameter_mm=87.5)
    stress = solver.compute_bending_stress(wt_n=wt, y_form_factor=0.36)
    margin = solver.evaluate_safety_margin(stress, yield_strength_mpa=620)
    
    print(f"Tangential Load: {wt} N")
    print(f"Calculated Tooth Bending Stress: {stress} MPa")
    print(f"Margin of Safety against Yield: {margin}")
  
