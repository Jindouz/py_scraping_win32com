import win32com.client as comclt
import time

wsh = comclt.Dispatch("WScript.Shell")

wsh.AppActivate("chrome")
wsh.SendKeys("^t")
time.sleep(2)
wsh.SendKeys("https://www.youtube.com/watch?v=Q8PdffUfoF0")
wsh.SendKeys("~")
time.sleep(6)
wsh.SendKeys("^w")

