from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os
import requests
import zipfile





def baixar_arquivo(url):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        nome_arquivo = url.split("/")[-1]
        return (nome_arquivo, response.content)
    else:
        raise ValueError("Erro ao baixar o arquivo. Código de status:", response.status_code)

def init_scrapping():
    chrome_options = Options()
    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": download_dir,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
    })


    service = Service(ChromeDriverManager().install())

    browser = webdriver.Chrome(service=service, options=chrome_options)


    link = 'https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos'

    browser.get(link)

    browser.find_element("xpath", '/html/body/div[5]/div/div/div/div/div[2]/button[3]').click()

    link_download1 = browser.find_element("xpath" , '//*[@id="cfec435d-6921-461f-b85a-b425bc3cb4a5"]/div/ol/li[1]/a[1]').get_attribute('href')
    link_download2 = browser.find_element("xpath" , '//*[@id="cfec435d-6921-461f-b85a-b425bc3cb4a5"]/div/ol/li[2]/a').get_attribute('href')
    browser.quit()

    print('Donwloading files...')

    nome_arquivo1, content1 = baixar_arquivo(link_download1)
    nome_arquivo2, content2 = baixar_arquivo(link_download2)

    zip_files([(nome_arquivo1, content1), (nome_arquivo2, content2)])
    
def zip_files(files_list):
    zip_filename = os.path.join(download_dir, "downloaded_files.zip")

    with zipfile.ZipFile( zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for file_name, content in files_list:
            zipf.writestr(file_name, content)


download_dir = "./teste1"
if not os.path.exists(download_dir):
    os.makedirs(download_dir)

init_scrapping()



