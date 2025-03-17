def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

# main method
if __name__ == '__main__':
    import time
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.chrome.options import Options
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.common.by import By

    # Configure Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # run in background
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")

    # Initialize the WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Target URL (update this as needed)
    url = "https://app.tophat.com/e/013778/lecture"
    driver.get(url)
    time.sleep(5)  # Wait for the page to load

    try:
        # Locate the question container using the class name.
        # Note: Sometimes you may need to use a CSS selector to match the full class string.
        container = driver.find_element(By.CSS_SELECTOR, "div.QuestionWrapperstyles__Fieldset-sc-g4w8f0-3.fIsVvR")

        # Attempt to extract the question text.
        # This assumes there's a child element that holds the text. Adjust the selector as necessary.
        try:
            question_text = container.find_element(By.CSS_SELECTOR, ".question-text").text
        except Exception:
            # If the inner element has no distinct class, you might need to adjust or get text directly.
            question_text = container.text.split("\n")[0]  # example fallback

        print("Question:", question_text)

        # Find all options (assumes options are <li> elements with class 'option')
        options = container.find_elements(By.CSS_SELECTOR, "li.option")

        if options:
            print("Options:")
            for idx, option in enumerate(options, start=1):
                print(f"  {idx}. {option.text}")
        else:
            print("No options found with the selector 'li.option'.")

        # OPTIONAL: If you want to select (click) an option, for example, option 2:
        if len(options) >= 2:
            print("Clicking on the second option...")
            options[1].click()
        else:
            print("Not enough options available to perform a click.")

    except Exception as e:
        print(f"Error while processing the question container: {e}")

    driver.quit()


