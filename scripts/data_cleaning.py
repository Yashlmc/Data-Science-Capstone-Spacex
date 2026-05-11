import pandas as pd
import numpy as np

def clean_data(df):
    # Example: Filling missing values for Payload Mass
    if 'payload_mass_kg' in df.columns:
        avg_payload = df['payload_mass_kg'].mean()
        df['payload_mass_kg'] = df['payload_mass_kg'].replace(np.nan, avg_payload)
    
    # Example: Creating the Class label (1 for success, 0 for failure)
    # This depends on the 'landing_outcome' column logic
    return df

if __name__ == "__main__":
    # Load your part 1 data
    try:
        df = pd.read_csv('../data/dataset_part_1.csv')
        cleaned_df = clean_data(df)
        print("Data cleaning complete.")
        # cleaned_df.to_csv('../data/dataset_part_2.csv', index=False)
    except FileNotFoundError:
        print("Dataset not found. Check your file paths.")