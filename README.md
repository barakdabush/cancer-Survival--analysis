# Cancer Survival Analysis

This repository contains scripts and functions for conducting survival analysis on a cancer dataset. The primary focus is on analyzing survival rates based on various demographic and clinical factors, such as tumor stage, gender, ethnicity, and race.

## Table of Contents

- [Project Overview](#project-overview)
- [File Structure](#file-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Results](#results)


## Project Overview

The goal of this project is to conduct comprehensive survival analysis on a clinical dataset. The analysis includes the following key components:

Data Pre-processing and Visualization: The dataset is pre-processed to handle categorical variables, and demographic distributions are visualized to provide insights into the data.

Kaplan-Meier Estimator and Log-rank Test: These traditional statistical methods are used to estimate survival functions and compare survival rates across different tumor stages, respectively.

Random Survival Forest (RSF) Model: In addition to traditional methods, a Random Survival Forest model is employed to perform survival analysis. This includes:

Training the RSF model on the clinical data to predict survival times.
Evaluating model performance using the concordance index.
Identifying important features through permutation importance.
Reducing the feature set based on importance scores and retraining the model to enhance interpretability.
By integrating both traditional and machine learning approaches, this project aims to provide a deeper understanding of the factors influencing survival outcomes.

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

## Functions Overview

1. **Data Pre-processing:**
   The `pre_process` function is used to clean and prepare the data for analysis. It handles missing values, converts data types, and drops unnecessary columns.

2. **Demographic Analysis:**
   Use the `demographic_analysis` function to visualize the distribution of age, gender, ethnicity, and race among the patients.

3. **Survival Analysis:**
   The `kalman_meier_fitter_analysis` function plots the survival functions for different tumor stages using the Kaplan-Meier estimator.

4. **Log-rank Test:**
   The `log_rank_survival_analysis` function performs pairwise log-rank tests to compare survival distributions between different tumor stages.
## Usage
You can explore the detailed analysis by reviewing the notebook provided in this repository. 
If you prefer to run the analysis programmatically, you can use the functions provided in cancer_analysis.py.

## Results

![image](https://github.com/user-attachments/assets/2c98b259-f6cd-49f0-a510-831601987a03)

![image](https://github.com/user-attachments/assets/5b6c8d24-3e49-4435-9ae7-7b1e76d3070e)


