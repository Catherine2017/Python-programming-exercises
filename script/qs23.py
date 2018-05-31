import zlib
s = b"Hello word! hello world! hello world!"
t = zlib.compress(s)
print(len(s))
print(len(t))
print(zlib.decompress(t))
