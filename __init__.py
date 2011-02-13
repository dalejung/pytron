import inspect

def interlock(base, addition):
    if inspect.isclass(addition):
        e = ClassExtender()
    else:
        e = Extender()

    e.extend(base, addition)

class interlock_with(object):
    def __init__(self, *args):
        self.classes = args

    def __call__(self, cls):
        for klass in self.classes:
            interlock(cls, klass)

        return cls

def wrap_init(base, new_init):
    """
    """
    if getattr(base, 'init_wrapped', False):
        return

    base.init_wrapped = True
    if hasattr(base, '__init__'):
        base._old_init = base.__init__
        def init_wrapper(self, *args, **kwargs):
            self._old_init(*args, **kwargs) 
            new_init(self, *args, **kwargs)
        base.__init__ = init_wrapper
    else:
        base.__init__ = new_init

def add_methods(base, methods):
    """
        Attach methods to base
    """
    for name, method in methods.items():
        setattr(base, name, method)

def get_methods(addition):
    """
        Get the methods from an object
    """
    methods = {}
    for name in dir(addition):
        val = getattr(addition, name)
        if name.startswith('_') or not callable(val):
            continue
        methods[name] = val

    return methods

def interlock_methods(base, addition):
    """
    """
    methods = get_methods(addition)
    add_methods(base, methods)

class Extender(object):
    def extend(self, base, addition):
        interlock_methods(base, addition)

class ClassExtender(Extender):
    @staticmethod
    def init_mixins(self, *args, **kwargs): 
        """
        instantiate the lions and interlock them
        """
        self._mixins_imp = []
        for cls in self.mixins:
            obj = cls()
            self._mixins_imp.append(obj)
            interlock_methods(self, obj)

    def extend(self, base, addition):
        setdefaultattr(base, 'mixins', [])
        base.mixins.append(addition)
        wrap_init(base, self.init_mixins)


def setdefaultattr(obj, name, value):
    try:
        return getattr(obj, name)
    except AttributeError:
        setattr(obj, name, value)
    return value
