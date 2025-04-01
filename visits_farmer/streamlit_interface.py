# streamlit_interface.py
import time
import threading
import streamlit as st
from scrapper import visit_url

# Streamlit interface for the Selenium-based bot
st.title("Automated Bot with Selenium and Streamlit")
st.write("This bot launches a scraper every 5 seconds (in parallel) until the selected number of visits is completed.")

# Input to define the URL to visit
url_to_visit = st.text_input("Enter the URL to visit:", value="https://google.com")

# Input to define the number of scrapers/visits
if url_to_visit:
    iterations = st.number_input("Enter the number of visits:", min_value=1, max_value=100, value=1, step=1)

    # Option to choose whether to show the browser execution or run in headless mode
    show_execution = st.checkbox("Show execution (browser visible)", value=False)

    if st.button("Start Bot"):
        st.info("The bot is running...")
        threads = []
        # Launch scrapers in parallel with a 5-second interval
        for i in range(iterations):
            st.write(f"Starting scraper {i+1} of {iterations}")
            thread = threading.Thread(target=visit_url, args=(url_to_visit, show_execution))
            thread.start()
            threads.append(thread)
            time.sleep(5)  # Wait before starting the next scraper
        # Wait for all scrapers to complete
        for thread in threads:
            thread.join()
        st.success("All scrapers have completed their visits!")

# Automatically run Streamlit if the script is executed directly (for the .exe version)
if __name__ == '__main__':
    import sys, os, tempfile
    import streamlit.web.cli as stcli
    # If running as a bundled executable, sys.frozen will be True.
    if getattr(sys, 'frozen', False):
        # Running as a bundled executable; create a temporary .py file for Streamlit to run.
        try:
            with open(__file__, "rb") as f:
                code = f.read()
        except Exception as e:
            code = b""
        with tempfile.NamedTemporaryFile(suffix=".py", delete=False) as tmp:
            tmp.write(code)
            tmp_filename = tmp.name
        sys.argv = ["streamlit", "run", tmp_filename]
        sys.exit(stcli.main())
    else:
        sys.argv = ["streamlit", "run", __file__]
        sys.exit(stcli.main())
