from channels.routing import route
from . import consumers


channel_routing = [
    # Wire up websocket channels to our consumers:
    route('websocket.connect', consumers.ws_connect),
    route('websocket.receive', consumers.ws_receive),
    route('websocket.disconnect', consumers.ws_disconnect),
]
