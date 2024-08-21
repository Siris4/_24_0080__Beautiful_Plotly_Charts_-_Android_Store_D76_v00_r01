import pandas as pd

# Load the CSV file into a DataFrame
file_path = r'C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0080__Day76_Beautiful_Plotly_Charts_&_Android_Store__240820\NewProject\r00-r09 START\r00_env_START\apps.csv'
df = pd.read_csv(file_path)

# Remove the columns "Last_Updated" and "Android_Ver"
df = df.drop(columns=["Last_Updated", "Android_Ver"])

# Count the number of rows with NaN in the "Rating" column
nan_count_in_rating = df["Rating"].isna().sum()

# Create a new DataFrame that excludes rows with NaN values in the "Rating" column
df_apps_clean = df.dropna(subset=["Rating"])

# Get the shape of the cleaned DataFrame
df_apps_clean_shape = df_apps_clean.shape

# Print the number of rows with NaN in the "Rating" column
print("Number of rows with NaN in the 'Rating' column:", nan_count_in_rating)

# Print the shape of the cleaned DataFrame
print("Shape of df_apps_clean DataFrame:", df_apps_clean_shape)

# Display the first few rows of the cleaned DataFrame
print("First few rows of df_apps_clean:")
print(df_apps_clean.head())

# Display a random sample of rows from the cleaned DataFrame
print("Random sample of rows from df_apps_clean:")
print(df_apps_clean.sample(5))
