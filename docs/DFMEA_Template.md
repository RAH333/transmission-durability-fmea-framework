# Design Failure Mode and Effects Analysis (DFMEA) - Transmission Subsystem

**System:** PTD Mechanical Development / Gear Arrangement Assembly  
**Prepared By:** Senior Engineer Applicant  

| Item / Function | Potential Failure Mode | Potential Effect of Failure | SEV | Potential Cause | OCC | Current Design Controls | DET | RPN | Actions Recommended |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Input Shaft Gear Teeth** / Transmit Torque | Tooth Root Fatigue Fracture | Complete loss of drive, catastrophic housing damage | **9** | Cyclic bending stress exceeding fatigue limits | **3** | Analytical stress solver script evaluation (Lewis/AGMA limits) | **4** | **108** | Implement shot-peening on root fillets; update DVP to include accelerated life cyclic tests. |
| **Spline Interfaces** / Axial Alignment | Galling / Adhesive Wear | Increased backlash, high vibration telemetry signature | **6** | Insufficient lubrication distribution at high thermal bands | **4** | GD&T micro-geometry optimization profile | **3** | **72** | Add dual-channel oil lubrication pathways inside shaft core. |
