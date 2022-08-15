from utils import build_distance_matrix_by_address_name

distance_matrix  = build_distance_matrix_by_address_name(
    start_address='Losari Kidul Cirebon',
    destination_addresses=[
        'Mulyasari Losari Cirebon',
        'Panggang Sari Losari Cirebon',
        'Barisan Losari Cirebon',
    ]
)

print(distance_matrix)
 