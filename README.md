# Cancer Survival Analysis

This repository contains scripts and functions for conducting survival analysis on a cancer dataset. The primary focus is on analyzing survival rates based on various demographic and clinical factors, such as tumor stage, gender, ethnicity, and race.

## Table of Contents

- [Project Overview](#project-overview)
- [File Structure](#file-structure)
- [Installation](#installation)
- [Functions Overview](#functions-overview)
- [Usage](#usage)
- [Results](#results)


## Project Overview

This project conducts a thorough survival analysis on a clinical dataset using both traditional statistical methods and machine learning techniques. The analysis is structured into the following key components:

- **Data Pre-processing and Visualization**
  - **Data Pre-processing**: Handles categorical variables to prepare the dataset for analysis.
  - **Visualization**: Displays demographic distributions to gain insights into the dataset.

- **Kaplan-Meier Estimator and Log-rank Test**
  - **Kaplan-Meier Estimator**: Estimates survival functions to evaluate survival probabilities over time.
  - **Log-rank Test**: Compares survival rates across different tumor stages to identify significant differences.

- **Random Survival Forest (RSF) Model**
  - **Model Training**: Trains the RSF model on the clinical data to predict survival times.
  - **Performance Evaluation**: Assesses model performance using the concordance index.
  - **Feature Importance**: Identifies important features through permutation importance.
  - **Feature Reduction**: Reduces the feature set based on importance scores and retrains the model to enhance interpretability.


## File Structure

- `clinical.tsv`: The dataset containing clinical information of cancer patients.
- `cancer_analysis.py`: The main script containing all functions for data processing, analysis, and visualization.
- `cancer_analysis.ipynb`: Notebook with comprehensive analysis and visualizations for the entire project.
- `README.md`: Project documentation.

## Installation

1. Clone this repository to your local machine:
    ```bash
    git clone https://github.com/barakdabush/cancer-survival-analysis.git
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

5. **plot_feature_importance:**
   The `plot_feature_importance` function visualizes feature importances from a Random Survival Forest model as a horizontal bar plot.
   
## Usage
You can explore the detailed analysis by reviewing the notebook provided in this repository. 
If you prefer to run the analysis programmatically, you can use the functions provided in cancer_analysis_functions.py.

## Results

![image](https://github.com/user-attachments/assets/2c98b259-f6cd-49f0-a510-831601987a03)

![image](https://github.com/user-attachments/assets/5b6c8d24-3e49-4435-9ae7-7b1e76d3070e)
