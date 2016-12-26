
def handle(socket, protocol, platform, data):
    handler = route.get(protocol)
    if handler is None:
        print("protocol:{} handler is not found".format(protocol))
        return
    fun = getattr(sys.modules[__name__], handler)
    fun(socket, platform, data)

def order_check(socket, platform, data):
    pass

def allocate_order(socket, platform, data):
    pass

def history_order(socket, platform, data):
    pass

def cancel_order(socket, platform, data):
    pass

def order_feedback(socket, platform, data):
    pass
