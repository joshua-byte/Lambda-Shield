import pandas as pd
import numpy as np

from simulation import run_simulation
from risk import compute_risk


def compare_architectures(
    network_size,
    base_lambda,
    noise_var,
    steps,
    runs=5
):

    architectures = [
        "scale_free",
        "random",
        "segmented"
    ]

    rows = []

    for arch in architectures:

        infection_ratios = []
        resilience_scores = []
        velocities = []

        for _ in range(runs):

            sim = run_simulation(
                network_size,
                base_lambda,
                noise_var,
                steps,
                network_type=arch
            )

            risk = compute_risk(sim, network_size)

            infection_ratios.append(risk["infection_ratio"])
            resilience_scores.append(risk["resilience_score"])
            velocities.append(risk["propagation_velocity"])

        rows.append({
            "Architecture": arch,
            "Avg Infection Ratio": np.mean(infection_ratios),
            "Avg Resilience Score": np.mean(resilience_scores),
            "Avg Propagation Velocity": np.mean(velocities)
        })

    df = pd.DataFrame(rows)

    # Determine best architecture
    best_arch = df.sort_values(
        "Avg Resilience Score",
        ascending=False
    ).iloc[0]["Architecture"]

    return df, best_arch