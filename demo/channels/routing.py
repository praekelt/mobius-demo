from channels import route_class

from demo.channels.consumers import EchoConsumer


channel_routing = [
    route_class(EchoConsumer, path=r"^/echo")
]
