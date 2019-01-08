from flask import Flask, request, json
from settings import *
import vk
import messageHandler

app = Flask(__name__)

@app.route('/', methods=['POST'])
def processing():
    data = json.loads(request.data)
    if 'type' not in data.keys():
        return 'not vk'
    if data['type'] == 'confirmation':
        return confirmation_token
    elif data['type'] == 'message_new':
        messageHandler.create_answer(data['object'], token)
        return 'ok'
#   {"type":"message_new","object":{"date":1544612189,"from_id":257134277,"id":10,"out":0,"peer_id":257134277,"text":"lh",
#   "conversation_message_id":10,"fwd_messages":[],"important":false,"random_id":0,"attachments":[],"is_hidden":false},"group_id":175190610}

