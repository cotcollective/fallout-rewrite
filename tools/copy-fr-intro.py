#!/usr/bin/env python3
"""Copy official FR intro subtitles from master.dat (INTRO.SVE / OVRINTRO.TXT) into ENGLISH cut paths."""
import struct, os

PATH = '/mnt/WIN1TB/Games/Fallout/fallout-ce/master.dat'
OUT = '/mnt/WIN1TB/Games/Fallout/fallout-ce/'

data = open(PATH, 'rb')


def lzss_decompress(src):
    out = bytearray()
    (length,) = struct.unpack('>I', src[0:4])
    i = 4
    while i < len(src) and len(out) < length:
        bitflags = src[i]; i += 1
        for bit in range(8):
            if ((bitflags >> (7 - bit)) & 1) == 1:
                if i >= len(src): break
                out.append(src[i]); i += 1
            else:
                if i + 1 >= len(src): break
                b1 = src[i]; b2 = src[i + 1]; i += 2
                count = (b1 & 0x0F) + 3
                pos = ((b1 & 0xF0) << 4) | b2
                start = len(out) - pos - 1
                for j in range(count):
                    if start + j < 0: break
                    out.append(out[start + j])
    return bytes(out)


# parse tree again (full)
(data_count,) = struct.unpack('>i', data.read(4))
data.read(12)  # unk1..3
names = []
for _ in range(data_count):
    n = data.read(1)[0]
    names.append(data.read(n).decode('ascii', 'replace'))
entries = {}
for d in range(data_count):
    (fc,) = struct.unpack('>i', data.read(4))
    data.read(12)
    for _ in range(fc):
        nl = data.read(1)[0]
        fn = data.read(nl).decode('ascii', 'replace')
        attrs, off, sz, ps = struct.unpack('>iiii', data.read(16))
        full = (names[d].replace('\\', '/') + '/' if names[d] else '/') + fn
        entries[full.upper()] = (attrs, off, sz, ps)

print(f'total entries: {len(entries)}')


def extract(datkey, outpath):
    e = entries.get(datkey.upper())
    if not e:
        print(f'MISS: {datkey}'); return False
    attrs, off, sz, ps = e
    data.seek(off)
    raw = data.read(ps if ps else sz)
    if ps:
        raw = lzss_decompress(raw)
    os.makedirs(os.path.dirname(outpath), exist_ok=True)
    with open(outpath, 'wb') as o:
        o.write(raw)
    print(f'  {datkey} -> {outpath} ({len(raw)}b)')
    return True


# copy official FR subtitles -> ENGLISH paths (interplay official FR)
pairs = [
    ('TEXT/FRENCH/CUTS/INTRO.SVE', OUT + 'data/TEXT/ENGLISH/CUTS/INTRO.SVE'),
    ('TEXT/FRENCH/CUTS/OVRINTRO.SVE', OUT + 'data/TEXT/ENGLISH/CUTS/OVRINTRO.SVE'),
    ('TEXT/FRENCH/CUTS/OVRINTRO.TXT', OUT + 'data/TEXT/ENGLISH/CUTS/OVRINTRO.TXT'),
]
ok = 0
for k, o in pairs:
    if extract(k, o): ok += 1
print(f'done {ok}/{len(pairs)}')

# ALSO extract for repo reference
REPO = '/mnt/WIN1TB/Games/fallout-rewrite/messages/cuts-fr/'
os.makedirs(REPO, exist_ok=True)
for k, _ in pairs:
    name = k.split('/')[-1]
    extract(k, REPO + name)

# verify ENGLISH existing english intros for reference
for ref in ['TEXT/ENGLISH/CUTS/INTRO.SVE', 'TEXT/ENGLISH/CUTS/OVRINTRO.SVE']:
    if ref in entries:
        print('exists in dat:', ref, entries[ref])