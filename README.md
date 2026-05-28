# LambdaShield: Network Attack Propagation Simulator

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Cybersecurity](https://img.shields.io/badge/Focus-NetworkSecurity-red)
![Simulation](https://img.shields.io/badge/Type-PropagationModeling-orange)
![Analytics](https://img.shields.io/badge/Analytics-NetworkScience-green)
![Status](https://img.shields.io/badge/Status-Active-success)

LambdaShield is an interactive network security analysis platform designed to simulate how adversarial compromise propagates across different network architectures and evaluate the resulting resilience and security risk.

The platform models stochastic propagation behavior across graph-based network topologies to analyze:

* attack spread dynamics,
* critical-node influence,
* outbreak velocity,
* and architectural resilience under adversarial conditions.

> **Key Question:**
> If an attacker gains initial access, how far and how fast can compromise spread across a network?

---

# Overview

Modern enterprise infrastructures are highly interconnected, making them vulnerable to:

* lateral movement,
* worm-style propagation,
* botnet expansion,
* and rapid compromise escalation.

LambdaShield helps security engineers, researchers, and students:

* model adversarial spread behavior,
* identify fragile network architectures,
* evaluate segmentation effectiveness,
* and analyze resilience before real-world deployment.

The project combines:

* cybersecurity analytics,
* network science,
* graph-based simulation,
* and security-risk modeling.

---

# Core Features

## Stochastic Propagation Simulation

Models probabilistic compromise spread across interconnected network nodes.

## Multiple Network Architectures

Supports:

* Scale-Free Networks
* Random Networks
* Segmented Network Models

## Propagation Analytics

Tracks:

* infection growth over time,
* outbreak velocity,
* spread dynamics,
* and propagation patterns.

## Security Insights

Provides:

* critical-node identification,
* resilience scoring,
* network density analytics,
* and risk classification.

## Interactive Visualization

Includes:

* real-time graph-based propagation tracking,
* topology visualization,
* and dynamic simulation analytics.

## Automated Reporting

Generates:

* PDF risk assessment reports,
* CSV simulation exports,
* and resilience summaries.

---

# Why LambdaShield Matters

Most security tools focus on:

> detecting attacks.

LambdaShield focuses on:

> understanding the impact of a successful compromise.

The platform helps answer questions such as:

* How vulnerable is a network architecture?
* Which nodes are most critical?
* Does segmentation reduce propagation risk?
* How quickly can compromise escalate?
* Which architectures are most resilient under attack?

---

# Security Use Cases

LambdaShield can be used for:

* enterprise network resilience analysis,
* adversarial propagation modeling,
* security architecture evaluation,
* malware-spread simulation,
* security education and training,
* red team / blue team exercises,
* and cyber-risk experimentation.

---

# Key Insights Demonstrated

The simulations demonstrate several important security concepts:

* Scale-free architectures are highly vulnerable due to hub-node centralization
* Flat network structures enable rapid lateral movement
* Segmentation significantly reduces propagation velocity
* Critical nodes disproportionately influence outbreak success
* Network topology strongly affects resilience under adversarial conditions

---

# Simulation Workflow

```text
1. Generate Network Topology
2. Configure Propagation Parameters
3. Simulate Compromise Spread
4. Track Propagation Dynamics
5. Analyze Network Metrics
6. Generate Risk Assessment Report
```

---

# Interactive Dashboard

<img width="1704" height="722" alt="networkx" src="https://github.com/user-attachments/assets/9bf50ada-7c7b-4605-822e-fdda34a0e7af" />


The dashboard provides:

* real-time propagation visualization,
* network analytics,
* topology monitoring,
* and resilience analysis.

Features include:

* infection spread tracking,
* critical-node identification,
* topology comparison,
* and adjustable simulation controls.

---

# Propagation Analytics

<img width="1730" height="826" alt="curve" src="https://github.com/user-attachments/assets/2cf35435-5e56-451f-9cb2-ae4ad2d87017" />


The propagation engine tracks:

* outbreak growth over time,
* average propagation behavior,
* spread acceleration,
* and compromise velocity.

These analytics help evaluate how different architectures respond under adversarial propagation scenarios.

---

# Automated Security Reporting

<img width="1016" height="835" alt="report_review" src="https://github.com/user-attachments/assets/cf6138bb-e9f9-4f37-b5af-e4f408eb41cf" />


LambdaShield generates structured security assessment reports including:

* resilience scoring,
* propagation metrics,
* critical-node analysis,
* outbreak summaries,
* and network risk classification.

The reporting system is designed to simulate lightweight security-analysis workflows for resilience evaluation.

---

# Network Metrics

LambdaShield analyzes metrics including:

| Metric                 | Description                        |
| ---------------------- | ---------------------------------- |
| Infection Ratio        | Percentage of compromised nodes    |
| Resilience Score       | Resistance to propagation spread   |
| Propagation Velocity   | Speed of compromise escalation     |
| Average Degree         | Average network connectivity       |
| Clustering Coefficient | Degree of local interconnectedness |
| Network Density        | Overall graph connectivity         |

---

# Example Network Architectures

## Scale-Free Networks

* Highly connected hub nodes
* Fast propagation potential
* Enterprise-like topology behavior

## Random Networks

* Uniform connection distribution
* Moderate propagation behavior

## Segmented Networks

* Isolated subnet structures
* Reduced lateral movement potential
* Improved resilience characteristics

---

# Technical Stack

## Languages & Frameworks

* Python

## Simulation & Analytics

* NetworkX
* NumPy
* Pandas

## Visualization

* Plotly
* Dash

## Reporting

* ReportLab / PDF generation

---

# Installation

## Clone Repository

```bash
git clone https://github.com/joshua-byte/LambdaShield.git
cd LambdaShield
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Usage

Run the interactive dashboard:

```bash
python app.py
```

Then access the dashboard locally through your browser.

---

# Example Research Applications

LambdaShield can support:

* cyber propagation research,
* resilience-analysis experimentation,
* topology-security evaluation,
* adversarial spread modeling,
* and security-network education workflows.

---

# Future Improvements

* Multi-stage attack simulation
* Adaptive defensive response modeling
* Real-time topology mutation
* Threat-intelligence integration
* AI-assisted resilience prediction
* Distributed network simulation
* ATT&CK-aligned propagation mapping
* Dynamic node hardening simulation
* Comparative architecture benchmarking

---

# Research Foundation

LambdaShield is based on ongoing research into adversarial propagation dynamics, network resilience, and stochastic compromise modeling.

📄 IEEE Xplore Publication:  
[Uncertainty-Driven Probabilistic Framework for Modeling Worm Propagation in Large-Scale Network Topologies](https://ieeexplore.ieee.org/document/11507173)

The implementation extends concepts related to:
- propagation behavior across graph topologies,
- critical-node influence,
- resilience scoring,
- and adversarial spread dynamics in distributed systems.

---

---
# Disclaimer

This project is intended solely for:

* cybersecurity education,
* resilience-analysis experimentation,
* network-science research,
* and defensive security analysis.

The platform is designed for controlled research and educational environments only.

---

# Author

Joshua Jesuraj Sanctus

Cybersecurity • Network Science • Detection Engineering • Security Analytics
