# LambdaShield - Network Resilience Simulator

LambdaShield is an interactive network security analysis tool that
simulates **stochastic worm propagation** and evaluates **cyber outbreak
risk** across network architectures.

The system models malware propagation using probabilistic infection
dynamics and graph-based network structures to help analysts understand
how different architectures influence attack spread.

The tool provides **visual analytics, resilience metrics, and automated
risk reports**.

------------------------------------------------------------------------

## Overview

Modern network infrastructures are vulnerable to rapid propagation
attacks such as worms, botnets, and distributed malware. The ability to
model propagation dynamics before deployment can significantly improve
defensive architecture design.

LambdaShield simulates attack propagation across different network
topologies and provides metrics such as:

-   Infection growth
-   Outbreak velocity
-   Network resilience score
-   Risk classification
-   Critical node detection

------------------------------------------------------------------------

## Features

-   Stochastic worm propagation simulation
-   Multiple network architecture models:
    -   Scale-free networks
    -   Random networks
    -   Segmented networks
-   Interactive visualization of infection spread
-   Network analytics and centrality analysis
-   Architecture comparison tools
-   PDF security report generation
-   Simulation data export (CSV)

------------------------------------------------------------------------

## Architecture

The system is structured into modular components:

    LambdaShield/
    │
    ├── app.py          # Streamlit dashboard
    ├── simulation.py   # Worm propagation model
    ├── risk.py         # Risk analysis engine
    ├── report.py       # PDF report generator
    ├── requirements.txt
    └── README.md

------------------------------------------------------------------------

## Installation

Clone the repository:

    git clone https://github.com/yourusername/lambdashield.git
    cd lambdashield

Install dependencies:

    pip install -r requirements.txt

------------------------------------------------------------------------

## Running the Application

Start the Streamlit dashboard:

    streamlit run app.py

The application will launch in your browser.

------------------------------------------------------------------------

## Usage

1.  Configure simulation parameters in the sidebar
2.  Select network architecture or upload a topology dataset
3.  Run the simulation
4.  Analyze propagation curves and risk metrics
5.  Export reports and simulation data

------------------------------------------------------------------------

## Example Applications

LambdaShield can be used for:

-   Cybersecurity architecture planning
-   Network resilience analysis
-   Malware propagation research
-   Security training simulations
-   Academic research in network science

