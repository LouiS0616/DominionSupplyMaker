from enum import Enum

from ._impl_as_collection import _ImplAsCollection
from ._impl_as_set import _ImplAsSet
from ._impl_as_stream import _ImplAsStream


#
class Impls(Enum):
    AS_COLLECTION = _ImplAsCollection
    AS_SET        = _ImplAsSet
    AS_STREAM     = _ImplAsStream


#
def build_sequential(name, impls, dct, *, builder):
    assert all(isinstance(impl, Impls) for impl in impls)

    return type(
        name, tuple(impl.value for impl in impls), {
            **dct, '_Seq_builder': lambda self, *args: builder(*args)
        }
    )

