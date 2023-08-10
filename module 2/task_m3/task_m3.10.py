def first(size: int, *args) -> int:
    return size + len(args)

first(5, "first", "second", "third")
def second(size: int, **args) -> int:
    return size + len(args)

second(3, comment_one="first", comment_two="second", comment_third="third")