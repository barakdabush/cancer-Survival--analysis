import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from lifelines.statistics import pairwise_logrank_test
from lifelines import KaplanMeierFitter


def pre_process(df):

    n = len(df)
    # Count the number of occurrences of "---" in each column
    counts = df.isin(["'--", "not reported"]).sum()
    selected_columns = counts[counts < n * 0.9].index.tolist()
    df = df[selected_columns].copy()
    df.replace(
        ["'--","not reported"], pd.NA, inplace=True
    )  # Replace '--' with NaN values
    df["age_at_index"] = pd.to_numeric(df["age_at_index"], errors="coerce")
    df.fillna({'vital_status':'Alive'}, inplace=True)
    df["vital_status"]= df["vital_status"].apply(lambda x: 1 if x == "Dead" else 0)
    df=df.drop(columns=['ajcc_staging_system_edition','icd_10_code','days_to_diagnosis'])
    df.loc[123, "days_to_death"] = 0
    df["days_to_last_follow_up"] = pd.to_numeric(df["days_to_last_follow_up"], errors="coerce")
    df.loc[636, "days_to_last_follow_up"] = abs(df.loc[636, "days_to_last_follow_up"])
    df['days_to_death'] = df['days_to_death'].fillna(df['days_to_last_follow_up'])
    df = df.dropna(subset=['days_to_death'])
    df["days_to_death"] = pd.to_numeric(df["days_to_death"], errors="coerce")
    return df


def demographic_analysis(df):
    demographics_columns = ["case_id", "age_at_index", "ethnicity", "gender", "race"]
    demographics_df = df[demographics_columns]

    # Set up the plotting style
    sns.set_theme(style="whitegrid")

    # Plot the distribution of Age at Index
    plt.figure(figsize=(10, 6))
    sns.histplot(demographics_df["age_at_index"], bins=20, kde=True)
    plt.title("Distribution of Age at Index")
    plt.xlabel("Age at Index")
    plt.ylabel("Frequency")
    plt.grid(False)

    plt.show()

    # Plot the gender distribution
    plt.figure(figsize=(8, 6))
    sns.countplot(data=demographics_df, x="gender")
    plt.title("Gender Distribution")
    plt.xlabel("Gender")
    plt.ylabel("Count")
    plt.grid(False)
    plt.show()

    # Plot the ethnicity distribution
    plt.figure(figsize=(8, 6))
    sns.countplot(data=demographics_df, x="ethnicity")
    plt.title("Ethnicity Distribution")
    plt.xlabel("Ethnicity")
    plt.ylabel("Count")
    plt.grid(False)
    plt.show()

    # Plot the race distribution
    plt.figure(figsize=(12, 6))
    sns.countplot(data=demographics_df, x="race")
    plt.title("Race Distribution")
    plt.xlabel("Race")
    plt.ylabel("Count")
    plt.xticks(rotation=45)
    plt.grid(False)
    plt.show()


def kalman_meier_fitter_analysis(df):
    duration="age_at_index"
    duration='days_to_death'
    df[duration] = pd.to_numeric(df[duration], errors="coerce")
    T = df[duration]  # Time to event or censoring
    E=df["vital_status"]
    # Initialize the KaplanMeierFitter
    kmf = KaplanMeierFitter()

    # Plot survival function for each tumor stage
    plt.figure(figsize=(12, 8))
    total_patients = 0
    tumor_stages = []
    for stage in df["tumor_stage"].dropna().unique():
        if len(E[df["tumor_stage"] == stage]) >= 60:
            tumor_stages.append(stage)
            count_patients = len(E[df["tumor_stage"] == stage])
            total_patients += count_patients
            kmf.fit(
                T[df["tumor_stage"] == stage],
                event_observed=E[df["tumor_stage"] == stage],
                label=stage,
            )
            kmf.plot()
    plt.title(f"Survival Function by Tumor Stage ({total_patients} patients)")
    plt.xlabel("Time to Death from Diagnosis (days)")
    plt.ylabel("Survival Probability")
    plt.legend(title="Tumor Stage")
    plt.grid(True)
    plt.show()

    survival_tumor_stage_df = df[df["tumor_stage"].isin(tumor_stages)]
    return survival_tumor_stage_df


def log_rank_survival_analysis(df):
    duration='age_at_index'
    duration="days_to_death"
    E=df['vital_status']
    tumor_stages = df["tumor_stage"].unique()
    results = pairwise_logrank_test(df[duration], df["tumor_stage"], E)
    print("Pairwise Log-rank test results:")
    print(results.summary)
    # Extract p-values from the results
    p_values = results.p_value
    threshold = 0.05

    # Extract unique stages

    # Create an empty matrix to store the p-values
    p_value_matrix = np.zeros((len(tumor_stages), len(tumor_stages)))
    custom_order = {
        "stage i": 1,
        "stage iia": 2,
        "stage iiib": 3,
        "stage iiic": 4,
        "stage iv": 5,

    }
    # Sort the list according to the custom order
    tumor_stages = sorted(tumor_stages, key=lambda x: custom_order[x])

    # Populate the matrix with p-values for pairwise comparisons
    for i, stage_x in enumerate(tumor_stages):
        for j, stage_y in enumerate(tumor_stages):
            if j < i:  # Only fill lower triangle
                if (stage_x, stage_y) in results.name:
                    p_value_matrix[i, j] = p_values[
                        results.name.index((stage_x, stage_y))
                    ]
                elif (stage_y, stage_x) in results.name:
                    p_value_matrix[i, j] = p_values[
                        results.name.index((stage_y, stage_x))
                    ]
                else:
                    p_value_matrix[i, j] = np.nan
            else:
                p_value_matrix[i, j] = np.nan  # Fill upper triangle with NaN

    # Set the colors of the cells based on significance
    colors = [
        ["green" if p < threshold else "red" for p in row] for row in p_value_matrix
    ]

    # Plot the heatmap with custom colors
    plt.figure(figsize=(10, 8))
    plt.imshow(p_value_matrix, cmap="coolwarm", interpolation="nearest", vmin=0, vmax=1)
    plt.colorbar(label="p-value")
    plt.xticks(np.arange(len(tumor_stages)), tumor_stages, rotation=45)
    plt.yticks(np.arange(len(tumor_stages)), tumor_stages)
    plt.title("Pairwise Comparisons Between Tumor Stages")
    plt.xlabel("Stage Y")
    plt.ylabel("Stage X")
    plt.tight_layout()

    # Set the colors of the cells
    for i in range(len(tumor_stages)):
        for j in range(len(tumor_stages)):
            if j < i:  # Only fill lower triangle
                plt.text(
                    j,
                    i,
                    "{:.3f}".format(p_value_matrix[i, j]),
                    ha="center",
                    va="center",
                    color=colors[i][j],
                )
    plt.grid(False)
    plt.show()


def plot_feature_importance(importances,indices,features,ci):
    
    thr=0.001
    plt.figure(figsize=(14, 8))
    sns.barplot(y=features[indices], x=importances[indices],hue=features[indices],legend=False,palette="viridis")
    plt.axvline(x=thr, color='r', linestyle='--')
    plt.title(f'Feature Importances from Random Survival Forest (Permutation Importance). ci={ci:.3f}')
    plt.xlabel('Importance')
    plt.ylabel('Feature')
    plt.tight_layout()
    plt.show()



if __name__ == "__main__":
    
    file_path = r"C:\Users\aviga\pythonProject\cancer_homework\clinical.tsv"  # Update with your file path
    df = pd.read_csv(file_path, sep="\t")
    # Perform pre-processing
    df = pre_process(df)
    # demographic_analysis(df)
    survival_tumor_stage_df = kalman_meier_fitter_analysis(df)
    log_rank_survival_analysis(survival_tumor_stage_df)

