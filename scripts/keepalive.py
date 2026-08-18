import asyncio
import sys

from playwright.async_api import async_playwright

PORTFOLIO_URL = "https://portfolio-kunalsoyane.streamlit.app/"
WAKE_BUTTON_TEXT = "Yes, get this app back up!"


async def keep_awake(url: str) -> bool:
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        try:
            page = await browser.new_page()
            await page.goto(url, wait_until="domcontentloaded", timeout=120_000)
            await page.wait_for_timeout(5_000)

            wake_button = page.get_by_role("button", name=WAKE_BUTTON_TEXT)
            if await wake_button.count() > 0:
                print(f"Sleeping — clicking wake button: {url}")
                await wake_button.click()
                await page.wait_for_timeout(60_000)
                print("Woken up.")
            else:
                print(f"Already awake: {url}")
            return True
        except Exception as exc:
            print(f"Failed to reach {url}: {exc}", file=sys.stderr)
            return False
        finally:
            await browser.close()


if __name__ == "__main__":
    ok = asyncio.run(keep_awake(PORTFOLIO_URL))
    sys.exit(0 if ok else 1)