no_heat_wave = input("Are there no heatwaves? (true/false): ").strip().lower() == "true"
guide_available = input("Is your guide available? (true/false): ").strip().lower() == "true"

if no_heat_wave and guide_available:
    print("You can proceed with the trip")
else:
    print("You cannot proceed with the trip")
