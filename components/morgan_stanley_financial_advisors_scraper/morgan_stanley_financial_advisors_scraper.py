
import typing
from typing import Optional
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

from core.workflows.abstract_workflow import AbstractWorkflow


class ScraperInput(BaseModel):
    base_url: str


class GoogleSheetOutput(BaseModel):
    sheet_url: str


class MorganStanleyFinancialAdvisorsScraper(AbstractWorkflow):
    def __init__(self) -> None:
        super().__init__()

    async def transform(
        self, args: ScraperInput, callbacks: typing.Any
    ) -> GoogleSheetOutput:
        results_dict = await super().transform(args=args, callbacks=callbacks)
        sheet_url = results_dict[0].sheet_url
        out = GoogleSheetOutput(sheet_url=sheet_url)
        return out


load_dotenv()
morgan_stanley_financial_advisors_scraper_app = FastAPI()


@morgan_stanley_financial_advisors_scraper_app.post("/transform/")
async def transform(
    args: ScraperInput,
) -> GoogleSheetOutput:
    morgan_stanley_financial_advisors_scraper = MorganStanleyFinancialAdvisorsScraper()
    return await morgan_stanley_financial_advisors_scraper.transform(args, callbacks=None)
