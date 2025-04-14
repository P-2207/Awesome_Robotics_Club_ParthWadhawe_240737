import math

def calculate_joint_angles(x, y, z, coxa_length=5.0, femur_length=10.0, tibia_length=15.0):
    coxa_rotation = math.atan2(y, x)
    horizontal_reach = math.hypot(x, y) - coxa_length
    vertical_reach = -z
    distance_to_foot = math.hypot(horizontal_reach, vertical_reach)

    if distance_to_foot > (femur_length + tibia_length):
        raise ValueError("Foot position is out of reach.")

    tibia_cos = max(min((femur_length*2 + tibia_length*2 - distance_to_foot*2) / (2 * femur_length * tibia_length), 1), -1)
    tibia_angle = math.acos(tibia_cos)

    base_angle = math.atan2(vertical_reach, horizontal_reach)
    femur_cos = max(min((distance_to_foot*2 + femur_length*2 - tibia_length*2) / (2 * distance_to_foot * femur_length), 1), -1)
    femur_offset = math.acos(femur_cos)
    femur_angle = base_angle + femur_offset

    return (
        round(math.degrees(coxa_rotation), 2),
        round(math.degrees(femur_angle), 2),
        round(math.degrees(tibia_angle), 2)
    )

def try_leg_positions():
    positions = [
        {"name": "Test 1", "point": (15, 5, -5)},
        {"name": "Test 2", "point": (6.5, 1.2, -8)},
        {"name": "Test 3", "point": (32, 0.5, -8)},
        {"name": "Test 4", "point": (55, 5, -50)},
        {"name": "Test 5", "point": (5, 8, -25)}
    ]

    for test in positions:
        x, y, z = test["point"]
        print(f"\n{test['name']}")
        print(f"Target Position: x={x}, y={y}, z={z}")
        try:
            coxa, femur, tibia = calculate_joint_angles(x, y, z)
            print(f"Joint Angles → Coxa: {coxa}°, Femur: {femur}°, Tibia: {tibia}°")
            print("Status: Reachable.")
        except ValueError as error:
            print("Status: Unreachable.")
            print(f"Reason: {error}")

if __name__ == "_main_":
    try_leg_positions()