from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance

def run():
    stations = build_station_list()

    coord=(52.2053, 0.1218)
    x=stations_by_distance(stations,coord)

    closest10=x[:10]
    furthest10=x[-10:]
    closest_data=[]
    furthest_data=[]
    for i in range(10):
        closest_data.append((closest10[i][0].name,closest10[i][0].town,closest10[i][1]))
        furthest_data.append((furthest10[i][0].name,furthest10[i][0].town,furthest10[i][1]))

        print(closest_data)
        print(furthest_data)

if __name__ == "__main__":
    run()