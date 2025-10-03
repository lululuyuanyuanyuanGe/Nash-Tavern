from browser_use import Agent, Browser, ChatGoogle
from dotenv import load_dotenv
import asyncio
from schema import JobPosting

load_dotenv()

gemini_flash = ChatGoogle(model = "gemini-flash-latest")
lubrowser = Browser(executable_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
                    user_data_dir='C:\\Users\\yj200\\AppData\\Local\\Google\\Chrome\\User Data',
                    profile_directory='Profile 1',)

async def call_agent(job_url: str):
    agent = Agent(task= f"""
        Go to this job posting URL: {job_url}
        Extract the job description, job requirement, job title, location, employment type
        return these information in json format
        """,
        llm = gemini_flash,
        calculate_cost = True,
        browser = lubrowser)
    output = await agent.run()
    print("=======================")
    print(output)
    print("=======================")
    print(output.structured_output)
    return output.structured_output

async def scrape_job_schema(job_urls: list[str] = []):

    tasks = [call_agent(job_url) for job_url in job_urls]
    results = await asyncio.gather(*tasks, return_exceptions = True)

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
        "https://www.linkedin.com/jobs/collections/recommended/?currentJobId=4300704984"
    ]
    
    results = await scrape_job_schema(job_urls)
    print(type(results))
    print(results)
    
    for idx, job_data in results.items():
        if job_data:
            print("=========================================================")
            print(f"{idx}: {job_data}")  # Use f-string
if __name__ == "__main__":
    asyncio.run(main())