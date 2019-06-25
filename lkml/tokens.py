class Token:
    value: str

    def __eq__(self, other):
        return self.__class__ == other.__class__

    def __repr__(self):
        value = getattr(self, "value", "")
        return f"{self.__class__.__name__}({value})"


class StreamStartToken(Token):
    id = "<stream start>"


class StreamEndToken(Token):
    id = "<stream end>"


class BlockStartToken(Token):
    id = "{"


class BlockEndToken(Token):
    id = "}"


class ValueToken(Token):
    id = ":"


class SqlBlockEndToken(Token):
    id = ";;"


class DotToken(Token):
    id = "."


class CommaToken(Token):
    id = ","


class ListStartToken(Token):
    id = "["


class ListEndToken(Token):
    id = "]"


class SqlBlockToken(Token):
    id = "<sql block>"

    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.id == other.id and self.value == other.value


class LiteralToken(Token):
    id = "<literal>"

    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.id == other.id and self.value == other.value


class QuotedLiteralToken(Token):
    id = "<quoted literal>"

    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.id == other.id and self.value == other.value