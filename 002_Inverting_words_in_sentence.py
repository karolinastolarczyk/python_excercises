# %% [markdown]
# Inverting words in a sentence

# %%
def reverse_words(str:'str'):
    return ' '.join(str.split()[::-1])

# %%
print(reverse_words('ALA ma Kotka'))
print(reverse_words("I love Python"))
print(reverse_words("Hello world!"))


