# %% [markdown]
# Palindrome

# %%
def is_palindrome(str):
    return str.lower().replace(' ', '') == str.lower().replace(' ', '')[::-1]

# %%
is_palindrome("A man a plan a canal Panama")

# %%
is_palindrome("Anna")


