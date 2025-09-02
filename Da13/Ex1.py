import asyncio
import random

async def download_file(file_name):
    print(f"Starting download: {file_name}")
    await asyncio.sleep(random.randint(1, 5))
    print(f"Finished download: {file_name}")

async def main():
    files = ["file1.zip", "file2.zip", "file3.zip", "file4.zip"]
    tasks = [download_file(file) for file in files]
    await asyncio.gather(*tasks)

asyncio.run(main())
