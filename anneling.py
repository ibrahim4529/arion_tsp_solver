import random
import math

def random_alternative(current_urutan):
    # ini swap
    """ random alternative path 
    @return: alternative path
    an alternative path is a random path start from first index 0 to length of distance matrix 
    always start from first index 0 or first place in the path
    return always [0, random number]
    """
    # [0, 1, 3, 4, 2]
    # [0, 2, 1, 3, 4]
    alternative_path = current_urutan[1:]
    random.shuffle(alternative_path)
    urutan = [0] + alternative_path
    return urutan


class Annealing:
    def __init__(self, distance_matrix):
        self.distance_matrix = distance_matrix
        # urutan start from 0
        list_of_place = list(range(len(distance_matrix)))
        self.urutan = random_alternative(list_of_place)
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
        temp = 2000
        temp_min = 0.1
        alpha = 0.99
        while temp > temp_min:
            #[0, 1, 2, 4, 3] => 100
            new_urutan = self.urutan.copy()
            new_urutan = random_alternative(new_urutan)
            #[0, 1, 3, 4, 2] => 99
            #[0, 2, 1, 3, 4] => 101
            new_jarak = self.calculate_jarak_new(new_urutan)
            #delta = 99 - 100
            #dalta = 101 - 99
            #delta = 2

            delta = new_jarak - self.jarak
            if delta < 0:
                # [0, 1, 3, 4, 2]
                self.urutan = new_urutan
                #self.jarak = 99
                self.jarak = new_jarak
            else:
                p = math.exp(-delta / temp)
                if random.random() < p:
                    self.urutan = new_urutan
                    self.jarak = new_jarak
            temp *= alpha
        return self.urutan, self.jarak