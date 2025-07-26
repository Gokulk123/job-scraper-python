#Imports the pandas library, used for working with tabular data (like CSV files).
# It helps you store job data in a DataFrame (like a table) and save it easily.
import pandas as pd

#Imports the fetch_jobs function from your custom module scraper/fake_jobs_scraper.py.
# This function is responsible for scraping or fetching job data from the fake jobs website.
from scraper.fake_jobs_scraper import fetch_jobs

# Calls the fetch_jobs() function and stores the result (a list of job dictionaries) into the variable jobs.
# Each job is a dictionary.
jobs = fetch_jobs()

print(f"✅ Total jobs scraped: {len(jobs)}")

if jobs:
    # Converts the list of dictionaries into a Pandas DataFrame, which looks like a table (rows and columns).
    df = pd.DataFrame(jobs)
    # Saves the DataFrame to a CSV file in the data/ folder.
    df.to_csv("data/jobs_2025_07.csv", index=False)
    print("✅ CSV saved successfully.")
else:
    print("⚠️ No jobs found.")
