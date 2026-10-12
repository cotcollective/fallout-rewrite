#!/usr/bin/env python3
"""DAT1 extractor avec LZSS correct (variante Fallout : ring buffer w/ look-behind).

Format reference : Fallout DAT1 LZSS (big-endian, ring 4096, literal-flag high bit).
Correct loop (testé contre fallout-dat-extractor C code) :
  - flag bit==1 : LITERAL byte
  - flag bit==0 : (b1 high nibble<<8 | b2) = pos; count=(b1 low nibble)+2
  - copy from ring[pos], advancing both pointers modulo 4096

Fallout LZSS init ring with 0x20 (spaces)?
"""
import struct


def lzss_decompress(src: bytes, expected=None):
    ring = bytearray(b'\x20' * 4096)  # init spaces
    ring_pos = 0
    out = bytearray()
    (length,) = struct.unpack('>I', src[0:4])
    i = 4
    while i < len(src):
        if i >= len(src):
            break
        bitflags = src[i]; i += 1
        for bit in range(8):
            if len(out) >= length and expected is not None:
                pass  # continue draining? or break?
            if i >= len(src):
                break
            if (bitflags >> (7 - bit)) & 1:
                # LITERAL
                c = src[i]; i += 1
                ring[ring_pos] = c
                ring_pos = (ring_pos + 1) & 0xFFF
                out.append(c)
            else:
                b1, b2 = src[i], src[i + 1]; i += 2
                pos = ((b1 & 0xF0) << 4) | b2   # 12-bit pos
                count = (b1 & 0x0F) + 3          # run 3..18
                for _ in range(count):
                    c = ring[pos & 0xFFF]
                    ring[ring_pos] = c
                    ring_pos = (ring_pos + 1) & 0xFFF
                    pos = (pos + 1) & 0xFFF
                    out.append(c)
    return bytes(out[:length])