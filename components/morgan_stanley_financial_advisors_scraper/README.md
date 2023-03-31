
# MorganStanleyFinancialAdvisorsScraper

This component is a workflow designed to scrape financial advisor contact information from the Morgan Stanley website and insert the structured data into a Google Sheet. The workflow starts by taking the base URL of the Morgan Stanley website as input and retrieves a list of financial advisors with their contact information. It then processes the data and arranges it in a structured format before inserting it into a Google Sheet, whose URL is provided as output.

## Initial generation prompt
description: "IOs - InputBaseModels:\n- description: Input model containing the base\
  \ URL of the Morgan Stanley website to\n    scrape.\n  name: ScraperInput\nOutputBaseModels:\n\
  - description: Output model containing the Google Sheet's URL where the structured\n\
  \    contact information of each financial advisor is inserted.\n  name: GoogleSheetOutput\n"
name: MorganStanleyFinancialAdvisorsScraper


## Transformer breakdown
- Execute the transform of the AbstractWorkflow
- Prepare the Output BaseModel

## Parameters
[]

        