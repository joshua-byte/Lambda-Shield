import streamlit as st
import plotly.graph_objects as go
import networkx as nx
import numpy as np
import pandas as pd
import time

from simulation import run_simulation
from risk import compute_risk
from report import generate_report

st.set_page_config(page_title="LambdaShield", layout="wide")

st.title("LambdaShield — Network Resilience Simulator")

st.write(
"""
Simulates stochastic worm propagation and evaluates cyber outbreak risk
to help design resilient network architectures.
"""
)

# ---------------- Load Topology ----------------

def load_topology(file):

    try:
        df = pd.read_csv(file)

        if "source" in df.columns and "target" in df.columns:
            return nx.from_pandas_edgelist(df, "source", "target")

    except Exception:
        pass

    file.seek(0)

    edges = []

    for line in file:
        line = line.decode("utf-8").strip()

        if not line:
            continue

        parts = line.replace(",", " ").split()

        if len(parts) >= 2:
            edges.append((parts[0], parts[1]))

    G = nx.Graph()
    G.add_edges_from(edges)

    return G


# ---------------- Sidebar ----------------

st.sidebar.header("Simulation Controls")

network_size = st.sidebar.slider("Network Size", 50, 500, 200)

base_lambda = st.sidebar.slider(
    "Base Infection Rate (λ₀)", 0.1, 1.0, 0.3
)

noise_var = st.sidebar.slider(
    "Noise Variance (σ²)", 0.0, 0.1, 0.02
)

steps = st.sidebar.slider(
    "Simulation Steps", 10, 100, 40
)

network_type = st.sidebar.selectbox(
    "Network Architecture",
    ["scale_free", "random", "segmented"]
)

uploaded_file = st.sidebar.file_uploader(
    "Upload Network Topology (.csv or .txt)",
    type=["csv", "txt"]
)

compare_mode = st.sidebar.checkbox(
    "Compare Network Architectures"
)

# ---------------- Uploaded Network ----------------

G_uploaded = None

if uploaded_file:

    G_uploaded = load_topology(uploaded_file)

    st.subheader("Uploaded Network Statistics")

    st.success(
        f"Loaded network with {G_uploaded.number_of_nodes()} nodes and {G_uploaded.number_of_edges()} edges"
    )

    avg_degree = np.mean([d for _, d in G_uploaded.degree()])

    st.write("Average Degree:", round(avg_degree, 2))


# ---------------- Architecture Comparison ----------------

if compare_mode:

    st.subheader("Architecture Comparison")

    architectures = ["scale_free", "random", "segmented"]

    rows = []
    runs = 5

    for arch in architectures:

        infection_vals = []
        resilience_vals = []

        for _ in range(runs):

            sim = run_simulation(
                network_size,
                base_lambda,
                noise_var,
                steps,
                arch
            )

            risk = compute_risk(sim, network_size)

            infection_vals.append(risk["infection_ratio"])
            resilience_vals.append(risk["resilience_score"])

        rows.append({
            "Architecture": arch,
            "Infection Ratio": np.mean(infection_vals),
            "Resilience Score": np.mean(resilience_vals)
        })

    df_compare = pd.DataFrame(rows)

    st.dataframe(df_compare, use_container_width=True)

    fig_compare = go.Figure()

    fig_compare.add_bar(
        x=df_compare["Architecture"],
        y=df_compare["Resilience Score"]
    )

    fig_compare.update_layout(
        title="Architecture Resilience Comparison",
        xaxis_title="Architecture",
        yaxis_title="Resilience Score",
        transition=dict(duration=500)
    )

    st.plotly_chart(fig_compare, use_container_width=True)

    best = df_compare.sort_values(
        "Resilience Score", ascending=False
    ).iloc[0]

    st.success(f"Recommended Architecture: {best['Architecture']}")


# ---------------- Run Simulation ----------------

if st.sidebar.button("Run Simulation"):

    with st.spinner("Running network simulation..."):

        progress = st.progress(0)

        for i in range(100):
            progress.progress(i + 1)
            time.sleep(0.01)

        progress.empty()

        if G_uploaded is not None:

            network_size = G_uploaded.number_of_nodes()

            results = run_simulation(
                network_size,
                base_lambda,
                noise_var,
                steps,
                graph=G_uploaded
            )

        else:

            results = run_simulation(
                network_size,
                base_lambda,
                noise_var,
                steps,
                network_type
            )

    st.success("Simulation complete")

    risk = compute_risk(results, network_size)

    # ---------------- Risk Metrics ----------------

    st.subheader("Risk Assessment")

    col1, col2, col3, col4, col5 = st.columns(5)

    col1.metric("Risk Level", risk["risk_level"])
    col2.metric("Avg λ(t)", round(risk["avg_lambda"], 3))
    col3.metric("Infection Ratio", round(risk["infection_ratio"], 3))
    col4.metric("Resilience Score", round(risk["resilience_score"], 3))
    col5.metric("Propagation Velocity", round(risk["propagation_velocity"], 2))

    st.info(risk["recommendation"])

    # ---------------- Risk Gauge ----------------

    fig_gauge = go.Figure(go.Indicator(
        mode="gauge+number",
        value=risk["risk_score"],
        title={'text': "Network Risk (%)"},
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': "red"},
            'steps': [
                {'range': [0, 30], 'color': "green"},
                {'range': [30, 60], 'color': "yellow"},
                {'range': [60, 100], 'color': "red"}
            ]
        }
    ))

    st.plotly_chart(fig_gauge, use_container_width=True)

    # ---------------- Propagation Curve ----------------

    st.subheader("Propagation Curve")

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        y=results["infected_count"],
        mode="lines+markers",
        name="Infected Nodes"
    ))

    fig.update_layout(
        xaxis_title="Time Step",
        yaxis_title="Infected Nodes",
        template="plotly_dark",
        transition=dict(duration=500)
    )

    st.plotly_chart(fig, use_container_width=True)

    # ---------------- Lambda Curve ----------------

    fig2 = go.Figure()

    fig2.add_trace(go.Scatter(
        y=results["lambda_values"],
        mode="lines",
        name="λ(t)",
        line=dict(color="orange")
    ))

    fig2.update_layout(
        xaxis_title="Time Step",
        yaxis_title="Average λ(t)",
        template="plotly_dark",
        transition=dict(duration=500)
    )

    st.plotly_chart(fig2, use_container_width=True)

    # ---------------- Critical Nodes ----------------

    G = results["graph"]

    centrality = nx.betweenness_centrality(G)

    top_nodes = sorted(
        centrality,
        key=centrality.get,
        reverse=True
    )[:5]

    st.subheader("Critical Nodes")

    df_nodes = pd.DataFrame({"Critical Node": top_nodes})

    st.dataframe(df_nodes, use_container_width=True)

    # ---------------- Network Analytics ----------------

    st.subheader("Network Analytics")

    avg_degree = np.mean([d for _, d in G.degree()])
    clustering = nx.average_clustering(G)
    density = nx.density(G)

    col1, col2, col3 = st.columns(3)

    col1.metric("Average Degree", round(avg_degree, 2))
    col2.metric("Clustering Coefficient", round(clustering, 3))
    col3.metric("Network Density", round(density, 4))

    # ---------------- Network Visualization ----------------

    st.subheader("Network Infection Snapshot")

    infected = results["final_infected"]

    MAX_VIS_NODES = 300

    if G.number_of_nodes() > MAX_VIS_NODES:

        sample_nodes = list(G.nodes())[:MAX_VIS_NODES]
        G_vis = G.subgraph(sample_nodes)

        st.caption(
            f"Showing {MAX_VIS_NODES} nodes out of {G.number_of_nodes()}"
        )

    else:
        G_vis = G

    pos = nx.kamada_kawai_layout(G_vis)

    edge_x = []
    edge_y = []

    for edge in G_vis.edges():

        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]

        edge_x += [x0, x1, None]
        edge_y += [y0, y1, None]

    edge_trace = go.Scatter(
        x=edge_x,
        y=edge_y,
        mode="lines",
        line=dict(width=0.5, color="#888"),
        hoverinfo="none"
    )

    node_x = []
    node_y = []
    node_color = []

    critical_set = set(top_nodes)

    for node in G_vis.nodes():

        x, y = pos[node]

        node_x.append(x)
        node_y.append(y)

        if node in infected:
            node_color.append("red")
        elif node in critical_set:
            node_color.append("yellow")
        else:
            node_color.append("blue")

    node_trace = go.Scatter(
        x=node_x,
        y=node_y,
        mode="markers",
        text=list(G_vis.nodes()),
        hoverinfo="text",
        marker=dict(size=8, color=node_color)
    )

    fig_network = go.Figure(data=[edge_trace, node_trace])

    fig_network.update_layout(
        showlegend=False,
        template="plotly_dark"
    )

    st.plotly_chart(fig_network, use_container_width=True)

    st.caption(
        "Red: infected nodes | Yellow: critical nodes | Blue: healthy nodes"
    )

    # ---------------- Export Simulation Data ----------------

    df_export = pd.DataFrame({
        "infected_nodes": results["infected_count"],
        "lambda": results["lambda_values"]
    })

    st.download_button(
        "Download Simulation Data",
        df_export.to_csv(index=False),
        "simulation_data.csv"
    )

    # ---------------- PDF Report ----------------

    pdf = generate_report(
        risk,
        results,
        network_size,
        top_nodes
    )

    st.download_button(
        "Download Risk Report (PDF)",
        pdf,
        file_name="LambdaShield_Report.pdf",
        mime="application/pdf"
    )