
# test_morgan_stanley_scraper.py

import pytest
from pydantic import BaseModel
from typing import List, Dict
from my_components.example.morgan_stanley_scraper import (
    MorganStanleyScraper,
    ScraperInput,
    ContactInformation,
)

# Define test cases
test_data = [
    (
        ScraperInput(base_url="https://example.com"),
        ContactInformation(
            raw_contact_data=[
                {
                    "name": "John Doe",
                    "phone": "+1 123-456-7890",
                    "email": "john.doe@example.com",
                },
                {
                    "name": "Jane Smith",
                    "phone": "+1 098-765-4321",
                    "email": "jane.smith@example.com",
                },
            ]
        ),
    ),
    (
        ScraperInput(base_url="https://example.com/empty"),
        ContactInformation(raw_contact_data=[]),
    ),
]

# Use @pytest.mark.parametrize for multiple test scenarios
@pytest.mark.parametrize("input_data, expected_output", test_data)
def test_morgan_stanley_scraper(input_data: BaseModel, expected_output: BaseModel, monkeypatch):
    
    def mock_get(*args, **kwargs):
        class MockResponse:
            def __init__(self, content, status_code):
                self.content = content
                self.status_code = status_code

            def raise_for_status(self):
                pass

        if args[0] == "https://example.com":
            return MockResponse(b'<html><head></head><body><div class="contact-information"><p class="name">John Doe</p><p class="phone">+1 123-456-7890</p><p class="email">john.doe@example.com</p></div><div class="contact-information"><p class="name">Jane Smith</p><p class="phone">+1 098-765-4321</p><p class="email">jane.smith@example.com</p></div></body></html>', 200)
        elif args[0] == "https://example.com/empty":
            return MockResponse(b"<html><head></head><body></body></html>", 200)

    # Use monkeypatch to replace requests.Session.get with the mock_get function
    monkeypatch.setattr("requests.Session.get", mock_get)

    # Instantiate the MorganStanleyScraper
    scraper = MorganStanleyScraper()

    # Call the transform() method with the mocked input data
    output = scraper.transform(input_data)

    # Assert that the returned data matches the expected output
    assert output == expected_output
