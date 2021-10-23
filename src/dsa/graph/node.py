from dsa.generic import Node


class GraphNode(Node):
    """GraphNode class implementation for Graph data structure."""

    def __init__(self, neighbors=set(), **kwargs):
        """Initialize GraphNode class object instance.

        Args:
            neighbors(list or set, optional): Graph node neighbors.
            **kwargs: Any extra attributes for the GraphNode object instance.

        """
        super().__init__(**kwargs)
        self.neighbors = neighbors
