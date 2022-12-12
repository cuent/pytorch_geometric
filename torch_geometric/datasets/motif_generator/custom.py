from typing import Any

from torch_geometric.data import Data
from torch_geometric.datasets.motif_generator import MotifGenerator
from torch_geometric.utils import from_networkx


class CustomMotif(MotifGenerator):
    r"""Generates a motif based on a custom structure in the form of a
    :class:`torch_geometric.data.Data` or :class:`networkx.Graph`.

    Args:
        structure (torch_geometric.data.Data or networkx.Graph): The structure
            to use as a motif.
    """
    def __init__(self, structure: Any):
        super().__init__()

        self.structure = None
        if isinstance(structure, Data):
            self.structure = structure
        else:
            try:
                import networkx as nx
                if isinstance(structure, nx.Graph):
                    self.structure = from_networkx(structure)
            except ImportError:
                pass

        if self.structure is None:
            raise ValueError(f"Expected a 'structure' of type "
                             f"'torch_geometric.data.Data' or 'networkx.Graph'"
                             f"(got {type(structure)})")

    def __call__(self) -> Data:
        return self.structure
