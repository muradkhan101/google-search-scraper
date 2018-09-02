import requests
from base64 import b64decode

def save_base64_image(image_str, file_name):
    # 23 is length of data:image/jpeg;base64, prepending string
    byte_array = b64decode(image_str[23:])
    with open(file_name, 'wb') as f:
        f.write(byte_array)
    return True

def save_image_from_url(url, file_name):
    try:
        req = requests.get(url)
        extension = url[ url.rfind('.'): ]
        with open(file_name + '.' + extension, 'wb') as f:
            f.write(req.content)
    except:
        print('DOWNLOADING ', url, ' FAILED')
        return False
    return True
