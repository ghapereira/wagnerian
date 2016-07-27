import googlemaps
from datetime import datetime
import json
import requests
import networkx as nx

def dist_matrix_gen(origins):
    with open('confs.json', 'r') as fp:
        apikey = json.load(fp)['apidata']['apikey']

    gmaps = googlemaps.Client(key=apikey)

    now = datetime.now()

    matrix = gmaps.distance_matrix(
        origins,
        origins,
        mode="driving",
        language="pt-BR",
        avoid="tolls",
        units="metric",
        departure_time=now,
        traffic_model="best_guess"
    )

    del apikey

    return matrix

def main():
    origins = ["Belo Horizonte, Brazil", "Pintópolis, Brazil",
               "São Francisco, Brazil", "Francisco Sá, Brazil",
               "Francisco Dumont, Brazil", "Coração de Jesus, Brazil",
               "Ibiaí, Brazil", "Ponto Chique, Brazil",
               "São Romão, Brazil", "Brasília de Minas, Brazil"]

    matrix = dist_matrix_gen(origins)
    print(matrix)

    #dist_graph = nx.Graph()
    '''
    rowid = 0
    for orig in matrix['origin_addresses']:
        dist_graph.add_node(orig)

        colid = 0
        for el in matrix['rows'][rowid]['elements']:
            if colid != rowid:
                dist_graph.add_edge()
                dataline += str(el['distance']['value'])

            colid += 1

        rowid += 1
    '''
    #print(dist_graph.nodes())

if __name__ == '__main__':
    main()

