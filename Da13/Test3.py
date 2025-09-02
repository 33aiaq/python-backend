import asyncio
import random

async def download_file(file_name):
    print(f"Starting download: {file_name}")
    # simulate network delay with random sleep
    await asyncio.sleep(random.randint(1, 3))
    print(f"Finished download: {file_name}")

async def main():
    # list of files to "download"
    files = ["file1.zip", "file2.zip", "file3.zip"]

    # create tasks for concurrent execution
    tasks = [download_file(file) for file in files]

    # run all tasks at once
    await asyncio.gather(*tasks)

# run the async program
asyncio.run(main())
