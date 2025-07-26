# Imports the requests library – used to send HTTP requests (like opening a webpage in code)
import requests
# Imports BeautifulSoup from bs4 – it parses (analyzes) HTML/XML so that you can extract specific parts like <div>, <p>, etc.
from bs4 import BeautifulSoup

# Defines a function named fetch_jobs that takes a default URL (of the fake jobs site).
def fetch_jobs(url="https://realpython.github.io/fake-jobs/"):

    # Sends an HTTP GET request to the given url and stores the result (HTML + metadata) in the response object.
    response = requests.get(url)

    # Checks if the HTTP status code is not 200 (which means "OK").
    # If the site didn't load successfully, it prints an error and returns an empty list.
    if response.status_code != 200:
        print("❌ Failed to fetch jobs:", response.status_code)
        return []
    
    # Loads the response HTML into BeautifulSoup using the built-in html.parser.
    soup = BeautifulSoup(response.text, "html.parser")

    # Creates an empty list jobs to store job data (each job will be a dictionary).
    jobs = []

    # Finds all job listings on the page.Each job is wrapped in a <div class="card-content">.
    job_cards = soup.find_all("div", class_="card-content")
    print(f"🔍 Found {len(job_cards)} job cards.")

    # Loops through each job card one by one.
    for card in job_cards:

        # Finds the job title in an <h2 class="title"> tag. .text.strip() removes extra spaces or newlines.
        title = card.find("h2", class_="title").text.strip()

        # Extracts the company name inside an <h3 class="company">.
        company = card.find("h3", class_="company").text.strip()

        # Extracts the job location inside a <p class="location"> tag.
        location = card.find("p", class_="location").text.strip()

        # Adds a dictionary of the extracted job info into the jobs list.
        jobs.append({
            "title": title,
            "company": company,
            "location": location
        })

    # After the loop, returns the full list of job dictionaries back to the caller.
    return jobs
