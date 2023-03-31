
# DataCleaner

This component takes the raw contact information dictionaries and cleans them to return structured data containing first name, last name, title, email, city, state, and phone number of each financial advisor.

## Initial generation prompt
description: 'This component takes the raw contact information dictionaries and cleans
  them to return structured data containing first name, last name, title, email, city,
  state, and phone number of each financial advisor. Inputs: List of raw contact information
  dictionaries from the MorganStanleyScraper component. Outputs: List of dictionaries
  with structured contact information.'
name: DataCleaner


## Transformer breakdown
- Step 1: Iterate through each raw contact dictionary.
- Step 2: Extract first name, last name, title, email, city, state, and phone number into separate variables.
- Step 3: Clean and normalize the values of the extracted variables.
- Step 4: Combine the cleaned and normalized values into a structured contact information dictionary.
- Step 5: Add the structured contact information dictionary to the output list.
- Step 6: Return the output list containing the dictionaries with structured contact information.

## Parameters
[]

        