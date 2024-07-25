import pandas as pd
import os
import re

# Directory where the CSV files are located
directory_csv = r'C:\Users\morsh\Desktop\Casa DIgital\Data_Science_Project_-_Challenge_2\ship_project\input_csv'

# Directory where the output CSV file will be saved
directory_output = r'C:\Users\morsh\Desktop\Casa DIgital\Data_Science_Project_-_Challenge_2\ship_project\output_csv'

# List to store the ship types found
found_types = set()

# Function to extract the ship type from the ship name
def extract_type(name):
    # Remove letters A, B, C, D, E after the first name
    parts = name.split()
    if len(parts) > 1:
        first_name = parts[0]
        type_part = parts[1]
        # Remove letters A, B, C, D, E from the type part
        type_part = re.sub(r'[ABCDE]', '', type_part).strip()
        return f"{first_name} {type_part}".strip()
    return name.strip()

# Function to process CSV files
def process_csv_files(directory_csv):
    for file in os.listdir(directory_csv):
        if file.startswith('navio_') and file.endswith('.csv'):
            file_path = os.path.join(directory_csv, file)
            try:
                df = pd.read_csv(file_path)
                
                if 'Nome do Navio' in df.columns:
                    for ship_name in df['Nome do Navio']:
                        type_part = extract_type(ship_name)
                        if type_part:
                            found_types.add(type_part)
            except Exception as e:
                print(f"Error processing file {file}: {e}")

# Process CSV files
process_csv_files(directory_csv)

# Create DataFrame with the found types and their IDs
df_types = pd.DataFrame({
    'ID': range(1, len(found_types) + 1),
    'Type': list(found_types)
})

# Ensure the output directory exists
if not os.path.exists(directory_output):
    os.makedirs(directory_output)

# Complete path for the output CSV file
output_file_path = os.path.join(directory_output, 'tipos_navios.csv')

# Save DataFrame as a CSV file
df_types.to_csv(output_file_path, index=False)

print(f"File tipos_navios.csv created successfully at {output_file_path}!")
