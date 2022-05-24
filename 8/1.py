import hashlib
def sub_count(s):
    N = len(s)
    hash_set = set()
    for i in range(N + 1):
        for j in range(i + 1, N + 1):
            x = hashlib.sha1(s[i:j].encode('utf-8')).hexdigest()
            hash_set.add(x)
    return len(hash_set)



s = 'abbakadabra'
print(f'Количество различных подстрок {s}:{sub_count(s)}')