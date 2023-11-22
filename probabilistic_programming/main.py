import numpy as np

# Define the states of a battery
states = ["full", "half_empty"]

# Define the probability of a battery being half-empty when bought brand new
initial_half_empty_probability = 0.1


def battery_model():
    initial_battery_state = np.random.choice(states,
                                             p=[1 - initial_half_empty_probability, initial_half_empty_probability])

    # Assume you received an opened pack with at least one empty battery
    if initial_battery_state != "half_empty":
        return ["full"] * 3

    # Return the states of the remaining three batteries
    return np.random.choice(states, size=3, p=[0.5, 0.5])


# Perform simulation for question (a)
num_simulations = 100000
full_batteries_count_a = 0

for _ in range(num_simulations):
    observed_data = battery_model()
    full_batteries_count_a += sum(1 for battery in observed_data if battery == "full") == 3

probability_three_full_a = full_batteries_count_a / num_simulations

print(f"Probability of having three full batteries given at least one is empty: {probability_three_full_a:.4f}")

# Perform simulation for question (b)
num_simulations = 100000
full_batteries_count_b = 0

for _ in range(num_simulations):
    observed_data = battery_model()
    full_batteries_count_b += (
                observed_data[0] == "half_empty" and all(battery == "full" for battery in observed_data[1:]))

probability_three_full_b = full_batteries_count_b / num_simulations

print(f"Probability of having three full batteries given the first is half-empty: {probability_three_full_b:.4f}")