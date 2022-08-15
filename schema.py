from enum import Enum
from typing import List, Tuple
from pydantic import BaseModel

class Methode(str, Enum):
    ANNEALING = 'annealing'
    LOCAL_SAERCH = 'local_search'
    DP = 'dp'
    BRUTE_FORCE = 'brute_force'

class Urutan(BaseModel):
    from_address: str
    to_addresses: str
    jarak: int

class RequestOptimize(BaseModel):
    start_location: str = "Polindra Indramayu"
    destination_locations: List[str] = [
        "Jatibarang Indramayu",
        "Bankir Indramayu",
        "Cipadung Indramayu",
        "SMA N 1 Indramayu"
    ]
    method: Methode = Methode.DP

class ResponseOptimizeTsp(BaseModel):
    urutan_tujuan: List[Urutan]
    urutan: List[int]
    jarak: float