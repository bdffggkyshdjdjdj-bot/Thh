import subprocess
import time
import webbrowser

# VNC server চালু
subprocess.Popen(["vncserver", "-localhost", ":1", "-geometry", "1280x720"])
time.sleep(2)

# Firefox চালু (display :1 এ)
subprocess.Popen(["firefox"], env={"DISPLAY": ":1"})

# novnc proxy চালু
subprocess.Popen([
    "websockify", "-D", "6080",
    "localhost:5901"
])

print("Open: http://localhost:6080/vnc.html")
