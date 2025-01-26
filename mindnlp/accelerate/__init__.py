"""accelerate"""
from .utils import (
    accelerate_distributed_type,
    DistributedType,
    infer_auto_device_map,

)

from .big_modeling import (
    init_empty_weights,
    init_on_empty,

)
