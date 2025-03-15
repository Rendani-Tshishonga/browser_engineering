"""
Build a browser which can handle windows and
can draw the web page to the context of the window
"""
import tkinter as tk
from browser.Browser import request, lex

WIDTH = 1920
HEIGHT = 1080
HSTEP = 13
VSTEP = 18
SCROLL_STEP = 100

class Window(tk.TK):
    def __init__(self):
        super().__init__()
        self.title("Browser Engineering")
        self.canvas(
            width=WIDTH,
            height=HEIGHT
        )
        self.canvas.pack()
        self.scroll = 0
        self.window.bind("<Down>", self.scrolldown)
    
    def scrolldown(self, e):
        self.scroll += SCROLL_STEP
        self.draw()

    def draw(self):
        self.canvas.delete("all")
        for x, y, c in self.display_list:
            if y > self.scroll + HEIGHT: continue
            if y + VSTEP < self.scroll: continue
            self.canvas.create_text(x, y - self.scroll, text=c)

    @staticmethod
    def layout(text):
        display_list = []
        cursor_x, cursor_y = HSTEP, VSTEP
        for c in text:
            display_list.append((cursor_x, cursor_y, c))
            cursor_x += HSTEP
            if cursor_x >= WIDTH - HSTEP:
                cursor_y += VSTEP
                cursor_x = HSTEP
        return display_list

    def load(self, url):
        body = url.request()
        text = lex(body)
        self.display_list = layout(text)
        self.draw()
