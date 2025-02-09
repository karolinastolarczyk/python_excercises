# %% [markdown]
# Second largest number

# %%
def second_largest(lista):
    if len(set(lista)) == 1:
        return None
    l = list(set(lista))
    l.sort()
    return l[-2]

# %%
second_largest([3, 5, 1, 2, 4])


