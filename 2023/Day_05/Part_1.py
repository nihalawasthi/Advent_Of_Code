from collections import defaultdict

with open("D:\My\Problem Solutions\Advent_of_code_2023\Day_05\input.txt") as file:
    lines = file.read().split('\n')
    lines = [line for line in lines if line]

d = defaultdict(dict)

seeds = [int(k) for k in lines[0][7:].split()]
for line in lines[1:]:
    if 'map' in line:
        src, _, dst = line[:-5].split('-')
        continue

    dst_base, src_base, lenght = [int(k) for k in line.split()]
    d[src][src_base] = (dst_base, lenght)


def _get_mapping(value, resource):
    mappings = sorted(d[resource].items())
    for src, (dst, l) in mappings:
        if value >= src and value < src + l:
            return dst + value - src
    return value


ans = float('inf')
for seed in seeds:
    soil = _get_mapping(seed, 'seed')
    fertilizer = _get_mapping(soil, 'soil')
    water = _get_mapping(fertilizer, 'fertilizer')
    light = _get_mapping(water, 'water')
    temperature = _get_mapping(light, 'light')
    humidity = _get_mapping(temperature, 'temperature')
    location = _get_mapping(humidity, 'humidity')
    ans = min(ans, location)

print(ans)