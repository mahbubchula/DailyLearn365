# DailyLearn365

[![Streamlit App](https://img.shields.io/badge/Streamlit-Deployed-brightgreen?logo=streamlit)](https://streamlit.io/cloud)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python Version](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)](https://www.python.org/)
[![GitHub Repo Size](https://img.shields.io/github/repo-size/YOUR_GITHUB_USERNAME/DailyLearn365)]()
[![Last Commit](https://img.shields.io/github/last-commit/YOUR_GITHUB_USERNAME/DailyLearn365)]()
[![Open Source](https://img.shields.io/badge/Open%20Source-Yes-success)]()

---

## Overview

**DailyLearn365** is a structured, longitudinal learning tracking and analytics tool designed to systematically document, analyze, and reflect on daily learning activities over a continuous 365-day period.

Built with **Streamlit** and deployed via **GitHub + Streamlit Community Cloud**, the tool requires no local installation and is suitable for researchers, graduate students, and professionals seeking reproducible and reflective learning workflows.

---

## Motivation

Continuous learning is fundamental to academic research and professional development, yet daily learning activities are rarely captured in structured, analyzable formats. DailyLearn365 addresses this gap by transforming everyday learning into a **data-centric, reproducible knowledge record**.

The system is intentionally designed not as a diary, but as a **learning analytics instrument** capable of supporting reflection, longitudinal analysis, and future research applications.

---

## Key Objectives

- Systematic documentation of daily learning activities  
- Support for reflective and self-regulated learning  
- Creation of reproducible longitudinal learning datasets  
- Interpretable analytics on learning effort and consistency  
- Deployment-ready professional and research portfolio artifact  

---

## Core Features

- Daily learning entry with domain, topic, depth, and reflection  
- Automatic date handling and append-only data storage  
- Learning streak computation and summary statistics  
- Interactive visual analytics (time investment and domain distribution)  
- CSV-based persistent storage for transparency and reproducibility  
- Fully cloud-deployable with zero backend configuration  

---

## System Architecture

DailyLearn365/
├── app.py # Main Streamlit application
├── requirements.txt # Python dependencies
├── README.md # Project documentation
├── .gitignore
│
├── data/
│ └── daily_logs.csv # Persistent learning records
│
└── modules/
├── logger.py # Data input and storage logic
├── analytics.py # Learning metrics and statistics
└── visualization.py # Interactive visualizations

yaml
Copy code

The architecture is modular, extensible, and suitable for future research-grade extensions.

---

## Deployment

DailyLearn365 is designed for **direct cloud deployment** without local setup.

1. Create a public GitHub repository  
2. Upload all project files following the documented structure  
3. Navigate to **Streamlit Community Cloud**  
4. Connect the GitHub repository  
5. Select `app.py` as the application entry point  
6. Deploy  

---

## Data Philosophy

- One row represents one learning day  
- Data storage is append-only to preserve learning history  
- CSV format ensures transparency, portability, and reproducibility  
- The dataset can support:
  - learning analytics research  
  - self-regulated learning studies  
  - AI-assisted reflective systems  

---

## Intended Use Cases

- Graduate students tracking research skill development  
- Researchers maintaining reflective learning logs  
- Professionals documenting continuous upskilling  
- Longitudinal studies of learning behavior  
- Academic and professional portfolio demonstration  

---

## Planned Extensions

- Monthly and yearly automated learning reports  
- AI-assisted synthesis of daily reflections  
- Topic evolution and learning trajectory modeling  
- Exportable summaries for academic reporting  
- Integration with literature and code repositories  

---

## License

This project is released under the **MIT License**, allowing free use, modification, and distribution with attribution.

---

## Author

**Mahbub Hassan**  
Transportation Engineering Researcher  
Chulalongkorn University, Bangkok, Thailand  

Research interests include intelligent transportation systems, AI-enabled mobility, learning analytics, and open research tools.

---

## Citation

If you use or adapt this tool in academic work, citation is appreciated.  
A formal citation format (BibTeX) will be provided upon first publication.
