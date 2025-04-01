# Visits Farmer Bot

This project automates web visits using Selenium and Streamlit. It allows users to specify the URL and the number of visits directly in the Streamlit interface. Users can also choose whether to run the browser in headless mode or visible mode.

## Features

- Launches multiple scrapers in parallel with a 5-second interval between each.
- Simulates user interactions such as scrolling and clicking on the webpage.
- URL and visit count are configurable via the Streamlit interface.
- Option to run the browser in headless mode for faster execution.

## How to Use

1. Run the Streamlit interface:
   ```bash
   streamlit run streamlit_interface.py
   ```
2. Use the interface to:
   - Enter the URL to visit.
   - Specify the number of visits.
   - Choose the execution mode (headless or visible).
3. Click "Start Bot" to begin the automated visits.

## Requirements

- Python 3.12+
- Selenium
- Streamlit
- WebDriver Manager
- dotenv
- PyInstaller (for building executables)

## Installation

Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Building Executables

### Windows
Run the following command to build a Windows executable:
```bash
pyinstaller --onefile --noconsole streamlit_interface.py
```

### macOS
Run the following command to build a macOS app:
```bash
pyinstaller --onefile --windowed streamlit_interface.py
```
