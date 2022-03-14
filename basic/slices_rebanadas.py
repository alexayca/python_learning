
lyric="In a beautiful world"

print(lyric, " : ",len(lyric))

print(lyric[5]," ... ",lyric[13])   # index

# Slices    inicio : final : pasos
print(lyric[5:13], " : ", len(lyric[5:13]))
print(lyric[:13])   # Todo antes del index[13], desde el inicio
print(lyric[5:])    # Todo despues del index[5], hasta el final

# en pasos
print(lyric[5:13:2])
print(lyric[5::2])
print(lyric[:13:2])
print(lyric[::-1])  # toda la cadena, en pasos negativos, es decir al reves 
