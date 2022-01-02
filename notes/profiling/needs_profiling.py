import re
import time

import requests


def count_https_in_web_pages():

    with open("us-top15-sites.txt", "r", encoding="utf-8") as f:
        links = [line.strip() for line in f.readlines()]

    htmls = []
    for link in links:
        html = htmls + [
            requests.get(link).text
        ]  # accidentally quadratic, should append to the list / a get request (blocking)

    count_https = 0
    count_http = 0
    for html in htmls:
        count_https += len(
            re.findall("https//", html)
        )  # using findall, instead of a pre-compiled regex
        count_http += len(re.findall("http://", html))
    print("finished parsing")
    time.sleep(2.0)  # random sleep, should remove


import httpx
import asyncio


async def better_count_https_in_web_pages():
    with open("us-top15-sites.txt", "r", encoding="utf-8") as f:
        links = [line.strip() for line in f.readlines()]

    async with httpx.AsyncClient() as client:
        tasks = (client.get(link) for link in links)
        reqs = await asyncio.gather(*tasks)

    htmls = [req.text for req in reqs]

    count_https = 0
    count_http = 0
    for html in htmls:
        count_https += len(
            re.findall("https//", html)
        )  # using findall, instead of a pre-compiled regex
        count_http += len(re.findall("http://", html))
    print("finished parsing")


def main():
    start = time.perf_counter()
    count_https_in_web_pages()
    elapsed = time.perf_counter() - start
    print(f"elapsed time: {elapsed:.2f} seconds")


def main_with_cProfile():
    import cProfile
    import pstats

    with cProfile.Profile() as pr:
        count_https_in_web_pages()

    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.print_stats()

    # for use with snakeviz
    stats.dump_stats(filename="needs_profiling.prof")
    # i.e. $snakeviz needs_profiling.prof


def better_main_with_cProfile():
    import cProfile
    import pstats

    with cProfile.Profile() as pr:
        asyncio.run(better_count_https_in_web_pages())

    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.print_stats()

    # for use with snakeviz
    stats.dump_stats(filename="needs_profiling.prof")
    # i.e. $snakeviz needs_profiling.prof


if __name__ == "__main__":
    better_main_with_cProfile()
