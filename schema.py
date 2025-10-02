from pydantic import BaseModel, Field
from typing import List, Optional

class JobRequirement(BaseModel):
    category: str = Field(description="Category (e.g., 'Technical Skills', 'Experience')")
    items: List[str] = Field(description="List of requirements in this category")

class JobPosting(BaseModel):
    title: str = Field(description="Job title")
    company: str = Field(description="Company name")
    location: Optional[str] = Field(description="Job location")
    job_type: Optional[str] = Field(description="Employment type (full-time, part-time, etc.)")
    description: str = Field(description="Complete job description")
    must_have_requirements: List[JobRequirement] = Field(
        description="Essential qualifications and skills"
    )
    nice_to_have_requirements: List[JobRequirement] = Field(
        description="Preferred but optional qualifications"
    )
    responsibilities: List[str] = Field(description="Key job responsibilities")
    salary_range: Optional[str] = Field(description="Salary information if available")
    application_url: str = Field(description="URL to apply for the job")
