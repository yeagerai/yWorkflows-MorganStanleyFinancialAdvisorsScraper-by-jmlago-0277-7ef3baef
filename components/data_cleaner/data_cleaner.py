
import os
from typing import List, Dict
from fastapi import FastAPI
from pydantic import BaseModel, Field

from core.abstract_component import AbstractComponent


class DataCleanerInputDict(BaseModel):
    raw_contact_dictionaries: List[Dict] = Field(..., description="List of raw contact information dictionaries from the MorganStanleyScraper component.")


class DataCleanerOutputDict(BaseModel):
    structured_contact_information: List[Dict] = Field(..., description="List of dictionaries with structured contact information.")


class DataCleaner(AbstractComponent):
    def __init__(self) -> None:
        super().__init__()

    def transform(
        self, args: DataCleanerInputDict
    ) -> DataCleanerOutputDict:

        structured_data = []

        for raw_contact in args.raw_contact_dictionaries:
            first_name, last_name, title, email, city, state, phone = (None,) * 7

            # Extract and clean variables (pseudo-code)
            # first_name, last_name = extract_names(raw_contact)
            # title = extract_title(raw_contact)
            # email = extract_email(raw_contact)
            # city, state = extract_city_and_state(raw_contact)
            # phone = extract_phone(raw_contact)

            structured_contact = {
                "first_name": first_name,
                "last_name": last_name,
                "title": title,
                "email": email,
                "city": city,
                "state": state,
                "phone": phone,
            }

            structured_data.append(structured_contact)

        return DataCleanerOutputDict(structured_contact_information=structured_data)


data_cleaner_app = FastAPI()


@data_cleaner_app.post("/transform/")
async def transform(
    args: DataCleanerInputDict,
) -> DataCleanerOutputDict:
    data_cleaner = DataCleaner()
    return data_cleaner.transform(args)
