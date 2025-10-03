from pydantic import BaseModel, Field
from typing import Optional

class JobPosting(BaseModel):
    title: str = Field(description="Job title")
    company: str = Field(description="Company name")
    location: Optional[str] = Field(default=None, description="Location")
    description: str = Field(description="Job description")
    requriement: str = Field(description="Job requirement, leave none if not mentioned")
    application_url: str = Field(description="Application URL")
