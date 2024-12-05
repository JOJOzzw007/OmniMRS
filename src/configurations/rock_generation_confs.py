

import dataclasses


@dataclasses.dataclass
class RockGenerationConf:
    instancers_path: str = dataclasses.field(default_factory=str)
    rocks_settings: dict = dataclasses.field(default_factory=dict)


@dataclasses.dataclass
class RequestGroupConf:
    seed: int = dataclasses.field(default_factory=int)
    collections: list = dataclasses.field(default_factory=list)
    use_point_instancer: bool = dataclasses.field(default_factory=bool)
    requests: list = dataclasses.field(default_factory=list)


@dataclasses.dataclass
class RequestConf:
    attribute: str = dataclasses.field(default_factory=str)
    num: int = dataclasses.field(default_factory=int)
    parent: str = dataclasses.field(default_factory=str)
    axes: list = dataclasses.field(default_factory=list)
    layer: dict = dataclasses.field(default_factory=dict)
    sampler: dict = dataclasses.field(default_factory=dict)
