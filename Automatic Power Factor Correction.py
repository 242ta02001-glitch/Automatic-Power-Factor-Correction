# Automatic Power Factor Correction (APFC)
# EEE Mini Project

import math

print("========================================")
print(" AUTOMATIC POWER FACTOR CORRECTION")
print("========================================")

TARGET_PF = 0.95

while True:
    try:
        active_power = float(input("\nEnter Active Power (kW): "))
        current_pf = float(input("Enter Present Power Factor (0-1): "))

        if active_power <= 0 or current_pf <= 0 or current_pf > 1:
            print("Enter valid values.")
            continue

        print("\n------ System Status ------")
        print(f"Active Power       : {active_power:.2f} kW")
        print(f"Present PF         : {current_pf:.2f}")
        print(f"Target PF          : {TARGET_PF:.2f}")

        if current_pf >= TARGET_PF:
            print("Power Factor is acceptable.")
            print("Capacitor Bank    : OFF")

        else:
            # Calculate reactive power before correction
            q_initial = active_power * math.tan(math.acos(current_pf))

            # Calculate reactive power at target PF
            q_target = active_power * math.tan(math.acos(TARGET_PF))

            # Required capacitor compensation
            capacitor_kvar = q_initial - q_target

            print("\nPower Factor is LOW.")
            print(f"Required Compensation: {capacitor_kvar:.2f} kVAR")
            print("Capacitor Bank    : ON")
            print(f"Corrected PF      : {TARGET_PF:.2f}")

        print("----------------------------")

        choice = input("\nPerform another calculation? (yes/no): ")

        if choice.lower() != "yes":
            print("\nAPFC system stopped.")
            break

    except ValueError:
        print("Invalid input! Enter numerical values.")
