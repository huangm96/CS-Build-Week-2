def room_search(visited, starting_room, target):
    backwards = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}
    queue = []
    visited_rooms = set()
    start = starting_room['room_id']
    queue.append(start)
    paths = [[]]
    while len(queue) > 0:
        path = paths.pop(0)
        last_room = queue[-1]
        print(f'Last Room {last_room}')
        print(f'Path {path}')
        if last_room == target:
            return path
        else:
            if last_room not in visited_rooms:
                visited_rooms.add(last_room)
                connected_room = []
                for d in visited[str(last_room)]:
                    connected_room.append(d)
                    new_path = path.copy()
                    new_path.append(d)
                    paths.append(new_path)
                # print(f'Connected {connected_room}')
                for connection in connected_room:
                    # print(f'TESTING {visited[str(start)][connection]}')
                    # copy_path = list(path)
                    # copy_path.append(connection)
                    queue.append(visited[str(last_room)][connection])
            else:
                connected_room = []
                for d in visited[str(last_room)]:
                    connected_room.append(d)
                    new_path = path.copy()
                    new_path.append(d)
                    paths.append(new_path)
                for connection in connected_room:
                    queue.append(visited[str(last_room)][connection])
