import numpy as np

# Define the states of a battery
states = ["full", "half_empty"]

# Define the probability of a battery being half-empty when bought brand new
init_half_empty = 0.1


def battery_model(a=3):
    init_bat_state = []
    for i in range(a):
        init_bat_state.append(np.random.choice(states, p=[1 - init_half_empty, init_half_empty]))
    init_bat_state.append(states[1])
    return init_bat_state

def battery_model_b(a=4):
    init_bat_state = []
    for i in range(a):
        init_bat_state.append(np.random.choice(states, p=[1 - init_half_empty, init_half_empty]))

    return init_bat_state
def q_a(num):
    full_batteries_count_a = 0

    for _ in range(num):
        observed_data = battery_model()
        full_batteries_count_a += sum(1 for battery in observed_data if battery == "full") == 3

    probability_three_full_a = full_batteries_count_a / num

    print(f"Probability of having three full batteries in the box with one empyt battery is: {probability_three_full_a:.4f}")

sim_count = 100000
q_a(sim_count)

def q_b(num):
    full_batteries_count_a = 0

    for _ in range(num):
        observed_data = battery_model_b()
        full_batteries_count_a += sum(1 for battery in observed_data if battery == "full") == 3

    probability_three_full_a = full_batteries_count_a / num

    print(f"Probability of having three full batteries in the box with one empyt battery is: {probability_three_full_a:.4f}")


q_b(sim_count)