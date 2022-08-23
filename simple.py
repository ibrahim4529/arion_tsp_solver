from utils import build_distance_matrix_by_address_name
from anneling import Annealing

distance_matrix  = build_distance_matrix_by_address_name(
    start_address='Losari Kidul Cirebon',
    destination_addresses=[
        'Mulyasari Losari Cirebon',
        'Panggang Sari Losari Cirebon',
        'Barisan Losari Cirebon',
    ]
)

annealing = Annealing(distance_matrix=distance_matrix)
urutan, jarak = annealing.annealing()
print(urutan)
print(jarak)
 