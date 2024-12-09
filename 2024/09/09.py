def transform_disk_map(disk_map: str) -> list:
    res = []
    i = 0
    for k, num in enumerate(disk_map):
        if not k % 2:
            res += [i]*int(num)
            i += 1
        else:
            res += [None]*int(num)
    return res


def defragment(disk_map: list) -> list:
    defrag = disk_map[:]
    try:
        while None in defrag:
            defrag[defrag.index(None)] = defrag.pop()
    except ValueError:
        pass
    return defrag


def transform_disk_map_better(disk_map: str) -> dict:
    blocks = dict()
    file_id = 0
    cur = 0
    for k, num in enumerate(disk_map):
        if not k % 2:
            blocks[cur] = {'id': file_id, 'size': int(num)}
            file_id += 1
        else:
            blocks[cur] = {'size': int(num)}
        cur += int(num)
    return blocks


def defragment_better(disk_map: dict) -> dict:
    defrag = disk_map.copy()
    for i in reversed(disk_map.keys()):
        if 'id' in disk_map[i]:
            for k in sorted(defrag.keys()):
                if k < i and 'id' not in defrag[k] and defrag[k]['size'] >= disk_map[i]['size']:
                    if defrag[k]['size'] > disk_map[i]['size']:
                        defrag[k+disk_map[i]['size']] = {'size': defrag[k]['size']-disk_map[i]['size']}
                    defrag[k] = disk_map[i].copy()
                    defrag[i].pop('id')
                    break
    return defrag


def disk_map_dict_to_str(disk_map: dict) -> str:
    res = ''
    for k in sorted(disk_map.keys()):
        if 'id' in disk_map[k]:
            res += str(disk_map[k]['id'])*disk_map[k]['size']
        else:
            res += '.'*disk_map[k]['size']
    return res


def disk_map_dict_to_list(disk_map: dict) -> list:
    res = []
    for k in sorted(disk_map.keys()):
        if 'id' in disk_map[k]:
            res += [disk_map[k]['id']]*disk_map[k]['size']
        else:
            res += [0]*disk_map[k]['size']
    return res


def checksum(defragmented_disk_map: list) -> int:
    return sum(i*num for i, num in enumerate(defragmented_disk_map))


def part_1(data: str) -> int:
    return checksum(defragment(transform_disk_map(data)))


def part_2(data: str) -> int:
    defrag = defragment_better(transform_disk_map_better(data))
    return checksum(disk_map_dict_to_list(defrag))


with open('input.txt') as f:
    data = f.read()

print(part_2(data))
