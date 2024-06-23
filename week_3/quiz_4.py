# %%
def discrete_log(y, a, p):
    for b in range(1, p):
        if a**b % p == y:
            return b
    return None


# %%
discrete_log(3, 2, 5)

# %%
discrete_log(4, 5, 7)


# %%
def is_primitive_root(a, p):
    powers = set()
    for b in range(1, p):
        powers.add(a**b % p)
    return len(powers) == p - 1


def identify_primitive_roots(candidates, p):
    primitive_roots = []
    for candidate in candidates:
        if is_primitive_root(candidate, p):
            primitive_roots.append(candidate)
    return primitive_roots


# %%
p = 3
candidates = [0, 1, 2]
identify_primitive_roots(candidates, p)

# %%
p = 7
candidates = list(range(1, 7))
identify_primitive_roots(candidates, p)
