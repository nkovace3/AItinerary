import asyncio

from apscheduler.schedulers.blocking import BlockingScheduler

from services.pipeline import run_ingestion

scheduler = BlockingScheduler()

@scheduler.scheduled_job("interval", seconds=10)
def scheduled_ingestion():
    print("Starting scheduled ingestion...")
    asyncio.run(run_ingestion())
    print("Scheduled ingestion complete.")

if __name__ == '__main__':
    print("Scheduler started.")
    scheduler.start()