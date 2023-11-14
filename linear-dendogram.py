import pandas as pd
from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'data/teams.csv'  # Replace with your file path
teams_data = pd.read_csv(file_path)

# Selecting relevant features
features = ['int_overall', 'int_attack', 'int_midfield', 'int_defence', 'int_international_prestige']

# Filtering teams with 'int_international_prestige' > 4
filtered_teams = teams_data[teams_data['int_international_prestige'] > 4]

# Performing hierarchical clustering
Z = linkage(filtered_teams[features], method='ward')

# Plotting the dendrogram
plt.figure(figsize=(15, 8))
dendrogram(Z, labels=filtered_teams['str_team_name'].values, leaf_rotation=90, leaf_font_size=8)
plt.title('Hierarchical Clustering Dendrogram for Teams with International Prestige > 4')
plt.xlabel('Team Name')
plt.ylabel('Distance')
plt.show()

# File path for saving the image
png_file_path = 'chart/teams_dendrogram.png'

# Saving the plot as a PNG file
plt.savefig(png_file_path)
