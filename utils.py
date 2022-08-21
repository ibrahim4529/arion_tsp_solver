from typing import List, Tuple
from python_tsp.heuristics import solve_tsp_simulated_annealing, solve_tsp_local_search
from python_tsp.exact import solve_tsp_dynamic_programming, solve_tsp_brute_force
import requests
import numpy as np
import math
import random
from config import get_config

cfg = get_config()

def random_alternative(distance_matrix):
    urutan_awal= list(range(len(distance_matrix)))
    alternative_path = urutan_awal[1:]
    random.shuffle(alternative_path)
    urutan = [0] + alternative_path
    return urutan

class Annealing:
    def __init__(self, distance_matrix):
        self.distance_matrix = distance_matrix
        # urutan start from 0
        self.urutan = random_alternative(distance_matrix)
        print(self.urutan)
        self.jarak = self.calculate_jarak()

    def calculate_jarak(self):
        jarak = 0
        for i in range(len(self.urutan)):
            next_path = i + 1
            if next_path > len(self.urutan)-1:
                next_path = 0
            jarak += self.distance_matrix[self.urutan[i]][self.urutan[next_path]]
        return jarak
    
    def calculate_jarak_new(self, new_urutan):
        jarak = 0
        for i in range(len(new_urutan)):
            next_path = i + 1
            if next_path > len(new_urutan)-1:
                next_path = 0
            jarak += self.distance_matrix[new_urutan[i]][new_urutan[next_path]]
        return jarak
    
    def annealing(self):
        temp = 100
        temp_min = 0.1
        alpha = 0.99
        while temp > temp_min:
            new_urutan = random_alternative(self.distance_matrix)
            new_jarak = self.calculate_jarak_new(new_urutan)
            delta = new_jarak - self.jarak
            if delta < 0:
                self.urutan = new_urutan
                self.jarak = new_jarak
            else:
                p = math.exp(-delta / temp)
                if random.random() < p:
                    self.urutan = new_urutan
                    self.jarak = new_jarak
            temp *= alpha
        return self.urutan, self.jarak
    
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
