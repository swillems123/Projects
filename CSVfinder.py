import pandas as pd
import zipfile

# Path to the ZIP file
zip_file_path = r'C:\Users\sethw\OneDrive\Documents\Projects\archive.zip'

# Name of the CSV file inside the ZIP archive
csv_file_name = 'toprankedanime.csv'  # Replace with the actual CSV file name inside the ZIP

# Open the ZIP file and read the CSV file
with zipfile.ZipFile(zip_file_path, 'r') as z:
	with z.open(csv_file_name) as f:
		df = pd.read_csv(f)

# Filter the dataset for "Finished Airing" status
finished_airing_animes = df[df['status'] == 'Finished Airing']

# Count the number of animes with "Finished Airing" status
count_finished_airing = finished_airing_animes.shape[0]

# Print the result
print(f'The number of animes that are "Finished Airing": {count_finished_airing}')



