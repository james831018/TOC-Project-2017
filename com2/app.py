import sys
from io import BytesIO

import telegram
from flask import Flask, request, send_file

from fsm import TocMachine


API_TOKEN = '322175803:AAHsdBD7IEq6p7-yPTMxYytxoNkYQYZ_Gc0'
WEBHOOK_URL = 'https://69fabb4f.ngrok.io/hook'

app = Flask(__name__)
bot = telegram.Bot(token=API_TOKEN)
machine = TocMachine(
    states=[
        'user',
        'state1',
        'state2','state3','state4','state5','state6','state7','state8',
        'state9','state10','state11','state12',
        'state13','state14','state15','state16',
    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state1',
            'conditions': 'is_going_to_state1'
        },
        {
            'trigger': 'advance',
            'source': 'state1',
            'dest': 'state2',
            'conditions': 'is_going_to_state2'
        },
        {
            'trigger': 'advance',
            'source': 'state2',
            'dest': 'state3',
            'conditions': 'is_going_to_state3'
        },
       {
            'trigger': 'advance',
            'source': 'state3',
            'dest': 'state4',
            'conditions': 'is_going_to_state4'
        },
       {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state5',
            'conditions': 'is_going_to_state5'
        },
       {
            'trigger': 'advance',
            'source': 'state5',
            'dest': 'state6',
            'conditions': 'is_going_to_state6'
        },
       {
            'trigger': 'advance',
            'source': 'state6',
            'dest': 'state7',
            'conditions': 'is_going_to_state7'
        },
       {
            'trigger': 'advance',
            'source': 'state7',
            'dest': 'state8',
            'conditions': 'is_going_to_state8'
        },
       {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state9',
            'conditions': 'is_going_to_state9'
        },
       {
            'trigger': 'advance',
            'source': 'state9',
            'dest': 'state10',
            'conditions': 'is_going_to_state10'
        },
       {
            'trigger': 'advance',
            'source': 'state10',
            'dest': 'state11',
            'conditions': 'is_going_to_state11'
        },
       {
            'trigger': 'advance',
            'source': 'state11',
            'dest': 'state12',
            'conditions': 'is_going_to_state12'
        },
       {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state13',
            'conditions': 'is_going_to_state13'
        },
       {
            'trigger': 'advance',
            'source': 'state13',
            'dest': 'state14',
            'conditions': 'is_going_to_state14'
        },
       {
            'trigger': 'advance',
            'source': 'state14',
            'dest': 'state15',
            'conditions': 'is_going_to_state15'
        },
       {
            'trigger': 'advance',
            'source': 'state15',
            'dest': 'state16',
            'conditions': 'is_going_to_state16'
        },
        {
            'trigger': 'go_back',
            'source': [
                'state4','state8','state12','state16'
            ],
            'dest': 'user'
        },
 
    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)


def _set_webhook():
    status = bot.set_webhook(WEBHOOK_URL)
    if not status:
        print('Webhook setup failed')
        sys.exit(1)
    else:
        print('Your webhook URL has been set to "{}"'.format(WEBHOOK_URL))


@app.route('/hook', methods=['POST'])
def webhook_handler():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    machine.advance(update)
    return 'ok'


@app.route('/show-fsm', methods=['GET'])
def show_fsm():
    byte_io = BytesIO()
    machine.graph.draw(byte_io, prog='dot', format='png')
    byte_io.seek(0)
    return send_file(byte_io, attachment_filename='fsm.png', mimetype='image/png')


if __name__ == "__main__":
    _set_webhook()
    app.run()
