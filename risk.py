import numpy as np


def compute_risk(results, network_size):

    infected_series = results.get("infected_count", [])
    lambda_series = results.get("lambda_values", [])

    # ---------------- Basic Metrics ----------------

    if len(lambda_series) > 0:
        avg_lambda = float(np.mean(lambda_series))
    else:
        avg_lambda = 0.0

    if len(infected_series) > 0:
        final_infected = infected_series[-1]
    else:
        final_infected = 0

    infection_ratio = final_infected / network_size if network_size > 0 else 0

    # ---------------- Propagation Metrics ----------------

    growth = np.diff(infected_series) if len(infected_series) > 1 else []

    if len(growth) > 0:
        propagation_velocity = float(np.mean(growth))
        peak_growth = float(np.max(growth))
    else:
        propagation_velocity = 0.0
        peak_growth = 0.0

    outbreak_time = results.get("outbreak_time", None)

    # ---------------- Risk Classification ----------------

    if infection_ratio < 0.15 and avg_lambda < 0.25:

        risk = "LOW"
        advice = "Maintain monitoring and apply regular patching."

    elif infection_ratio < 0.40 or propagation_velocity < 5:

        risk = "MEDIUM"
        advice = "Enable anomaly monitoring and traffic throttling."

    else:

        risk = "HIGH"
        advice = "Isolate infected nodes and deploy network segmentation."

    # ---------------- Resilience Score ----------------

    resilience_score = max(0.0, 1 - infection_ratio)

    # ---------------- Risk Score ----------------

    risk_score = min(100.0, infection_ratio * 100)

    # ---------------- Burst Detection ----------------

    burst_threshold = network_size * 0.05
    burst_detected = peak_growth > burst_threshold

    # ---------------- Output ----------------

    return {

        "risk_level": risk,

        "avg_lambda": avg_lambda,

        "infection_ratio": float(infection_ratio),

        "risk_score": float(risk_score),

        "resilience_score": float(resilience_score),

        "burst_detected": burst_detected,

        "propagation_velocity": propagation_velocity,

        "peak_growth": peak_growth,

        "outbreak_time": outbreak_time,

        "recommendation": advice
    }