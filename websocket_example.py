#!/usr/bin/env python

import websocket
import json

subscribing_topic = "/abc"
publishing_topic = "/def"

try:
    import thread
except ImportError:
    import _thread as thread


def on_message(ws, message):
    print(message)


def on_error(ws, error):
    print(error)


def on_close(ws):
    print("### closed ###")


def on_open(ws):
    def run(*args):

        advertise_message = {'op': 'advertise', 'topic': publishing_topic, 'type': 'std_msgs/String'}
        publish_message = {'op': 'publish', 'topic': publishing_topic, 'msg': {'data': 'testestet'}}
        subscribe_message = {'op': 'subscribe', 'topic': subscribing_topic, 'type': 'std_msgs/String'}

        ws.send(json.dumps(advertise_message))
        ws.send(json.dumps(publish_message))
        ws.send(json.dumps(subscribe_message))

    thread.start_new_thread(run, ())


if __name__ == "__main__":
    websocket.enableTrace(False)
    ws = websocket.WebSocketApp("ws://localhost:9090", on_message=on_message, on_error=on_error, on_close=on_close)

    ws.on_open = on_open
    ws.run_forever()
