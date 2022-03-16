import requests


def test_file():
    url = "http://127.0.0.1:5000/file"
    file_path = {'file': open("G:/图片素材/24MB左右.jpg", 'rb')}
    r = requests.post(url, files=file_path)
    assert r.status_code == 200
