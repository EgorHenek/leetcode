class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda meeting: meeting[0])
        free_rooms_heap = list(range(n))
        used_rooms = []
        heapq.heapify(free_rooms_heap)
        rooms_counter = [0] * n
        for start, end in meetings:
            while used_rooms and used_rooms[0][0] <= start:
                _, room = heapq.heappop(used_rooms)
                heapq.heappush(free_rooms_heap, room)
            if free_rooms_heap:
                room = heapq.heappop(free_rooms_heap)
                heapq.heappush(used_rooms, [end, room])
            else:
                room_availability_time, room = heapq.heappop(used_rooms)
                heapq.heappush(used_rooms, [room_availability_time + end - start, room])
            rooms_counter[room] += 1
        return rooms_counter.index(max(rooms_counter))