import sys
from bs4 import BeautifulSoup
import requests
from os import mkdir
from os.path import isdir
from shutil import rmtree
from urllib.parse import urlparse
from tqdm import tqdm


class Main:


    def __init__(self, page_link):
        self.__page_link = page_link
        self.__output_path = '.\\images'

    def start(self):
        self.create_download_folder()

        response = requests.get(self.__page_link)

        soup = BeautifulSoup(response.text, 'html.parser')
        img_tags = soup.find_all('a')

        download_images = []
        for element in img_tags:
            if element['href'].endswith('.jpg'):
                download_images.append(element['href'])

        for url_image in tqdm(download_images, leave=True):
                self.save_file(url_image)

    def save_file(self, url_image):
        name_file = str(url_image).split('/')[-1]
        response = requests.get(url_image, stream=True)

        if response.status_code == 200:
            with open(f'{self.__output_path}\\{name_file}', 'wb') as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)

    def create_download_folder(self):
        if isdir(self.__output_path):
            rmtree(self.__output_path)

        mkdir(self.__output_path)

    def is_valid_url(self):
        try:
            result = urlparse(self.__page_link)
            return all([result.scheme, result.netloc])
        except ValueError:
            return False

if __name__ == '__main__':
    args = sys.argv
    if len(args) <= 1:
        print('Informe a URL que deseja consultar.')
        exit()

    app = Main(args[1])
    if not app.is_valid_url():
        print('Informe uma URL válida.')
        exit()

    app.start()
    print('Processo finalizado!')
