from Pyro5.api import expose

from .._callbacks import get_auto_callback_class

__all__ = [
    "get_auto_callback_pyro",
]


def get_auto_callback_pyro():
    klass = get_auto_callback_class()

    class pyroCallback(klass):
        @expose
        def receive_core_callback(self, signal_name, args):
            # let it throw an exception.
            getattr(self, signal_name).emit(*args)

    return pyroCallback
