# ==========================================================
# TRAFFIC SIGNAL OPTIMIZATION USING RULE-BASED AI
# ==========================================================
#
# CO1 : Knowledge Representation, PEAS Model,
#       Rule Sets, Dictionaries, Functions
#
# CO2 : Search-Based Optimization (Future Scope)
#
# CO3 : Constraint Satisfaction through
#       Traffic Density Rules
#
# CO4 : Decision Making using Utility-Based Logic
#
# CO5 : Probabilistic Traffic Prediction
#       (Future Scope)
#
# CO6 : Hybrid AI Architecture and
#       Explainable Reasoning
#
# ==========================================================

print("\nTRAFFIC SIGNAL OPTIMIZATION SYSTEM")
print("=" * 60)

# ==========================================================
# PEAS MODEL (CO1)
# ==========================================================
#
# Performance Measure:
#     Minimize waiting time and congestion
#
# Environment:
#     Four-way traffic intersection
#
# Actuators:
#     Traffic signal controller
#
# Sensors:
#     Vehicle count input / traffic sensors
#
# ==========================================================


# ==========================================================
# TRAFFIC DENSITY ANALYSIS
# CO1 + CO3
# ==========================================================

def classify_density(vehicle_count):

    if vehicle_count <= 15:
        return "LOW"

    elif vehicle_count <= 35:
        return "MEDIUM"

    else:
        return "HIGH"


# ==========================================================
# RULE ENGINE
# CO1 + CO4 + CO6
# ==========================================================

def calculate_green_time(density):

    # Rule 1
    if density == "LOW":
        return 20

    # Rule 2
    elif density == "MEDIUM":
        return 40

    # Rule 3
    elif density == "HIGH":
        return 60


# ==========================================================
# SIGNAL OPTIMIZATION
# CO1 + CO6
# ==========================================================

def optimize_signals(traffic_data):

    results = {}

    for road, vehicles in traffic_data.items():

        density = classify_density(vehicles)

        green_time = calculate_green_time(density)

        results[road] = {
            "vehicles": vehicles,
            "density": density,
            "green_time": green_time
        }

    return results


# ==========================================================
# EXPLAINABLE REASONING TRACE
# CO6
# ==========================================================

def explain_decision(results):

    print("\nREASONING TRACE")
    print("-" * 60)

    for road, info in results.items():

        print(
            f"{road}: "
            f"{info['vehicles']} vehicles "
            f"-> {info['density']} Density "
            f"-> Green Signal = "
            f"{info['green_time']} sec"
        )


# ==========================================================
# DISPLAY RESULTS
# ==========================================================
def display_results(results):

    print("\n")
    print("=" * 60)
    print("        TRAFFIC SIGNAL OPTIMIZATION REPORT")
    print("=" * 60)

    for road, info in results.items():

        print(
            f"{road:<10} | "
            f"Vehicles: {info['vehicles']:<3} | "
            f"Density: {info['density']:<6} | "
            f"Green Time: {info['green_time']} sec"
        )

    print("=" * 60)


# ==========================================================
# MODE SELECTION
# ==========================================================

print("\nSelect Mode")
print("1. Manual Input")
print("2. Demo Data")

choice = input("Enter your choice (1 or 2): ")


# ==========================================================
# MANUAL INPUT MODE
# ==========================================================

if choice == "1":

    traffic_data = {

        "North": int(input("Enter North Road Vehicle Count : ")),

        "South": int(input("Enter South Road Vehicle Count : ")),

        "East": int(input("Enter East Road Vehicle Count : ")),

        "West": int(input("Enter West Road Vehicle Count : "))
    }


# ==========================================================
# DEMO MODE
# ==========================================================

else:

    traffic_data = {

        "North": 50,
        "South": 28,
        "East": 10,
        "West": 42
    }


# ==========================================================
# PROCESS DATA
# ==========================================================

optimized_results = optimize_signals(traffic_data)


# ==========================================================
# DISPLAY OUTPUT
# ==========================================================

display_results(optimized_results)

# CO6 : Explainable AI Trace
explain_decision(optimized_results)


# ==========================================================
# CO2 FUTURE EXTENSION
# ==========================================================
#
# Search Algorithms:
#
# - BFS
# - DFS
# - Uniform Cost Search
# - A*
#
# Future Enhancement:
#
# Optimize vehicle routing across multiple
# intersections using A* Search.
#
# Example:
#
# Junction A ---- Junction B ---- Junction C
#
# A* can determine the least congested path.
#
# ==========================================================


# ==========================================================
# CO5 FUTURE EXTENSION
# ==========================================================
#
# Bayesian Traffic Prediction
#
# Example:
#
# P(Congestion | Rain)
#
# Predict future traffic conditions
# using probabilistic reasoning.
#
# ==========================================================


# ==========================================================
# CO6 FUTURE HYBRID AI
# ==========================================================
#
# Rule-Based System
#        +
# Search Algorithms
#        +
# Bayesian Inference
#
# = Intelligent Traffic Management System
#
# ==========================================================