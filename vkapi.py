import vk
import requests
import json
import settings

session = vk.Session()
api = vk.API(session, v=5.92)


def send_message(user_id, token, message,  attachment=""):
    api.messages.send(access_token=token, user_id=str(user_id),random_id=0, message=message, attachment=attachment)

"""def get_picture(user_id,photo_dir):
    url = api.photos.getMessagesUploadServer(peer_id=str(user_id),access_token=settings.access_token)['upload_url']
    files = {'photo': open(photo_dir, 'rb')}

    response = requests.post(url, files=files)
    result = json.loads(response.text)

    uploadResult = api.photos.saveMessagesPhoto(server=result["server"],
                                                  photo=result["photo"],
                                                  hash=result["hash"])
    attachment=uploadResult[0]["id"]
    return attachment"""

