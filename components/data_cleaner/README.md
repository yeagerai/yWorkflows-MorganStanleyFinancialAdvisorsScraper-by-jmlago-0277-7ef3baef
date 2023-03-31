markdown
# Component Name
DataCleaner

# Description
The DataCleaner component is designed to process and structure raw contact information dictionaries from the MorganStanleyScraper component. It extracts relevant fields from the input and returns a list of structured contact information dictionaries.

# Input and Output Models

## Input Model: DataCleanerInputDict
- `raw_contact_dictionaries` (List[Dict]): List of raw contact information dictionaries from the MorganStanleyScraper component. This field is mandatory.

## Output Model: DataCleanerOutputDict
- `structured_contact_information` (List[Dict]): List of dictionaries with structured contact information. This field is mandatory.

# Parameters
There are no parameters for this component.

# Transform Function

The transform() function of the DataCleaner component performs the following steps:

1. Initializes an empty list `structured_data` to store the structured contact information.
2. Iterates through each `raw_contact` in `args.raw_contact_dictionaries`.
3. Extracts and cleans the following variables (pseudo-code implementation is provided in the source code):
    - first_name, last_name
    - title
    - email
    - city, state
    - phone
4. Constructs a `structured_contact` dictionary from the extracted variables.
5. Appends the `structured_contact` dictionary to the `structured_data` list.
6. Returns the `DataCleanerOutputDict` with the `structured_contact_information` field set to the structured data.

# External Dependencies
- `List` and `Dict` are imported from the `typing` module for type hinting purposes.
- `FastAPI` is imported from the `fastapi` module to create an HTTP API for the DataCleaner component.
- `BaseModel` and `Field` are imported from the `pydantic` module to create input and output data models with validation.

# API Calls
There are no external API calls made by this component.

# Error Handling
Errors are not handled explicitly within the component. However, if the input data does not properly conform to the defined Pydantic models, a validation error will be thrown automatically by Pydantic.

# Examples

To use the DataCleaner component within a Yeager Workflow, you need to:

1. Instantiate the DataCleaner component:
