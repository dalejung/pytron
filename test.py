import unittest
from datetime import datetime

import pytron

class Bark(object):
    def __init__(self, woof='woof'):
        self.woof = woof
        self.last_barked = None
        super(Bark, self).__init__()

    def bark(self):
        self.last_barked = datetime.now()
        return self.woof

class Target(object):
    def __init__(self):
        self.created = datetime.now()
        super(Target, self).__init__()


class TestExtend(unittest.TestCase):

    def test_object_extend_object(self):
        woof = 'W0000F'
        b = Bark(woof)
        t = Target()
        pytron.extend(t,b)
        self.assertTrue(hasattr(b,'bark'))
        self.assertTrue(hasattr(t,'bark'))
        self.assertEqual(t.bark(), woof)
        self.assertEqual(t.bark.im_self, b)

    def test_class_extend_object(self):
        b = Bark()
        pytron.extend(Target,b)
        t = Target()
        self.assertTrue(hasattr(b,'bark'))
        self.assertTrue(hasattr(t,'bark'))

    def test_class_extend_class(self):
        pytron.extend(Target,Bark)
        t = Target()
        self.assertTrue(hasattr(t,'bark'))

def run():
    unittest.main()

if __name__ == '__main__':
    run()
