markdown
# Component Name
MorganStanleyScraper

# Description
MorganStanleyScraper is a component in a Yeager Workflow designed to scrape contact information from a given base_url of a Morgan Stanley website. The component is a Python class that inherits from the AbstractComponent base class and implements the transform() method for processing input data.

# Input and Output Models
## Input Model
The component accepts an input model called `ScraperInput` that contains one property:
- `base_url`: (str) The base URL of the Morgan Stanley web page from which contact information will be scraped.

## Output Model
The component returns an output model called `ContactInformation` that contains one property:
- `raw_contact_data`: (List[Dict]) A list of dictionaries representing the contact details extracted from the base_url.

# Parameters
There are no parameters for the MorganStanleyScraper component.

# Transform Function
The `transform()` method takes the `ScraperInput` model as a parameter and returns the `ContactInformation` model as output. The method is implemented as follows:

1. Initialize a session with the `requests` library.
2. Load the `base_url` using the created session and store the response.
3. Instantiate BeautifulSoup with the loaded HTML content.
4. Find the relevant tags containing the contact information within the HTML.
5. Extract the raw contact information from the found tags and store it in a list of dictionaries.
6. Create the `ContactInformation` output model with the raw contact data and return it.

# External Dependencies
The component relies on the following external libraries:
- `fastapi`: Provides the FastAPI class for creating APIs.
- `requests`: Handles HTTP requests to interact with web pages.
- `beautifulsoup4`: Parses HTML and XML documents for web scraping.

# API Calls
The MorganStanleyScraper component makes a single external API call using the `requests` library to the provided `base_url`. The purpose of the API call is to fetch the HTML content of the page, which is then used by the BeautifulSoup library for web scraping.

# Error Handling
As the component uses the `requests` library to load the `base_url`, it can handle the standard HTTP errors that may arise during the request. Any non-200 status code will raise the appropriate error from the `requests` library.

Exceptions related to BeautifulSoup or any other part of the transform are not explicitly handled within this component. These exceptions will be raised as they occur, and it is the responsibility of the parent Yeager Workflow to handle these errors if necessary.

# Examples
Below is an example of how to use the MorganStanleyScraper component within a Yeager Workflow:

