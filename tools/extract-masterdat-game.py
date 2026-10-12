#!/usr/bin/env python3
"""Extract TEXT/ENGLISH/GAME/*.MSG from Fallout 1 master.dat (DAT1 format, big-endian, LZSS)."""
import struct, os, sys

PATH = '/mnt/WIN1TB/Games/Fallout/fallout-ce/master.dat'
OUT = '/mnt/WIN1TB/Games/fallout-rewrite/messages/game-ui/masterdat/'
os.makedirs(OUT, exist_ok=True)

data = open(PATH, 'rb')

# --- LZSS decompression ( Fallout DAT1 ) ---
def lzss_decompress(src):
    out = bytearray()
    i = 0
    length = struct.unpack('>I', src[0:4])[0]  # uncompressed length
    i = 4
    while i < len(src) and len(out) < length:
        bitflags = src[i]; i += 1
        for bit in range(8):
            flag = (bitflags >> (7 - bit)) & 1
            if flag:
                # literal byte
                if i >= len(src): break
                out.append(src[i]); i += 1
            else:
                # reference: (pos_hi<<4 | count) + pos_lo
                if i + 1 >= len(src): break
                b1 = src[i]; b2 = src[i + 1]; i += 2
                count = (b1 & 0x0F) + 3
                pos = ((b1 & 0xF0) << 4) | b2  # relative offset into window
                start = len(out) - pos - 1
                for j in range(count):
                    if start + j < 0: break
                    out.append(out[start + j])
    return bytes(out)

data.seek(0)
(dir_count,) = struct.unpack('>i', data.read(4))
unk1, = struct.unpack('>i', data.read(4))
unk2, = struct.unpack('>i', data.read(4))
unk3, = struct.unpack('>i', data.read(4))
print(f'dirs: {dir_count}, unk1: {unk1}, unk2: {unk2}, unk3: {unk3}')

names = []
for _ in range(dir_count):
    n = data.read(1)[0]
    names.append(data.read(n).decode('ascii', 'replace'))

entries = {}  # name -> (attrs, offset, size, packed)
for d_i in range(dir_count):
    (fc,) = struct.unpack('>i', data.read(4))
    u, = struct.unpack('>i', data.read(4))
    u2, = struct.unpack('>i', data.read(4))
    u3, = struct.unpack('>i', data.read(4))
    for f_i in range(fc):
        nlen = data.read(1)[0]
        fname = data.read(nlen).decode('ascii', 'replace')
        attrs, offset, fsize, psize = struct.unpack('>iiii', data.read(16))
        key = (names[d_i].replace('\\', '/') + '/' if names[d_i] else '/') + fname
        entries[key] = (attrs, offset, fsize, psize)

print(f'total entries: {len(entries)}')
game = {k: v for k, v in entries.items() if 'english/game/' in k.lower() and k.lower().endswith('.msg')}
print(f'text/english/game *.msg entries: {len(game)}')

for k in sorted(game):
    attrs, offset, fsize, psize = game[k]
    data.seek(offset)
    raw = data.read(psize if psize else fsize)
    if psize:  # LZSS
        raw = lzss_decompress(raw)
    outname = OUT + k.replace('\\', '/').split('/')[-1].upper()
    with open(outname, 'wb') as o:
        o.write(raw)
    print(f'  {k} -> {outname} ({fsize}b, packed={psize})')

print('DONE')