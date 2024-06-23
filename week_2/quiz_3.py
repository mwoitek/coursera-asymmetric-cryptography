# %%
from math import gcd

# %%
p = 5
q = 11
n = p * q
n

# %%
phi = (p - 1) * (q - 1)
phi

# %%
valid_keys = []
for d in range(2, phi):
    if gcd(d, phi) == 1:
        valid_keys.append(d)
valid_keys

# %%
candidate_keys = [2, 5, 8, 9, 17, 21]
for key in candidate_keys:
    if key in valid_keys:
        print(key)
