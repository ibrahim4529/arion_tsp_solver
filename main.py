from fastapi import FastAPI
from schema import Methode, RequestOptimize, ResponseOptimizeTsp, Urutan
from utils import build_distance_matrix_by_address_name, solve_using_anneling, solve_using_dp, solve_using_brute_force, solve_using_local_saerch
app = FastAPI()


@app.post("/cacluate-tsp", response_model=ResponseOptimizeTsp)
def cacluate_tsp(request: RequestOptimize):
    addresses = [request.start_location] + request.destination_locations
    distance_matrix = build_distance_matrix_by_address_name(request.start_location, request.destination_locations)
    list_urutan = []
    if request.method == Methode.ANNEALING:
        urutan, jarak = solve_using_anneling(distance_matrix)
    elif request.method == Methode.DP:
        urutan, jarak =  solve_using_dp(distance_matrix)
    elif request.method == Methode.BRUTE_FORCE:
        urutan, jarak  = solve_using_brute_force(distance_matrix)
    elif request.method == Methode.LOCAL_SAERCH:
        urutan, jarak = solve_using_local_saerch(distance_matrix)
    # [0, 1,2,3,4]
    for i, value in enumerate(urutan):
        next_path = i + 1
        if next_path > len(urutan)-1:
            next_path = 0
        list_urutan.append(Urutan(from_address=addresses[urutan[i]], to_addresses=addresses[urutan[next_path]], jarak=distance_matrix[urutan[i]][urutan[next_path]]))
    return ResponseOptimizeTsp(urutan_tujuan=list_urutan, jarak=jarak, urutan=urutan, distance_matrix=distance_matrix.tolist())

@app.get("/")
def read_root():
    return {"message": "Arion Api v1.0"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
