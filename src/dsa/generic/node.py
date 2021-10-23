from reprlib import recursive_repr


class Node(object):
    """Generic Node class implementation for any data structure."""

    def __init__(self, **kwargs):
        """Initialize Node class object instance."""
        self.__dict__.update(kwargs)

    def __str__(self):
        """Node class __str__ method."""
        return str(self.__dict__)

    @recursive_repr()
    def __repr__(self):
        """Node class __repr__ method."""
        kwargs = []

        for key, value in self.__dict__.items():
            if not key.startswith("_"):
                kwargs.append(
                    "{key}={value}".format(
                        key=key,
                        value=repr(value)
                    )
                )

        return "{name}({kwargs})".format(
            name=self.__class__.__name__,
            kwargs=", ".join(kwargs)
        )
