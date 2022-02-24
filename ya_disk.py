import requests


TOKEN = "AQAAAAAeD-bTAADLWxzlK_FWs00okOMsVtSbbCc"


def get_headers():
    token = TOKEN
    return {
        'Content-Type': 'application/json',
        'Authorization': 'OAuth {}'.format(token)
    }

def create_folder(folder_name):
    url = "https://cloud-api.yandex.net/v1/disk/resources"
    headers = get_headers()
    params = {'path': folder_name}
    response = requests.put(url, headers=headers, params=params)
    if response.status_code == 201:
        print(f'Добавлена папка {folder_name}')
        return response.status_code




if __name__ == '__main__':

    create_folder('YaDisk_test_folder')


