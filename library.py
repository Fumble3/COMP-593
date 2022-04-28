import requests
import ctypes

def set_desktop_background_image(image_path):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 0)

def download_image_from_url(image_url, save_path):
    
    print('Downloading the image from URL...', end='')
    response = requests.get(image_url)
    
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print('Success!')
        
    else:
        print('Failed. Response code: ', response.status_code)
    
