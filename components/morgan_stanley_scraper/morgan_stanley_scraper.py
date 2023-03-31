
import os
from typing import List, Dict
from fastapi import FastAPI
from pydantic import BaseModel
import requests
from bs4 import BeautifulSoup

from core.abstract_component import AbstractComponent

    
class ScraperInput(BaseModel):
    base_url: str


class ContactInformation(BaseModel):
    raw_contact_data: List[Dict]


class MorganStanleyScraper(AbstractComponent):
    def __init__(self) -> None:
        super().__init__()

    def transform(self, args: ScraperInput) -> ContactInformation:
        print(f"Executing the transform of the {type(self).__name__} component...")

        # Initialize a session with requests
        session = requests.Session()

        # Load the base_url using the session
        response = session.get(args.base_url)

        # Instantiate BeautifulSoup with the loaded HTML content
        soup = BeautifulSoup(response.content, "html.parser")

        # Find the relevant tags containing the contact information
        contact_tags = soup.find_all("div", class_="contact-information")

        # Extract the raw contact information from the tags
        raw_contact_data = []
        for tag in contact_tags:
            contact_data = {}
            contact_data["name"] = tag.find("p", class_="name").text.strip()
            contact_data["phone"] = tag.find("p", class_="phone").text.strip()
            contact_data["email"] = tag.find("p", class_="email").text.strip()
            raw_contact_data.append(contact_data)

        # Store the raw contact information in a list of dictionaries
        output = ContactInformation(raw_contact_data=raw_contact_data)
        return output


morgan_stanley_scraper_app = FastAPI()


@morgan_stanley_scraper_app.post("/transform/")
async def transform(args: ScraperInput) -> ContactInformation:
    morgan_stanley_scraper = MorganStanleyScraper()
    return morgan_stanley_scraper.transform(args)

