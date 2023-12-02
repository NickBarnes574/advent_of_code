"""
web_utilities.py - A module for fetching data from webpages and saving it to local files.
"""

import requests


def fetch_webpage_and_save(url, filename, timeout=10):
    """
    Fetch data from a webpage and save it to a local file.

    Args:
        url (str): The URL of the webpage to fetch.
        filename (str): The name of the local file to save the data.
        timeout (int): Timeout for the HTTP request in seconds (default is 10 seconds).

    Raises:
        requests.exceptions.HTTPError: If an HTTP error occurs.
        requests.exceptions.RequestException: If a request error occurs.
        IOError: If an IO error occurs while writing to the file.

    Returns:
        None
    """
    try:
        # Make an HTTP request to the webpage with a specified timeout
        response = requests.get(url, timeout=timeout)

        # Check the response status
        response.raise_for_status()

        # Extracted data (you can replace this with your data extraction logic)
        extracted_data = response.text

        # Write data to the specified file with encoding specified
        with open(filename, "w", encoding="utf-8") as file:
            file.write(extracted_data)

        print(f"Data from {url} successfully saved to {filename}")
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    except IOError as io_err:
        print(f"IO error occurred while writing to {filename}: {io_err}")
