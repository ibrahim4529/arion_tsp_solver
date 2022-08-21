from typing import List, Tuple
from python_tsp.heuristics import solve_tsp_simulated_annealing, solve_tsp_local_search
from python_tsp.exact import solve_tsp_dynamic_programming, solve_tsp_brute_force
import requests
import numpy as np
from anneling import Annealing
from config import get_config

cfg = get_config()

def solve_using_anneling(graph):
    annealing = Annealing(distance_matrix=graph)
    urutan, jarak = annealing.annealing()
    return urutan, jarak

def solve_using_local_saerch(graph):
    return solve_tsp_local_search(graph)

def solve_using_dp(graph):
    return solve_tsp_dynamic_programming(graph)

def solve_using_brute_force(graph):
    return solve_tsp_brute_force(graph)

def build_distance_by_response(response):
    distance_matrix = []
    for row in response['rows']:
        row_list = [row['elements'][j]['distance']['value'] for j in range(len(row['elements']))]
        distance_matrix.append(row_list)
    return np.array(distance_matrix)

def build_address_str(addresses):
    address_str = ''
    for i in range(len(addresses) - 1):
      address_str += addresses[i] + '|'
    address_str += addresses[-1]
    return address_str

def build_distance_matrix_by_address_name(start_address: str,
    destination_addresses: List[str]):
    addresses = [start_address] + destination_addresses
    request = 'https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial'
    start_address_str = build_address_str(addresses)
    destination_addresses_str = build_address_str(addresses)
    request += '&origins=' + start_address_str
    request += '&destinations=' + destination_addresses_str
    request += '&key='+cfg.MAPS_API_KEY
    response = requests.get(request)
    return build_distance_by_response(response.json())  
