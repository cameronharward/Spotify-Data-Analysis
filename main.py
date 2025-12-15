import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv("track_data_final.csv")

# Question 1:
# Which artists have the highest average track popularity
# (minimum of 5 tracks)

# Group by artist and calculate track count and average popularity
artist_stats = df.groupby("artist_name").agg(
    track_count=("track_name", "count"),
    avg_popularity=("track_popularity", "mean")
)

# Keep only artists with at least 5 tracks
artist_stats = artist_stats[artist_stats["track_count"] >= 5]

# Sort artists by average popularity
top_artists = artist_stats.sort_values(
    by="avg_popularity",
    ascending=False
).head(10)

# Create a bar graph for the top artists
plt.figure()
top_artists["avg_popularity"].plot(kind="barh")
plt.title("Top 10 Artists by Average Track Popularity")
plt.xlabel("Average Track Popularity")
plt.ylabel("Artist")
plt.gca().invert_yaxis()
plt.show()

# Question 2:
# Do explicit tracks tend to be more popular?

# Group tracks by explicit flag and calculate average popularity
explicit_stats = df.groupby("explicit").agg(
    avg_popularity=("track_popularity", "mean")
)

# Sort by average popularity
explicit_stats = explicit_stats.sort_values(
    by="avg_popularity",
    ascending=False
)

# Create a bar graph comparing explicit and non-explicit tracks
plt.figure()
explicit_stats["avg_popularity"].plot(kind="bar")
plt.title("Average Track Popularity: Explicit vs Non-Explicit")
plt.xlabel("Explicit")
plt.ylabel("Average Track Popularity")
plt.show()

# Print tables to see the results
print(top_artists)
print(explicit_stats)
