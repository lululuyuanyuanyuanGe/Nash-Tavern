from browser_use import Agent, Browser, ChatGoogle
from dotenv import load_dotenv
import asyncio
from schema import JobPosting

load_dotenv()

gemini_flash = ChatGoogle(model = "gemini-flash-latest")
async def call_agent(job_url: str):
    agent = Agent(task= f"""
        Go to this job posting URL: {job_url}
        
        Extract all relevant information about the job including:
        - Job title and company name
        - Job location and employment type
        - Complete job description
        - All requirements (both must-have and nice-to-have)
        - Key responsibilities
        - Salary information if mentioned
        - Application URL
        
        Organize requirements into categories like Technical Skills, 
        Experience, Education, Soft Skills, etc.
        """,
        llm = gemini_flash,
        output_model_schema = JobPosting)
    output = await agent.run()
    return output.structured_output

async def scrape_job_schema(job_urls: list[str] = []):

    tasks = [call_agent(job_url) for job_url in job_urls]
    results = asyncio.gather(*tasks, return_exceptions = True)

    structured_jobs_result = {}
    for i, result in enumerate(results):
        if isinstance(result, Exception):
            print(f"Error scraping job {i}: {result}")
            structured_jobs_result[i] = None
        else:
            structured_jobs_result[i] = result

    return structured_jobs_result
    
# Usage
async def main():
    job_urls = [
        "https://job-boards.greenhouse.io/oklo/jobs/5645116004"
    ]
    
    results = await scrape_job_schema(job_urls)
    
    for idx, job_data in results.items():
        if job_data:
            print(f"\nJob {idx}:")
            print(f"  Title: {job_data.title}")
            print(f"  Company: {job_data.company}")

if __name__ == "__main__":
    asyncio.run(main())

        


