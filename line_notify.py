import requests


class LineNotify:
    def __init__(self, token):
        self.token = token

    def send(self, payload, file=None):
        url = 'https://notify-api.line.me/api/notify'
        headers = {'Authorization': 'Bearer ' + self.token}
        print(requests.post(url, headers=headers, data=payload, files=file))

    def notify_text(self, message):
        payload = {'message': message}
        return self.send(payload)

    # def notify_file(self, filename):
    #     file = {'imageFile': open(filename, 'rb')}
    #     payload = {'message': 'test'}
    #     return self.send(payload, file)

    def notify_picture(self, url):
        payload = {'message': " ", 'imageThumbnail': url, 'imageFullsize': url}
        return self.send(payload)

    def notify_sticker(self, sticker_id, sticker_package_id):
        payload = {'message': " ", 'stickerPackageId': sticker_package_id,
                   'stickerId': sticker_id}
        return self.send(payload)
