
from bs4 import BeautifulSoup # type: ignore
from playwright.sync_api import sync_playwright, Playwright # type: ignore
import requests # type: ignore
import traceback

USERAGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:130.0) Gecko/20100101 Firefox/130.0"
BROWSER = "firefox" # setting this just in case I feel like making multi browser tricks



def setup_scraper(playwright, USERAGENT, BROWSER):

    if BROWSER == "firefox":
        browser = playwright.firefox

    base_browser = browser.launch(
        headless = True,
        args = ["--disable-blink-features=AutomationControlled"]
    )
    contextualized = base_browser.new_context(
        user_agent = USERAGENT,
        viewport = {"width": 1920, "height": 1080},
        locale = "en-US",
        timezone_id = "America/Chicago",
    )
    return base_browser, contextualized

def run_scraper(target_url, target_details):

    with sync_playwright() as playwright:
        browser, context = setup_scraper(playwright, USERAGENT, BROWSER)

        try:
            page = context.new_page()
            page.goto(target_url, wait_until = 'domcontentloaded')

            result = page.locator(target_details).inner_text()

            browser.close()
            return result
        except Exception as e:
            print(f"[UNEXPECTED ERROR] {target_url} -> {type(e).__name__}: {e}")
            traceback.print_exc()
            return f"Scrape Failed: unexpected {type(e).__name__} - {e}"
        finally:
            browser.close()

def clean_number(scraped_number):

    if 'Million' in scraped_number:
        no_dollar = scraped_number.strip('$')
        amt, text = no_dollar.split()
        final_amt = amt + '000000'
        grand_prize = int(final_amt)
        return grand_prize