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
    chrome_options.add_argument("--headless")  # Run in background
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")

    # Initialize WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Target URL
    url = "https://app.tophat.com/e/013778/lecture"

    # Run the bot for 1 hour (60 minutes) checking every 30 seconds
    end_time = time.time() + 3600  # 1 hour from now

    while time.time() < end_time:
        try:
            driver.get(url)
            time.sleep(5)  # Wait for the page to load

            # Look for the question wrapper class
            elements = driver.find_elements(By.CLASS_NAME, "QuestionWrapperstyles__Fieldset-sc-g4w8f0-3")

            if elements:
                print("✅ Question detected!")
                # Send a notification (Optional)
                # You can use an email, webhook, or desktop notification
            else:
                print("⏳ No question found, checking again in 30 sec...")

        except Exception as e:
            print(f"❌ Error: {e}")

        time.sleep(30)  # Wait before checking again

    # Close the browser after finishing
    driver.quit()
    print("✅ Done! 1-hour monitoring complete.")

