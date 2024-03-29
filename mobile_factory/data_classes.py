from dataclasses import dataclass


@dataclass
class Components:
    components: list[str]


@dataclass
class CreateOrderResponse:
    order_id: str
    total: float
    parts: list[str]