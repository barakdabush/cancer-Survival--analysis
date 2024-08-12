# Cancer Survival Analysis

This repository contains scripts and functions for conducting survival analysis on a cancer dataset. The primary focus is on analyzing survival rates based on various demographic and clinical factors, such as tumor stage, gender, ethnicity, and race.

## Table of Contents

- [Project Overview](#project-overview)
- [File Structure](#file-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Functions Overview](#functions-overview)
- [Data](#data)
- [Results](#results)
- [License](#license)

## Project Overview

The goal of this project is to perform survival analysis using the Kaplan-Meier estimator and Log-rank test on a clinical dataset. The analysis includes pre-processing the data, visualizing demographic distributions, and analyzing survival rates across different tumor stages.

## File Structure

- `clinical.tsv`: The dataset containing clinical information of cancer patients.
- `cancer_analysis.py`: The main script containing all functions for data processing, analysis, and visualization.
- `README.md`: Project documentation.

## Installation

1. Clone this repository to your local machine:
    ```bash
    git clone https://github.com/yourusername/cancer-survival-analysis.git
    ```

2. Navigate to the project directory:
    ```bash
    cd cancer-survival-analysis
    ```

3. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Data Pre-processing:**
   The `pre_process` function is used to clean
