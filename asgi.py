from playwright.sync_api import sync_playwright
import os
from urllib.parse import urlparse
from django.conf import settings
from bs4 import BeautifulSoup


# ---------------------------
# DOM ANALYZER (BeautifulSoup)
# ---------------------------

def analyze_dom(html):

    soup = BeautifulSoup(html, "html.parser")

    forms = soup.find_all("form")
    buttons = soup.find_all("button")
    links = soup.find_all("a")
    images = soup.find_all("img")

    images_without_alt = []

    for img in images:
        if not img.get("alt"):
            images_without_alt.append(img.get("src"))

    return {
        "forms": len(forms),
        "buttons": len(buttons),
        "links": len(links),
        "images_without_alt": images_without_alt
    }


# ---------------------------
# MAIN WEBSITE TESTER
# ---------------------------

def test_website(url):

    report = {}

    broken_links = []
    visited_pages = []
    images_without_alt = []

    try:

        with sync_playwright() as p:

            browser = p.chromium.launch(headless=True)
            page = browser.new_page()

            page.goto(url, timeout=60000)

            domain = urlparse(url).netloc

            links = page.query_selector_all("a")
            internal_links = []

            for link in links:

                href = link.get_attribute("href")

                if href and href.startswith("http") and domain in href:
                    internal_links.append(href)

            pages_to_visit = [url] + internal_links[:4]

            total_buttons = 0
            total_forms = 0
            total_links = 0

            for page_url in pages_to_visit:

                try:

                    page.goto(page_url, timeout=60000)

                    visited_pages.append(page_url)

                    html = page.content()

                    dom_report = analyze_dom(html)

                    total_buttons += dom_report["buttons"]
                    total_forms += dom_report["forms"]
                    total_links += dom_report["links"]

                    images_without_alt.extend(dom_report["images_without_alt"])

                    page_links = page.query_selector_all("a")[:10]

                    for link in page_links:

                        href = link.get_attribute("href")

                        if href and href.startswith("http"):

                            try:

                                response = page.request.get(href)

                                if response.status >= 400:

                                    broken_links.append((href, response.status))

                            except:

                                broken_links.append((href, "Error"))

                except:
                    continue


            screenshot_path = os.path.join(settings.MEDIA_ROOT, "screenshot.png")

            page.goto(url)

            page.screenshot(path=screenshot_path, full_page=True)

            report["status"] = "Website Crawled Successfully"
            report["title"] = page.title()

            report["visited_pages"] = visited_pages

            report["total_buttons"] = total_buttons
            report["total_forms"] = total_forms
            report["total_links"] = total_links

            report["broken_links"] = broken_links
            report["broken_count"] = len(broken_links)

            report["images_without_alt"] = images_without_alt

            report["screenshot"] = settings.MEDIA_URL + "screenshot.png"

            browser.close()

    except Exception as e:

        report["status"] = "Error loading website"
        report["error"] = str(e)

    return report