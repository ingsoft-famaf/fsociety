from channels import include

channel_routing = [
    include('chat_room.routing.channel_routing', path=r'^/chat_room/'),
]
