import time
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--lang=en-US')
# chrome_options.add_argument('--proxy-server=http://174.138.46.194:8080')
prefs = {"profile.managed_default_content_settings.images": 2, "int1.accept_language": "en-GB"}
chrome_options.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome(chrome_options=chrome_options)

urls = []
with open("./set/uncrawl.txt", "r", encoding="utf-8") as rfile:
    urls = [f.strip() for f in rfile if f.split(':')[0] != "Error "]

for url in urls:
    driver.get(url)
    time.sleep(10)
    html_selennium_text = driver.find_elements_by_xpath("//body")[0].text
    html = driver.page_source
    name = str(url.split('/')[2].split(':')[0])
    with open('./final_text/' + name + '.txt', 'w', encoding="utf-8") as f:
        f.write(str(html_selennium_text))
