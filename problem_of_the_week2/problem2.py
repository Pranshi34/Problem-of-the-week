def misere_nim(heaps):
    if all(h == 1 for h in heaps):
        return len(heaps) % 2 == 0
    
    xor_sum = 0
    for h in heaps:
        xor_sum ^= h
    return xor_sum != 0

heaps = list(map(int, input().split()))
print(misere_nim(heaps))
