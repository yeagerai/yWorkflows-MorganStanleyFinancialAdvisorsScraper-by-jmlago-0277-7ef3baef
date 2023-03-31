
import os
from typing import Any, Dict, List

from dotenv import load_dotenv
from fastapi import FastAPI
from google.oauth2 import service_account
from googleapiclient import errors, discovery
from pydantic import BaseModel

from core.abstract_component import AbstractComponent


class GoogleSheetsWriterInputDict(BaseModel):
    structured_contact_info: List[Dict[str, Any]]
    google_sheet_id: str


class GoogleSheetsWriterOutputDict(BaseModel):
    GoogleSheetOutput: str


class GoogleSheetsWriter(AbstractComponent):
    def __init__(self) -> None:
        super().__init__()

    def transform(
        self, args: GoogleSheetsWriterInputDict
    ) -> GoogleSheetsWriterOutputDict:
        # 1. Authenticate with Google API Python client
        creds = service_account.Credentials.from_service_account_file(
            os.environ.get("GOOGLE_APPLICATION_CREDENTIALS"),
            scopes=["https://www.googleapis.com/auth/spreadsheets"],
        )

        # 2. Initialize Google Sheets API service instance
        service = discovery.build("sheets", "v4", credentials=creds)

        # 3. For each contact in structured_contact_info
        for contact in args.structured_contact_info:
            # a. Append contact data to the specified Google Sheet
            range_name = "Sheet1!A1"
            values = [list(contact.values())]
            body = {"values": values}

            try:
                result = (
                    service.spreadsheets()
                    .values()
                    .append(
                        spreadsheetId=args.google_sheet_id,
                        range=range_name,
                        valueInputOption="RAW",
                        insertDataOption="INSERT_ROWS",
                        body=body,
                    )
                    .execute()
                )
            except errors.HttpError as error:
                print(f"An error occurred while writing to the sheet: {error}")

        # 4. Retrieve the Google Sheet URL
        sheet_metadata = service.spreadsheets().get(spreadsheetId=args.google_sheet_id).execute()
        sheet_url = sheet_metadata["spreadsheetUrl"]

        # 5. Return GoogleSheetOutput (Google Sheet URL)
        return GoogleSheetsWriterOutputDict(GoogleSheetOutput=sheet_url)


load_dotenv()
google_sheets_writer_app = FastAPI()


@google_sheets_writer_app.post("/transform/")
async def transform(
    args: GoogleSheetsWriterInputDict,
) -> GoogleSheetsWriterOutputDict:
    google_sheets_writer = GoogleSheetsWriter()
    return google_sheets_writer.transform(args)

