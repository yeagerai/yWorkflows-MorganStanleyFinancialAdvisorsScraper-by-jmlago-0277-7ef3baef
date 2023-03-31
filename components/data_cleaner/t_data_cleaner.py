
import pytest
from pydantic import ValidationError
from typing import List, Dict
from data_cleaner import DataCleaner, DataCleanerInputDict, DataCleanerOutputDict

# Define test cases with mocked input and expected output data
test_data = [
    (  # Test Case 1: Normal input data
        DataCleanerInputDict(raw_contact_dictionaries=[
            {
                "contact": "John Doe",
                "title": "CEO",
                "email": "johndoe@example.com",
                "location": "New York, NY",
                "phone": "123-456-7890",
            },
            {
                "contact": "Jane Smith",
                "title": "CTO",
                "email": "janesmith@example.com",
                "location": "Los Angeles, CA",
                "phone": "987-654-3210",
            },
        ]),
        DataCleanerOutputDict(structured_contact_information=[
            {
                "first_name": "John",
                "last_name": "Doe",
                "title": "CEO",
                "email": "johndoe@example.com",
                "city": "New York",
                "state": "NY",
                "phone": "123-456-7890",
            },
            {
                "first_name": "Jane",
                "last_name": "Smith",
                "title": "CTO",
                "email": "janesmith@example.com",
                "city": "Los Angeles",
                "state": "CA",
                "phone": "987-654-3210",
            },
        ]),
    ),
    (  # Test Case 2: Empty input data
        DataCleanerInputDict(raw_contact_dictionaries=[]),
        DataCleanerOutputDict(structured_contact_information=[]),
    ),
]

# Use @pytest.mark.parametrize to create multiple test scenarios
@pytest.mark.parametrize("input_data, expected_output", test_data)
def test_data_cleaner_transform(input_data: DataCleanerInputDict, expected_output: DataCleanerOutputDict):
    # Initialize DataCleaner component
    data_cleaner = DataCleaner()

    # Call the `transform()` method
    output = data_cleaner.transform(input_data)

    # Assert that the output matches the expected output
    assert output == expected_output

def test_data_cleaner_invalid_input():
    # Invalid input data (missing fields)
    raw_input_data = {"contact": "John", "title": "CEO"}

    # Expect a validation error when attempting to parse invalid input data
    with pytest.raises(ValidationError):
        DataCleanerInputDict(**raw_input_data)
