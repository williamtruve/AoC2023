def intersect_ranges(range_a, range_b):
    start = max(range_a[0], range_b[0])
    end = min(range_a[1], range_b[1])
    
    if start < end:
        return [(start, end)]
    else:
        return []

def disjoint_ranges(range_a, range_b):
    result = []
    
    # Check if range_a starts before range_b
    if range_a[0] < range_b[0]:
        result.append((range_a[0], min(range_a[1], range_b[0])))
    
    # Check if range_a ends after range_b
    if range_a[1] > range_b[1]:
        result.append((max(range_a[0], range_b[1]), range_a[1]))
    
    return result

def map_range(input_range, source_range, target_range, should_map=True):
    if should_map and input_range[0] >= source_range[0] and input_range[1] <= source_range[1]:
        offset = target_range[0] - source_range[0]
        
        # Map the input range to the target range
        mapped_start = input_range[0] + offset
        mapped_stop =  input_range[1] + offset
        
        return (mapped_start, mapped_stop)
    
    else:
        return input_range



