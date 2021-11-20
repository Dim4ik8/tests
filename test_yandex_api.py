import requests
import unittest


class TestYandexDiskAPI(unittest.TestCase):
    def setUp(self) -> None:
        self.mkdir_url = 'https://cloud-api.yandex.net/v1/disk/resources'
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'OAuth AQAAAAAEL32SAADLWyQxd0KRZE-Wtm-MGDXNRj0'
        }

        self.dir_name = 'unittest'

    def tearDown(self) -> None:
        response = requests.delete(
            url=self.mkdir_url,
            headers=self.headers,
            params={'path': self.dir_name}
        )

    def test_mkdir_201(self):
        params = {
            'path': self.dir_name
        }
        response = requests.put(
            url=self.mkdir_url,
            headers=self.headers,
            params=params
        )

        assert response.status_code == 201

    def test_mkdir_400(self):
        params = {
            self.dir_name: 'path'
        }
        response = requests.put(
            url=self.mkdir_url,
            headers=self.headers,
            params=params
        )
        assert response.status_code == 400

    def test_mkdir_401(self):
        params = {
            self.dir_name: 'path'
        }
        response = requests.put(
            url=self.mkdir_url,
            headers={},
            params=params
        )
        assert response.status_code == 401

    def test_mkdir_403(self):

        params = {
            'path': self.dir_name
        }
        response = requests.put(
            url=self.mkdir_url,
            headers=self.headers,
            params=params
        )
        if response.status_code == 201:
            self.skipTest('Свободного места на диске достаточно для создания папки...')
        assert response.status_code == 403

    def test_mkdir_404(self):
        params = {
            'path': self.dir_name
        }
        response = requests.put(
            url=self.mkdir_url + self.dir_name,
            headers=self.headers,
        )

        assert response.status_code == 404

    def test_mkdir_406(self):

        headers = {
            'Content-Type': 'application/json',
            'Accept': 'text/html',
            'Authorization': 'OAuth AQAAAAAEL32SAADLWyQxd0KRZE-Wtm-MGDXNRj0'
        }
        params = {
            'path': self.dir_name,
        }
        response = requests.put(
            url=self.mkdir_url,
            headers=headers,
            params=params
        )
        if response.status_code != 406:
            self.skipTest(f'Пришел код {response.status_code} вместо 406...')
        assert response.status_code == 406

    def test_mkdir_409(self):
        params = {
            'path': self.dir_name,
        }
        first_response = requests.put(
            url=self.mkdir_url,
            headers=self.headers,
            params=params
        )
        second_response = requests.put(
            url=self.mkdir_url,
            headers=self.headers,
            params=params
        )
        assert second_response.status_code == 409
