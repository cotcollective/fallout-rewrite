#!/usr/bin/env python3
"""Fallout DAT1 LZSS — algorithme officiel Shadowbird (NMA).

Format:
- Stream = blocs. Chaque bloc : Int16 BE N (taille du bloc suivant, SIGNED).
  * N < 0 : |N| octets sont copiés DIRECTEMENT (pas dans le dico).
  * N > 0 : |N| octets à décompresser. Dico vidé (0x20), DI = 4096 - 18.
  * N = 0 : fin.
- Dans un bloc compressé : FL (flags byte), puis 8 items (LSB-first, FL>>1 à chaque item).
  * item odd (FL&1==1) : 1 octet littéral -> sortie + dico[DI].
  * item even (FL&1==0) : DO = octet lu ; L = octet lu ; DO |= (L&0xF0)<<4 ; L&=0x0F ;
    (L+3) octets lus du dico[DO] (wrap), écrits sortie + dico[DI] (DI avance, DO avance).
"""
import struct
import os

DICT_SIZE = 4096
MIN_MATCH = 3
MAX_MATCH = 18


def lzss_decompress(src: bytes) -> bytes:
    out = bytearray()
    i = 0
    n_total = len(src)
    while i < n_total:
        # Read Int16 BE signed N
        if i + 2 > n_total:
            break
        (n,) = struct.unpack('>h', src[i:i + 2])
        i += 2
        if n == 0:
            break
        if n < 0:
            # direct copy, no dict
            out += src[i:i - n]
            i += -n
            if len(out) and 0:
                pass
            continue
        # compressed block of n bytes
        end_block = i + n
        dic = bytearray([0x20] * DICT_SIZE)
        di = DICT_SIZE - MAX_MATCH
        fl = 0
        # We don't know output length directly; read until block bytes consumed
        # But we must decode item-by-item; the block ends when its bytes are read.
        while i < end_block:
            if i >= end_block:
                break
            fl = src[i]; i += 1
            for _ in range(8):
                if i >= end_block:
                    break
                if fl & 1:
                    # literal
                    c = src[i]; i += 1
                    out.append(c)
                    dic[di] = c
                    di = (di + 1) % DICT_SIZE
                else:
                    do = src[i]; i += 1
                    l = src[i]; i += 1
                    do |= (l & 0xF0) << 4
                    l &= 0x0F
                    for _ in range(l + MIN_MATCH):
                        c = dic[do % DICT_SIZE]
                        out.append(c)
                        dic[di] = c
                        di = (di + 1) % DICT_SIZE
                        do += 1
                fl >>= 1
    return bytes(out)


def parse_master(path= '/mnt/WIN1TB/Games/Fallout/fallout-ce/master.dat'):
    data = open(path, 'rb')
    (dc,) = struct.unpack('>i', data.read(4))
    data.read(12)
    names = []
    for _ in range(dc):
        nl = data.read(1)[0]
        names.append(data.read(nl).decode('ascii', 'replace').replace('\\', '/'))
    entries = {}
    for d in range(dc):
        (fc,) = struct.unpack('>i', data.read(4))
        data.read(12)
        pre = (names[d] + '/') if names[d] != '.' else ''
        for _ in range(fc):
            nl = data.read(1)[0]
            fn = data.read(nl).decode('ascii', 'replace')
            a, o, s, p = struct.unpack('>iiii', data.read(16))
            entries[(pre + fn).upper()] = (a, o, s, p)
    return data, entries


if __name__ == '__main__':
    import sys
    data, entries = parse_master()
    key = sys.argv[1].upper() if len(sys.argv) > 1 else 'TEXT\\FRENCH\\GAME/COMBAT.MSG'
    key = key.replace('/', '\\').replace('\\', '|')  # normalize separator variants
    match = None
    for k, v in entries.items():
        # try direct match, and fuzzy on tail
        if k.replace('\\', '|') == key or k.endsWith(key.replace('\\', '|')) if hasattr(k, 'endsWith') else False:
            match = k
            break
    # simpler: find any key whose tail-equal
    tail = sys.argv[1].upper().replace('/', '/')
    for k, v in entries.items():
        kk = k.replace('\\', '/')
        if kk.upper().endswith('/' + tail.upper()) or kk.upper() == tail.upper():
            match = k; break
    if not match:
        print('NOT FOUND', sys.argv[1], file=sys.stderr)
        sys.exit(1)
    a, o, s, p = entries[match]
    print(f'# {match} attrs={a} off={o} size={s} packed={p}', file=sys.stderr)
    data.seek(o)
    raw = data.read(p if p else s)
    if p:
        raw = lzss_decompress(raw)
    sys.stdout.buffer.write(raw)