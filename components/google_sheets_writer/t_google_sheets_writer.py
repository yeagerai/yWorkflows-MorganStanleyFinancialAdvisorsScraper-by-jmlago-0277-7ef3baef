
import os
from unittest.mock import MagicMock

import pytest
from google.oauth2 import service_account
from googleapiclient import errors, discovery

from your_path_to_component import (
    GoogleSheetsWriter,
    GoogleSheetsWriterInputDict,
    GoogleSheetsWriterOutputDict,
)

# Disable network calls for test cases
discovery.build = MagicMock()

# Test cases with mocked input and expected output
test_cases = [
    (
        GoogleSheetsWriterInputDict(
            structured_contact_info=[{"Name": "John Doe", "Email": "john.doe@example.com"}],
            google_sheet_id="test_sheet_id",
        ),
        GoogleSheetsWriterOutputDict(GoogleSheetOutput="https://docs.google.com/spreadsheets/d/test_sheet_id"),
    ),
    (
        GoogleSheetsWriterInputDict(
            structured_contact_info=[{"Name": "Jane Doe", "Email": "jane.doe@example.com"}],
            google_sheet_id="another_test_sheet_id",
        ),
        GoogleSheetsWriterOutputDict(GoogleSheetOutput="https://docs.google.com/spreadsheets/d/another_test_sheet_id"),
    ),
]

# Use parametrize to create multiple test scenarios
@pytest.mark.parametrize("input_data, expected_output", test_cases)
def test_google_sheets_writer(input_data, expected_output):
    # Set the mock for service_account.Credentials.from_service_account_file()
    service_account.Credentials.from_service_account_file = MagicMock(
        return_value=MagicMock()
    )

    # Set the mock for service.spreadsheets().values().append
    discovery.build().spreadsheets().values().append = MagicMock()

    # Set the mock for service.spreadsheets().get
    discovery.build().spreadsheets().get = MagicMock(
        return_value=MagicMock(
            execute=lambda: {
                "spreadsheetId": input_data.google_sheet_id,
                "spreadsheetUrl": f"https://docs.google.com/spreadsheets/d/{input_data.google_sheet_id}",
            }
        )
    )

    # Instantiate GoogleSheetsWriter
    google_sheets_writer = GoogleSheetsWriter()

    # Call transform() method and assert output
    output = google_sheets_writer.transform(input_data)
    assert output == expected_output

# Additional test scenarios, for example error handling, can be added as new test functions
def test_google_sheets_writer_http_error():
    # Set the mock for service_account.Credentials.from_service_account_file()
    service_account.Credentials.from_service_account_file = MagicMock(
        return_value=MagicMock()
    )

    # Set the mock for service.spreadsheets().values().append to raise HttpError
    discovery.build().spreadsheets().values().append = MagicMock(
        side_effect=errors.HttpError("Http error occurred", None)
    )

    input_data = GoogleSheetsWriterInputDict(
        structured_contact_info=[{"Name": "John Doe", "Email": "john.doe@example.com"}],
        google_sheet_id="test_sheet_id",
    )

    # Instantiate GoogleSheetsWriter
    google_sheets_writer = GoogleSheetsWriter()

    # Call transform() method and expect no exceptions
    try:
        google_sheets_writer.transform(input_data)
    except errors.HttpError:
        pytest.fail("transform() should handle HttpError")
