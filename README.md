# 🕵️‍♂️ Noir Interrogation & Multi-Agent Architecture

An enterprise-grade, 1940s-themed interactive AI investigation system powered by Gemini API, Google Cloud Platform (GCP), and modular multi-agent telemetry. Built under the **T.M.T Protocol v1.0** framework.

---

## 🏛️ System Architecture & Core Modules

* **`agents/agent.py`**: Core agentic orchestrator managing multi-turn reasoning loops, tool execution bounds, and dynamic role contexts (`EliteAxis-Alpha`)[span_1](start_span)[span_1](end_span).
* **`agents/self_healing_vault.py`**: Cryptographic integrity verification system using SHA-256 state hashing and automated anomaly detection to trigger self-healing protocols[span_2](start_span)[span_2](end_span).
* **`config/cloud_state.py`**: Secure cloud persistence layer connected to **Google Cloud Datastore** (`project-449e9aa7-9f7e-4f91-951`) for robust agent state management[span_3](start_span)[span_3](end_span).
* **`config/agent_config.json`**: Global runtime parameters, strict tool-calling configurations, and strict architectural declarations[span_4](start_span)[span_4](end_span).
* **`evals/agent_analytics.py`**: Automated telemetry pipeline streaming real-time execution traces and risk scores to **Google Cloud BigQuery** (`tmt_agent_telemetry`)[span_5](start_span)[span_5](end_span).
* **`evals/run_local.py`**: Local evaluation harness for multi-agent reasoning validation and test case execution suites[span_6](start_span)[span_6](end_span).

---

## 🚀 Repository Structure

```text
├── agents/
│   ├── agent.py                 # Core Agentic Orchestrator
│   └── self_healing_vault.py    # Cryptographic Vault & Self-Healing Logic
├── config/
│   ├── agent_config.json        # Global Architectural Configs & Parameters
│   └── cloud_state.py           # GCP Datastore Persistence Layer
├── evals/
│   ├── agent_analytics.py       # BigQuery Telemetry Pipeline
│   └── run_local.py             # Local Evaluation Test Harness
├── index.html                   # Interactive 1940s Noir UI Canvas
├── README.md                    # Professional Project Documentation
└── requirements.txt             # Enterprise Python Dependencies





[View ARCHITECT.md](ARCHITECT.md)
