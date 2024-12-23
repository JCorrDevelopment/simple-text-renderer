from __future__ import annotations

import abc
import dataclasses
from typing import TYPE_CHECKING, Final, Self, TypedDict, Unpack

from std_utils.more_str.generators import random_string

if TYPE_CHECKING:
    from weavely.formatters.base import IBlockFormatter
    from weavely.renderers.base import IBlockRenderer


@dataclasses.dataclass(slots=True)
class Data:
    """
    Default label for data containing in the block to make operation on block more convenient.

    This class doesn't have any specific information, any specific Data type must be inherited from this class.
    """


class DataKwargs(TypedDict):
    """
    Type hint for the arbitrary keyword arguments to initialize the data object in the block.

    Should be inherited in the specific block class to provide the correct code completion.

    NOTE: Using of this kwargs is going a bit against static typing, but it's a trade-off to make
    the block creation more convenient and readable.
    """


class BaseBlock[TData: Data](abc.ABC):
    """
    Base class for all blocks in the Weavely.

    Idea of the block is to have a simple way to contain any arbitrary data and operate on it in abstract way. The best
    analogy for this is a simple paragraph in a text editor. It can contain any text, tables, images, etc. But you can
    move the paragraph around, change its style, etc. without knowing what is inside it.

    Each of blocks must contain a `Data` object, which is a container for the arbitrary information that block can
    operate on. Specific data type must be defined in the inherited class.

    Each block has a name, which is used to reference the blocks in the application. It can be provided by the user on
    block creation, or it will be generated automatically.

    Each block can follow one of two ways to format or render the data:
        a. It may specify a specific formatter or renderer object to use exclusively for this block.
        b. Or, otherwise, it will use the default formatter or renderers provided by the downstream objects
            implementation.
    """

    def __init__(
        self,
        data: TData,
        name: str | None = None,
        formatter: IBlockFormatter | None = None,
        renderer: IBlockRenderer | None = None,
    ) -> None:
        """
        Initialize the block object.

        Args:
            data (TData): Data object containing any arbitrary data that block can operate on. Specific data type must
                be defined in the inherited class.
            name (str | None): Optional name of the block. Used to reference the block in the file. If None, the block
                will generate it based on the class name and some randomized suffix.
            formatter (IBlockFormatter): Formatter object to format the data object. If None, the block will
                use the default formatter provided by the file formatter implementation.
            renderer (IBlockRenderer | None): Renderer object to render the block into a specific format.
                If None, the block will use the default renderer provided by the file renderer implementation.
        """
        self._data = data
        self._formatter = formatter
        self._renderer = renderer
        self._name: Final[str] = name or random_string(prefix=self.__class__.__name__)

    @property
    def data(self) -> TData:
        """
        Get the data object contained in the block.

        Returns:
            TData: Data object.
        """
        return self._data

    @property
    def formatter(self) -> IBlockFormatter | None:
        """
        Get the formatter object used by the block.

        Returns:
            IBlockFormatter | None: Formatter object.
        """
        return self._formatter

    @property
    def renderer(self) -> IBlockRenderer | None:
        """
        Get the renderer object used by the block.

        Returns:
            IBlockRenderer | None: Renderer object.
        """
        return self._renderer

    @property
    def name(self) -> str:
        """
        Get the block name.

        Returns:
            str: Block name.
        """
        return self._name

    @classmethod
    @abc.abstractmethod
    def by_data(
        cls,
        *,
        name: str | None = None,
        formatter: IBlockFormatter | None = None,
        renderer: IBlockRenderer | None = None,
        **data: Unpack[DataKwargs],
    ) -> Self:
        """
        Create a new block instance by providing the data object.

        Args:
            name (str | None): Optional name of the block. Used to reference the block in the file. If None, the block
                will generate it based on the class name and some randomized suffix.
            formatter (IBlockFormatter): Formatter object to format the data object. If None, the block will
                use the default formatter provided by the file formatter implementation.
            renderer (IBlockRenderer | None): Renderer object to render the block into a specific format.
                If None, the block will use the default renderer provided by the file renderer implementation.
            data (DataKwargs): Arbitrary range of keyword arguments to initialize the data object.
                Must be specified by the specific block class.

        Returns:
            Self: New block instance.

        Raises:
            DataIsMissingError: If information provided in `**data` is not enough to create data object.
        """
