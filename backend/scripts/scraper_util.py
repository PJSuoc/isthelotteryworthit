import json, random, re, time
from pathlib import Path
from playwright.sync_api import sync_playwright, TimeoutError as PWTimeout

USERAGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:130.0) Gecko/20100101 Firefox/130.0"
BROWSER = "firefox" # setting this just in case I feel like making multi browser tricks
MONEY_RE = r"\$\s?[\d.,]+"          # must look like a dollar amount

class BlockedError(Exception):
    pass

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

def run_scraper(target_url, target_details, timeout_ms=20000):

    with sync_playwright() as playwright:
        browser, context = setup_scraper(playwright, USERAGENT, BROWSER)
        page = context.new_page()
        try:
            resp = page.goto(target_url, wait_until="domcontentloaded", timeout=timeout_ms)
            if resp and resp.status in (403, 429):
                raise BlockedError(f"HTTP {resp.status}")

            # Wait until the element exists AND its text looks like a dollar amount
            page.wait_for_function(
                """([sel, pat]) => {
                    const el = document.querySelector(sel);
                    return !!el && new RegExp(pat).test(el.textContent);
                }""",
                arg=[target_details, MONEY_RE],
                timeout=timeout_ms,
            )
            return page.locator(target_details).first.inner_text().strip()
        except Exception:
            # Save evidence of what the page actually looked like
            page.screenshot(path="last_failure.png")
            Path("last_failure.html").write_text(page.content(), encoding="utf-8")
            raise
        finally:
            browser.close()

def clean_number(scraped_number):

    if 'Million' in scraped_number:
        no_dollar = scraped_number.strip('$')
        amt, text = no_dollar.split()
        final_amt = amt + '000000'
        grand_prize = int(final_amt)
        return grand_prize