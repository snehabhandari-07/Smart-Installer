from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
from voice_assistant import speak

software_links = {
    "python": {
        "url": "https://www.python.org/downloads/",
        "steps": [
            {'xpath': '//*[@id="touchnav-wrapper"]/header/div/div[2]/div/div[2]/p/a'}
        ]
    },
    "git": {
        "url": "https://git-scm.com/downloads",
        "steps": [
            {'xpath': '//*[@id="main"]/div[1]/div[1]/div/table/tbody/tr[1]/td[2]/a'},
            {'xpath': '//*[@id="auto-download-link"]'}
        ]
    },
    "docker": {
        "url": "https://www.docker.com/products/docker-desktop/",
        "steps": [
            {'xpath': '//*[@id="post-29028"]/div/div/div/div[2]/div[1]/div/div[4]/div/section/div[1]'},
            {'xpath':'//*[@id="dkr_dd_hp_windows"]'}
        ]
    },
    "nodejs": {
        "url": "https://nodejs.org/en/download/",
        "steps": [
            {'xpath': '/html/body/div[1]/div[2]/main/section[1]/div[2]/a[1]'}
        ]
    },
    "java": {
        "url": "https://www.oracle.com/java/technologies/javase-downloads.html",
        "steps": [
            {'xpath': '//*[@id="rt01tab1-jdk23-windows"]'},
            {'xpath':'//*[@id="jdk23-windows"]/section/div/div/div/table/tbody/tr[3]/td[3]/div/a[1]'}
        ]
    },
    "postman": {
        "url": "https://www.postman.com/downloads/",
        "steps": [
            {'xpath': '//*[@id="download-the-app-windows-64"]'}
        ]
    },
    "vs code": {
        "url": "https://code.visualstudio.com/download",
        "steps": [
            {'xpath': '//*[@id="download-alt-win"]'}
        ]
    },
    "intellij": {
        "url": "https://www.jetbrains.com/idea/download/",
        "steps": [
            {'xpath': '//*[@id="download-block"]/section[2]/div/div/div[1]/div[2]/div[1]/div/div/div/span/a'}
        ]
    },
    "mysql": {
        "url": "https://dev.mysql.com/downloads/installer/",
        "steps": [
            {'xpath': '//*[@id="files"]/div/table/tbody/tr[1]/td[4]/div/a'},
            {'xpath' : '//*[@id="content"]/div/div/p[2]/b/a'}
        ]
    },
    "mongodb": {
        "url": "https://www.mongodb.com/try/download/community",
        "steps":[
            {'xpath':'//*[@id="community"]/div/div/div[5]/div[1]/span/a'}
        ]
    }
}


def setup_driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("prefs", {
        "download.prompt_for_download": False,  # Auto-download
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True,
        "download.default_directory": "C:\\Users\\Dell\\Downloads"  # Set your desired download path
    })
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

def install_software(software_name):
    """Automate the software download process using Selenium."""
    software = software_links.get(software_name.lower())

    if software:
        speak(f"Starting the download for {software_name}.")
        driver = setup_driver()
        driver.get(software["url"])

        try:
            for step in software["steps"]:
                xpath = step['xpath']
                # Wait until the element is clickable
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
                button = driver.find_element(By.XPATH, xpath)
                button.click()
                speak(f"Clicked a download step for {software_name}.")
                time.sleep(3)  # Small delay between steps

            speak(f"{software_name.capitalize()} download has started.")
            time.sleep(40)  # Wait to ensure download begins

        except Exception as e:
            speak(f"An error occurred while downloading {software_name}: {e}")
        finally:
            driver.quit()
    else:
        speak(f"Sorry, I don't have a download link for {software_name}.")

