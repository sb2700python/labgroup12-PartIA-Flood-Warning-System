from floodsystem.flood import stations_highest_rel_level
from floodsystem.flood import stations_level_over_threshold
from floodsystem.station import MonitoringStation

def test_stations_level_over_threshold():
    #no range
    station1 = [MonitoringStation(station_id='2', measure_id='2', label='Station1', coord=(1.23, 4.56), typical_range=None, river='x', town='y')]
    tol = 0.5
    result1 = stations_level_over_threshold(station1,tol)
    assert result1 == []

    #faulty range
    station2 = [MonitoringStation(station_id='2', measure_id='2', label='Station2', coord=(1.23, 4.56), typical_range=(100,0), river='x', town='y')]
    result2 = stations_level_over_threshold(station2,tol)
    assert result2 == []

    station3 = MonitoringStation(station_id='2', measure_id='2', label='Station3', coord=(1.23, 4.56), typical_range=(0,100), river='x', town='y')
    station3.latest_level = 100
    stations3 = [station3]
    result3 = stations_level_over_threshold(stations3,tol)
    assert result3 == [('Station3',1)]

    station4 = MonitoringStation(station_id='2', measure_id='2', label='Station3', coord=(1.23, 4.56), typical_range=(0,100), river='x', town='y')
    station4.latest_level = 100
    stations4 = [station4]
    result4 = stations_level_over_threshold(stations4,1)
    assert result4 == []



def test_stations_highest_rel_level():
    station1 = MonitoringStation(station_id='1', measure_id='1', label='Station1', coord=(1.23, 4.56), typical_range=(0,100), river='x', town='y')
    station1.latest_level = 100
    station2 = MonitoringStation(station_id='2', measure_id='2', label='Station2', coord=(1.23, 4.56), typical_range=(0,100), river='x', town='y')
    station2.latest_level = 99
    stations = [station2,station1]
    result = stations_highest_rel_level(stations,2)
    assert result == [('Station1',1),('Station2',0.99)]