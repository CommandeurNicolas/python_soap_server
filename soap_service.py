from spyne import Iterable, Integer, Unicode, rpc, Application, Service
# from spyne.protocol.http import HttpRpc
from spyne.protocol.soap import Soap11
from spyne.protocol.json import JsonDocument


# class HelloWorldService(Service):
#     @rpc(Unicode, Integer, _returns=Iterable(Unicode))
#     def hello(ctx, name, times):
#         name = name or ctx.udc.config['HELLO']
#         times = times or ctx.udc.config['TIMES']
#         for i in range(times):
#             yield u'Hello, %s' % name

class ShippingService(Service):
    @rpc(Unicode, Integer, _returns=Iterable(Unicode))
    def shipping(ctx, distance, weight):
        distance = distance or ctx.udc.config['DISTANCE']
        weight = weight or ctx.udc.config['WEIGHT']
        yield u'%i' % (float(distance)//10 + float(weight)//2 )


class UserDefinedContext(object):
    def __init__(self, flask_config):
        self.config = flask_config


def create_app(flask_app):
    application = Application(
        [ShippingService], 
        tns='shipping',
        in_protocol=Soap11(validator='lxml'),
        out_protocol=Soap11(),
    )

    def _flask_config_context(ctx):
        ctx.udc = UserDefinedContext(flask_app.config)
    application.event_manager.add_listener('method_call', _flask_config_context)

    return application