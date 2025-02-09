# %% [markdown]
# In this task, you need to check if the characters in a given string are permutations.

# %%
from collections import Counter

# %%
def is_permutation(str1, str2):
    if len(str1) != len(str2):
        return False
    elif set(str1)!=set(str2):
        return False
    else: return Counter(str1) == Counter(str1)

# %%
print(is_permutation("abc", "bca"))
print(is_permutation("xyz", "xyzv")) 
print(is_permutation("mad", "Mad")) 


