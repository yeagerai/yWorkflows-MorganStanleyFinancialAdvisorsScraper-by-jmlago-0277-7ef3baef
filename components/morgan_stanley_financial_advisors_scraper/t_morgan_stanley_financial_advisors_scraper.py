
import typing
import pytest
from pydantic import ValidationError
from fastapi.testclient import TestClient
from .your_component_file import (
    MorganStanleyFinancialAdvisorsScraper,
    ScraperInput,
    GoogleSheetOutput,
    morgan_stanley_financial_advisors_scraper_app,
)

client = TestClient(morgan_stanley_financial_advisors_scraper_app)

# Define test cases and expected outputs
test_cases = [
    (
        {"base_url": "https://example.com"},
        GoogleSheetOutput(sheet_url="https://sheets.example.com/sheet1"),
    ),
    (
        {"base_url": "https://example.org"},
        GoogleSheetOutput(sheet_url="https://sheets.example.com/sheet2"),
    ),
]

# Test scenarios with parametrization
@pytest.mark.parametrize("input_data,expected_output", test_cases)
def test_morgan_stanley_financial_advisors_scraper(input_data, expected_output, mocker):
    # Mock the transform function with the expected outputs
    mocker.patch(
        'your_component_file.MorganStanleyFinancialAdvisorsScraper.transform',
        return_value=expected_output
    )

    # Initialize the component and call the transform() method
    scraper = MorganStanleyFinancialAdvisorsScraper()

    # Call the transform function
    result = scraper.transform(ScraperInput(**input_data), callbacks=None)

    # Verify that the returned output matches the expected output
    assert result.result() == expected_output

# Test for edge cases and error handling
def test_morgan_stanley_financial_advisors_scraper_invalid_base_url():
    with pytest.raises(ValidationError):
        ScraperInput(base_url="invalid-url")

def test_morgan_stanley_financial_advisors_scraper_app(input_data, expected_output, mocker):
    # Mock the transform function with the expected outputs
    mocker.patch(
        'your_component_file.MorganStanleyFinancialAdvisorsScraper.transform',
        return_value=expected_output
    )

    response = client.post("/transform/", json=input_data)
    assert response.status_code == 200
    assert response.json() == expected_output.dict()
