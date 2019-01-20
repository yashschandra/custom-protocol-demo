from client import Client
from constants import KEY
import socket
import json
from tkinter import *

class Browser():

    def __init__(self, geometry):
        self.geometry = geometry
        self.client = None

    def start(self):
        self.root = Tk()
        self.root.geometry(self.geometry)
        self.browser(self.root)
        self.root.mainloop()
        self.close_connection()

    def browser(self, root):
        self.generate_top_frame()
        self.generate_middle_frame()
        self.generate_bottom_frame()

    def generate_top_frame(self):
        frame = Frame(self.root)
        frame.pack()
        self.link_text = Text(frame, height = 2, width = 50)
        self.link_text.grid(row = 0)
        connect_button = Button(frame, text = 'connect', command = self.connect_button_handler)
        connect_button.grid(row = 0, column = 1)
        disconnect_button = Button(frame, text = 'disconnect', command = self.disconnect_button_handler)
        disconnect_button.grid(row = 0, column = 2)

    def generate_bottom_frame(self):
        frame = Frame(self.root)
        frame.pack()
        self.message_text = Text(frame, height = 2, width = 50)
        self.message_text.grid(row = 0)
        send_button = Button(frame, text = 'send', command = self.send_button_handler)
        send_button.grid(row = 0, column = 1)
        quit_button = Button(frame, text = 'quit', command = self.quit_button_handler)
        quit_button.grid(row = 0, column = 2)

    def generate_middle_frame(self):
        frame = Frame(self.root)
        frame.pack()
        self.chat_box = Text(frame, height = 10, width = 50)
        self.chat_box.grid(row = 0)
        self.chat_box.config(state = 'disabled')

    def send_button_handler(self):
        text = self.message_text.get("1.0", "end-1c")
        response = self.send_message(text)
        self.handle_response(response)

    def quit_button_handler(self):
        self.root.quit()

    def connect_button_handler(self):
        if self.client is None:
            self.client = Client()
            self.link = self.link_text.get("1.0", "end-1c")
            self.protocol = self.get_protocol()
            self.host = self.get_host_name()
            self.port = self.get_port()
            self.client.connect(self.host, self.port)
            response = self.send_message("hello")
            self.handle_response(response)

    def disconnect_button_handler(self):
        self.close_connection()

    def send_message(self, message):
        data = {
            "message": message,
            "host": self.host,
            "protocol": self.protocol,
            "port": self.port,
            "key": KEY
        }
        response = self.client.send_data(json.dumps(data))
        return json.loads(response)

    def close_connection(self):
        self.send_message("bye")
        self.client.close()
        self.client = None

    def handle_response(self, response):
        if self.validate(response):
            message = response['message']
        else:
            message = "invalid response"
        self.chat_box.config(state = 'normal')
        self.chat_box.insert(END, message+'\n')
        self.chat_box.config(state = 'disabled')

    def get_protocol(self):
        protocol = self.link.split(':')[0]
        return protocol

    def get_host_name(self):
        host = self.link.split(":")[1].split("//")[1]
        if host == 'localhost':
            host = '127.0.1.1'
        return host

    def get_port(self):
        return 9210

    def validate(self, response):
        if response['type'] == 'response':
            return True
        return False

if __name__ == '__main__':
    browser = Browser("800x400")
    browser.start()