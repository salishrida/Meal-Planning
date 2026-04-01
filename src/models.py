from dataclasses import dataclass
from typing import Optional

@dataclass
class Recipe:
    title: str
    url: str
    source: str
    description: Optional[str] = None
    protein_g: float = 0.0
``
