class Friends:
    def __init__(self, connections):
        self.connections = set(frozenset(c) for c in connections)

    def add(self, connection):
        if connection in self.connections:
            print(False)
        else:
            self.connections.add(frozenset(connection))
            print(True)

    def remove(self, connection):
        if connection in self.connections:
            self.connections.remove(frozenset(connection))
            print(True)
        else:
            print(False)

    def names(self):
        print(set().union(*self.connections))

    def connected(self, relation):
        result = set()
        for connection in self.connections:
            if relation in connection:
                result.add(*(connection - set(relation)))
        print(result)


# проверки add()
f = Friends(({"1", "2"}, {"3", "1"}))
f.add({"1", "3"})
f.add({"4", "5"})

# проверки remove()
f = Friends(({"1", "2"}, {"3", "1"}))
f.remove({"1", "3"})
f.remove({"4", "5"})

# Проверки names()
f = Friends(({"a", "b"}, {"b", "c"}, {"c", "d"}))
f.names()
f.remove({"d", "c"})
f.names()

# Проверки connected
f = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}))
f.connected("a")
f.connected("d")
f.remove({"c", "a"})
f.connected("c")