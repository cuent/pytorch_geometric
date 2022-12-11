import sys
from typing import Union

import torch

from torch_geometric.data import Data
from torch_geometric.utils.convert import from_networkx


class MotifGenerator:
    r"""Generate a motif based on a given structure.

    The structure is generated build in the attribute
    :class:`~torch_geometric.datasets.MotifGenerator.motif`
    using :class:`~torch_geometric.data.Data` as a base class.

    .. code-block:: python

        from torch_geometric.datasets.generators import MotifGenerator

        generator = MotifGenerator(structure='house')
        generator.motif # get the motif
        >>> Data(edge_index=[2, 12], y=[5], num_nodes=5)

    Args:
        structure (Data, Graph, str): generates a motif given:

            #. custom structure in PyG (:class:`~torch_geometric.data.Data`)
            #. custom structure in NetworkX (:class:`~networkx.Graph`)
            #. ready to use structures (str)
                * 'house' shape
                    generates a shape house with 5 nodes

    Returns :class:`~torch_geometric.data.Data` to represent a
        :class:`~torch_geometric.datasets.MotifGenerator.motif`.
    """
    def __init__(
        self,
        structure: Union[Data, str, ],
    ):
        self.structure = structure
        self.registered_structures = {
            "house":
            Data(
                num_nodes=5,
                edge_index=torch.tensor([
                    [0, 0, 0, 1, 1, 1, 2, 2, 3, 3, 4, 4],
                    [1, 3, 4, 4, 2, 0, 1, 3, 2, 0, 0, 1],
                ]),
                y=torch.tensor([1, 1, 2, 2, 3]),
            )
        }

    @property
    def motif(self) -> Data:
        if (isinstance(self.structure, str)
                and self.structure in self.registered_structures.keys()):
            return self.registered_structures[self.structure]
        elif isinstance(self.structure, Data):
            return self.structure
        elif check_for_networkx(self.structure):
            return from_networkx(self.structure)
        else:
            raise ValueError(f"Not supported structure. We currently support "
                             f"`torch_geometric.data.Data`, `networkx.Graph`, "
                             f"{', '.join(self.registered_structures.keys())}")


def check_for_networkx(structure):
    if "networkx" in sys.modules:
        from networkx import Graph

        return isinstance(structure, Graph)
    else:
        return False
