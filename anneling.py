from utils import build_distance_matrix_by_address_name
import random
import math

distance_matrix  = build_distance_matrix_by_address_name(
    start_address='Losari Kidul Cirebon',
    destination_addresses=[
        'Mulyasari Losari Cirebon',
        'Panggang Sari Losari Cirebon',
        'Barisan Losari Cirebon',
    ]
)

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
    

anneling = Annealing(distance_matrix=distance_matrix)
urutan, jarak = anneling.annealing()
print(urutan)
print(jarak)