"""
Build a browser which can handle windows and
can draw the web page to the context of the window
"""
import tkinter as tk
from browser.Browser import request, lex

WIDTH = 1920
HEIGHT = 1080

class Window(tk.TK):
    def __init__(self):
        super().__init__()
        self.title("Browser Engineering")
        self.canvas(
            width=WIDTH,
            height=HEIGHT
        )
        self.canvas.pack()

    def load(self, url):
        body = url.request()
        text = lex(body)
        HSTEP, VSTEP = 13, 18
        cursor_x, cursor_y = HSTEP, VSTEP
        for c in text:
            self.canvas.create_text(cursor_x, cursor_y, text=c)
            cursor_x += HSTEP
            if cursor_x >= WIDTH - HSTEP:
            cursor_y += VSTEP
            cursor_x = HSTEP



