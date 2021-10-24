from collections import defaultdict


class Graph(object):
    """Graph adjacency list representation using dictionary of lists/sets."""

    def __init__(self, directed, use_list=False):
        """Initialize Graph class object instance.

        Args:
            directed(bool): Whether graph is directed or not.
            use_list(bool, optional): Wheter to use list or set for adjacency
                list graph representation.

        """
        self._directed = directed
        self._use_list = use_list
        if self._use_list:
            self._adj_list = defaultdict(list)
        else:
            self._adj_list = defaultdict(set)

    def __str__(self):
        """Graph class custom __str__ method implementation.

        Returns:
            str: Dictionary adjacency list keys and values.

        """
        return str(self._adj_list)

    def __repr__(self):
        """Graph class custom __repr__ method implementation.

        Returns:
            str: Graph string object.

        """
        return "{name}(directed={directed})".format(
            name=self.__class__.__name__,
            directed=self._directed,
        )

    def __getitem__(self, item):
        return self._adj_list[item]

    @property
    def adj_list(self):
        """Graph class adjacency list property.

        Returns:
            Adjacency list representation: dictionary of sets.

        """
        return self._adj_list

    def add_edge(self, u, v):
        """Add an edge to graph.

        Args:
            u(Any): Target vertex value: any hashable object.
            v(Any): Destination vertex value.

        """
        self._add_to_adj_list(u, v)

        if not self._directed:
            self._add_to_adj_list(v, u)

    def _add_to_adj_list(self, key, value):
        """Protected class method for adding value to adj_list dictionary.

        Args:
            key(Any): Target vertex value: any hashable object.
            value(Any): Destination vertex value.

        """
        if key not in self._adj_list:
            if self._use_list:
                self._adj_list[key] = []
            else:
                self._adj_list[key] = set()

        if self._use_list and value not in self._adj_list:
            self._adj_list[key].append(value)
        else:
            self._adj_list[key].add(value)
