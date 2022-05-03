import numpy as np

# My comment : You should clarify whether student
# has to consider about "CORNER" values or not (and how).
# Corner values are the FIRST and the LAST value in a graph.

def peak_indexes(x):
    num = x.shape[0]
    pos = np.arange(num)
    mid_pos = pos[1:num-1]
    peak_locations = list()
        
    # head = x[0]
    # mid = x[1:num]
    # toe = x[num-1]
        
    # if head > mid[0]:
    #     peak_locations.append([pos[0]])    
    
    peak_locations.append(list( mid_pos[ (x[mid_pos] > x[mid_pos + 1]) & (x[mid_pos] > x[mid_pos - 1]) ] ))

    # if toe > mid[-2]:
    #     peak_locations.append([pos[num-1]])

    peak_locations = sum(peak_locations, [])

    return peak_locations

def main():
    d = np.array([float(e) for e in input().split()])
    pos = peak_indexes(np.array(d))
    if len(pos) > 0:
        print(", ".join([str(e) for e in pos]))
    else:
        print("No peaks")

exec(input().strip())