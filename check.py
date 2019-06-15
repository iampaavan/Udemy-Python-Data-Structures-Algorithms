class M(object):

    def public(self):
        print(f"Use tab to see me.")

    def _private(self):
        print(f"You won't be able to see me.")


m = M()
m.public()
m._private()


