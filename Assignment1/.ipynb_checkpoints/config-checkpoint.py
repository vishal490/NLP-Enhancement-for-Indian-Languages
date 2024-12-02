import os
# Get the directory path of the current script
current_directory = os.path.dirname(os.path.abspath(__file__))

# Define the relative path to the data folder
relative_data_folder = 'data'

# Define the path to the data folder relative to the current script
data_folder = os.path.join(current_directory, relative_data_folder)

# Now you can specify file paths within the data folder
file_path = os.path.join(data_folder, 'hi_100.txt')
