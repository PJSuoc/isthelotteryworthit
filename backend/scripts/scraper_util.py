
from bs4 import BeautifulSoup # type: ignore
from playwright.sync_api import sync_playwright, Playwright # type: ignore
import requests # type: ignore

USERAGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36"
BROWSER = "firefox" # setting this just in case I feel like making multi browser tricks



def setup_scraper(USERAGENT, BROWSER, playwright: Playwright):

    if BROWSER == "firefox":
        browser = playwright.firefox

    base_prep = browser.launch(
        headless = True,
        args = ["--disable-blink-features=AutomationControlled"]
    )
    contextualized = base_prep.new_context(
        user_agent = USERAGENT,
        viewport = {"width": 1920, "height": 1080},
        locale = "en-US",
        timezone_id = "America/Chicago",
    )
    return contextualized

def run_scraper(target_url, target_details):

    browser = setup_scraper(USERAGENT, BROWSER)

    try:
        page = browser.new_page()
        page.goto(target_url, wait_until = 'networkidle')

        result = page.locator(target_details).inner_text()

        browser.close()
        return result
    except:
        browser.close()
        return "Scrape Failed"