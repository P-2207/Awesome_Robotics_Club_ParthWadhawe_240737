# Awesome_Robotics_Club_ParthWadhawe_240737
 
# Hexapod Leg Inverse Kinematics

This Python script calculates the joint angles required for positioning the foot of a hexapod robot's leg at a specified 3D coordinate. The script simulates inverse kinematics for a 3-DOF (Degree of Freedom) leg composed of **Coxa**, **Femur**, and **Tibia** segments.

---

##  What It Does

- Calculates joint angles given a 3D position (x, y, z)
- Checks whether the foot position is physically reachable
- Outputs human-readable angles in degrees
- Runs multiple test cases for validation

---

##  How It Works

The leg has three main joints:
- **Coxa**: Rotates the leg left/right (horizontal plane)
- **Femur**: Moves the leg up/down (vertical plane)
- **Tibia**: Extends/retracts the leg to reach the target point

The script uses trigonometry and the law of cosines to compute:
- Horizontal and vertical reach
- Total reachability distance
- Angles for each joint in degrees

---

## 🚀 Running the Code

Make sure you have **Python 3** installed.

Run it with:
```bash
task.py
