def rabin_karp(t, p, d=256, q=1_000_003):
    n, m = len(t), len(p)
    if m > n:
        return []
    
    h = pow(d, m - 1, q) # d^(m-1) mod q
    hp = ht = 0

    for i in range(m): # preprocesamiento: O(m)
        hp = (d * hp + ord(p[i])) % q
        ht = (d * ht + ord(t[i])) % q
    res = []

    for s in range(n - m + 1):
        if hp == ht and t[s:s + m] == p: # verificaci´on: O(m)
            res.append(s)
        if s < n - m: # hash rodante: O(1)
            ht = (d * (ht - ord(t[s]) * h) + ord(t[s + m])) % q
    return res
