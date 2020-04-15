import network
def createAp():
    ap = network.WLAN(network.AP_IF)
    ap.active(True)
    ap.config(essid='espap-lemon') # d当后面增加audomod 参数时会出错。
    ap.status()
    ap.__dir__()

