import asyncio
from pyppeteer import launch

async def asyncmain():
    browser = await launch()
    page = await browser.newPage()
    await page.goto('https://github.com/THE-CODING-GOGGLES')
    await page.screenshot({'path': "image.png", 'fullPage': 'true'})
    await browser.close()

def main():
    asyncio.get_event_loop().run_until_complete(asyncmain())


main()
