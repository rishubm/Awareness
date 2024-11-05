import json
from seleniumbase import SB
from selenium.webdriver.common.by import By

def seleniumbase_result(query):
    results = []

    # Use SeleniumBase's context manager
    with SB() as sb:
        # Open Google search with the query
        sb.open(f"https://www.google.com/search?q={query.replace(' ', '+')}")
        
        # Wait for results to load
        sb.wait_for_element("div#search")

        # Extract each result's title, URL, and snippet
        search_results = sb.find_elements("div.g")  # Google's main result container

        for result in search_results:
            # Initialize empty strings for each field
            title = ""
            url = ""
            snippet = ""

            # Try to extract the title
            try:
                title_element = result.find_element(By.TAG_NAME, "h3")
                title = title_element.text if title_element else ""
            except:
                title = ""

            # Try to extract the URL
            try:
                link_element = result.find_element(By.TAG_NAME, "a")
                url = link_element.get_attribute("href") if link_element else ""
            except:
                url = ""

            # Try to extract the snippet/description
            try:
                snippet_element = result.find_element(By.CLASS_NAME, "Hdw6tb")
                snippet = snippet_element.text if snippet_element else ""
            except:
                snippet = ""

            # Append to results
            results.append({
                "query": query,
                "title": title,
                "url": url,
                "snippet": snippet
            })

    # Save results to JSON file
    with open("./json/selenium_search_results.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=4)

# Runner for testing
if __name__ == "__main__":
    query = "Texas Convergent"
    seleniumbase_result(query)
