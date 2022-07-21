#!/usr/local/bin/python3

islands_map = [
	[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
	[0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
	[0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
]















class Island:
    def __init__(self, x, y):
        self.area = 1
        self.x = x
        self.y = y

islands = []
islands_index = {}
islands_map_width = len(islands_map[0])
islands_map_height = len(islands_map)
r = []

def find_max_area():
    for i in range(islands_map_height):
        for j in range(islands_map_width):
            print(i, j, islands_map[i][j])
            if islands_map[i][j] == 0:
                continue
            cur_index = islands_map_width * i + j
            cur_id = -1
            if j > 0 and islands_map[i][j-1] == 1:
                index = islands_map_width * i + j - 1
                if index in islands_index:
                    cur_id = islands_index[index]
                    islands_index[cur_index] = cur_id
                    islands[cur_id].area += 1
            if i > 0 and islands_map[i-1][j] == 1:
                index = islands_map_width * (i - 1) + j
                if index in islands_index:
                    if cur_id == -1:
                        cur_id = islands_index[index]
                        islands_index[cur_index] = cur_id
                        islands[cur_id].area += 1
                    elif islands_index[index] != islands_index[cur_index]:
                        r.append((islands_index[index], islands_index[cur_index]))
            if cur_id == -1:
                islands.append(Island(i, j))
                islands_index[cur_index] = len(islands) - 1
                
    print(r)
    for i in range(0, len(islands)):
        print("%d (%d, %d) %d" % (i, islands[i].x, islands[i].y, islands[i].area))

def find_area(x, y):
    pass

def find_max_area2():
    for i in range(islands_map_height):
        for j in range(islands_map_width):
            if islands_map[i][j] == 0:
                continue
            print(i, j, islands_map[i][j])
            

if __name__ == '__main__':
    find_max_area()




