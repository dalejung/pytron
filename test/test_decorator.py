from pytron import interlock_with

class Arm(object):
    def __init__(self):
        print 'init arm'

    def punch(object):
        print 'i am punching'

class Leg(object):
    def __init__(self):
        print 'init leg'

    def kick(object):
        print 'i am kicking'

@interlock_with(Arm, Leg)
class Person(object):
    def __init__(self):
        print 'I AM PERSON'

sapien = interlock_with(Arm, Leg)

@sapien
class Alien(object):
    pass

print dir(Person)

p = Person()

p.kick()

alien = Alien()
alien.punch()

