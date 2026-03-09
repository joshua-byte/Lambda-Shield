import networkx as nx
import numpy as np
import random


def run_simulation(
    network_size=200,
    base_lambda=0.3,
    noise_var=0.02,
    steps=40,
    network_type="scale_free",
    graph=None,
    seed=None
):

    # ---------------- Reproducibility ----------------

    if seed is not None:
        random.seed(seed)
        np.random.seed(seed)

    # ---------------- Graph Selection ----------------

    if graph is not None:

        G = graph
        network_size = G.number_of_nodes()

    else:

        if network_type == "scale_free":

            G = nx.barabasi_albert_graph(network_size, 3)

        elif network_type == "random":

            G = nx.erdos_renyi_graph(network_size, 0.05)

        elif network_type == "segmented":

            clusters = max(2, network_size // 20)

            G = nx.connected_caveman_graph(
                clusters,
                network_size // clusters
            )

        else:

            G = nx.barabasi_albert_graph(network_size, 3)

    # ---------------- Initial Infection ----------------

    node_list = list(G.nodes())

    if not node_list:
        raise ValueError("Graph contains no nodes")

    infected = {random.choice(node_list)}

    infection_history = []
    lambda_history = []
    infection_states = []

    # Precompute neighbors for speed
    neighbors_map = {node: list(G.neighbors(node)) for node in G.nodes()}

    # ---------------- Simulation Loop ----------------

    for step in range(steps):

        new_infected = set()
        step_lambda_values = []

        for node in infected:

            lam = base_lambda + np.random.normal(0, noise_var)
            lam = max(lam, 0)

            step_lambda_values.append(lam)

            attempts = np.random.poisson(lam)

            neighbors = neighbors_map.get(node, [])

            if not neighbors:
                continue

            for _ in range(attempts):

                target = random.choice(neighbors)

                if target not in infected:
                    new_infected.add(target)

        infected |= new_infected

        infection_history.append(len(infected))
        infection_states.append(set(infected))

        avg_lambda = np.mean(step_lambda_values) if step_lambda_values else 0
        lambda_history.append(float(avg_lambda))

    # ---------------- Propagation Metrics ----------------

    growth = np.diff(infection_history) if len(infection_history) > 1 else []

    peak_growth = int(np.max(growth)) if len(growth) > 0 else 0

    propagation_velocity = float(np.mean(growth)) if len(growth) > 0 else 0

    # outbreak time (first time > 25% infected)
    outbreak_time = None

    for t, count in enumerate(infection_history):

        if count >= 0.25 * network_size:
            outbreak_time = t
            break

    return {

        "graph": G,

        "infected_count": infection_history,

        "lambda_values": lambda_history,

        "infection_states": infection_states,

        "final_infected": infected,

        "infection_ratio": len(infected) / network_size if network_size > 0 else 0,

        "peak_growth": peak_growth,

        "propagation_velocity": propagation_velocity,

        "outbreak_time": outbreak_time,

        "network_type": network_type
    }