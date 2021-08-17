from collections import deque
from subway_graph import create_station_graph

# -----------------------------------------------------------------------------
# class StationNode:
#     """지하철 역 노드를 나타내는 클래스"""
#     def __init__(self, name, num_exits) -> None:
#         self.name = name
#         self.num_exits = num_exits


# # 지하철 역 노드 인스턴스 생성
# station_0 = StationNode("교대역", 14)
# station_1 = StationNode("사당역", 14)
# station_2 = StationNode("종로3가역", 16)
# station_3 = StationNode("서울역", 16)

# # 노드들을 파이썬 리스트에 저장
# stations = [station_0, station_1, station_2, station_3]

# # 노드들을 파이썬 딕셔너리에 저장한다.
# stations_dict = {
#     "교대역" : station_0,
#     "사당역" : station_1,
#     "종로3가역" : station_2,
#     "서울역" : station_3
# }

# node_1 = stations_dict["교대역"]

# -----------------------------------------------------------------------------
def bfs(graph, start_node):
    """시작 노드에서 bfs를 실행하는 함수"""
    queue = deque() # 빈 큐 생성

    # 모든 노드를 방문하지 않은 노드로 표시
    for station_node in graph.values():
        station_node.visited = False

    # 시작점 노드를 방문 표시한 후 큐에 넣어준다.
    start_node.visited = True
    queue.append(start_node)

    while queue: # 큐에 노드가 있는 동안
        current_station = queue.popleft() # 큐의 가장 앞 데이터를 갖고 온다.
        for neighbor in current_station.adjacent_stations: # 인접한 노드를 돌면서
            if neighbor.visited == False: # 방문하지 않은 노드면
                neighbor.visited = True # 방문 표시를 하고
                queue.append(neighbor) # 큐에 넣는다.

stations = create_station_graph("E:\\PythonWorkspace\\data_structure\\Graph\\new_stations.txt")  # stations.txt 파일로 그래프를 만든다

gangnam_station = stations["강남"]

# 강남역과 경로를 통해 연결된 모든 노드를 탐색
bfs(stations, gangnam_station)

# 강남역과 서울 지하철 역들이 연결됐는지 확인
print(stations["강동구청"].visited)
print(stations["평촌"].visited)
print(stations["송도"].visited)
print(stations["개화산"].visited)

# 강남역과 대전 지하철 역들이 연결됐는지 확인
print(stations["반석"].visited)
print(stations["지족"].visited)
print(stations["노은"].visited)
print(stations["(대전)신흥"].visited)