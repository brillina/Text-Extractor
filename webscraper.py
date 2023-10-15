import hashlib
import io
from pathlib import Path
import pandas as pd
import requests
from bs4 import BeautifulSoup
from PIL import Image
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=sign+black+text+on+white+background&_sacat=0&LH_TitleDesc=0&_odkw=sign&_osacat=0")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
results = []
content = driver.page_source
soup = BeautifulSoup(content, "html.parser")


def gets_url(classes, location, source):
    results = []
    for a in soup.findAll(attrs={"class": classes}):
        name = a.find(location)
        if name not in results:
            results.append(name.get(source))
    return results


driver.quit()

if __name__ == "__main__":
    returned_results = gets_url("s-item__image-wrapper image-treatment", "img", "src")
    count = -1
    for b in returned_results:
        image_content = requests.get(b).content
        image_file = io.BytesIO(image_content)
        image = Image.open(image_file).convert("RGB")
        count += 1
        file_path = Path("C:\\Users\\aksud\\Images", "image" + str(count) + ".png")
        image.save(file_path, "PNG", quality=80)