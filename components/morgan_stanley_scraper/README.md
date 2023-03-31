
# MorganStanleyScraper

This component scrapes the contact information of financial advisors from the Morgan Stanley website. It uses BeautifulSoup and requests library to navigate, find and extract the data.

## Initial generation prompt
description: 'This component scrapes the contact information of financial advisors
  from the Morgan Stanley website. It uses BeautifulSoup and requests library to navigate,
  find and extract the data. Inputs: ScraperInput(base_url). Outputs: List of dictionaries
  containing raw contact information.'
name: MorganStanleyScraper


## Transformer breakdown
- Initialize a session with requests
- Load the base_url using the session
- Instantiate BeautifulSoup with the loaded HTML content
- Find the relevant tags containing the contact information
- Extract the raw contact information from the tags
- Store the raw contact information in a list of dictionaries

## Parameters
[]

        