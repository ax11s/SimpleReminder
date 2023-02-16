import threading
from win10toast import ToastNotifier

n = ToastNotifier()

title = "your title"
message = "your message"

def notify():
    n.show_toast(title , message, duration = 5)



def timer():
    threading.Timer(10.0, timer).start()
    notify()

timer()