import os

from django.core.management.utils import get_random_secret_key
from django.utils.crypto import get_random_string


TMP_DIR = 'scripts/.tmp'
SOURCE_DIR = 'scripts/files'


def create_dotenv_file(server_name):
    with open(f'{SOURCE_DIR}/.env-template.txt', 'r') as readfile:
        content: str = readfile.read()
        config = {
            'hostname': server_name,
            'secret_key': get_random_secret_key(),
            'api_access_key':  str(get_random_string(length=32)),
            'api_client_secret': str(get_random_string(length=32))
        }
        result: str = content.format(**config)
        with open('.env', 'w') as writefile:
            writefile.write(result)


def create_sudoers_config():
    with open(f'{SOURCE_DIR}/sudoers-template.txt', 'r') as readfile:
        content: str = readfile.read()
        config = {
            'user': os.environ['SUDO_USER']
        }
        result: str = content.format(**config)

        with open(f'{TMP_DIR}/sudoers-dplhooks', 'w') as writefile:
            writefile.write(result)


def create_nginx_config(server_name):
    with open(f'{SOURCE_DIR}/nginx-template.txt', 'r') as readfile:
        content: str = readfile.read()
        config = {
            'server_name': server_name,
            'user': os.environ['SUDO_USER']
        }
        result: str = content.format(**config).replace('\[','{').replace('\]', '}')
        with open(f'{TMP_DIR}/nginx-site-dplhooks', 'w') as writefile:
            writefile.write(result)


def create_systemd_service():
    with open(f'{SOURCE_DIR}/dplhooks.service.txt', 'r') as readfile:
        content: str = readfile.read()

        config = {
            'user': os.environ['SUDO_USER']
        }
        result: str = content.format(**config)

        with open(f'{TMP_DIR}/dplhooks.service', 'w') as writefile:
            writefile.write(result)


def main():
    create_systemd_service()
    create_sudoers_config()
    server_name = input('Server domain or IP: ')
    create_nginx_config(server_name)
    create_dotenv_file(server_name)


if __name__ == '__main__':
    main()
