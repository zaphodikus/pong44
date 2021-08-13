#

class ClientBase():

    @staticmethod
    def read_pos(string: str):
        s = string.split(',')
        return int(s[0]), int(s[1])

    @staticmethod
    def make_pos(tup) -> str:
        return str(tup[0]) + ',' + str(tup[1])
