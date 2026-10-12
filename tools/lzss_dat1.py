#!/usr/bin/env python3
"""DAT1 LZSS decompressor — correct variant for Fallout 1 master.dat.

DAT1 LZSS uses a ring buffer of 4096 bytes; on offset==0 special behavior.
Reference: libfallout / fallout-dat tooling.
"""
import struct


def lzss_decompress(src: bytes) -> bytes:
    ring = bytearray(4096)   # ring buffer, initialized to spaces or zeros
    ring_pos = 0
    out = bytearray()
    (length,) = struct.unpack('>I', src[0:4])
    i = 4
    while i < len(src) and len(out) < length:
        bitflags = src[i]; i += 1
        for bit in range(8):
            flag = (bitflags >> (7 - bit)) & 1
            if flag == 1:
                ring[ring_pos] = src[i]
                ring_pos = (ring_pos + 1) & 0xFFF
                out.append(src[i]); i += 1
            else:
                b1, b2 = src[i], src[i + 1]
                i += 2
                pos = ((b1 >> 4) << 8) | b2  # ring buffer offset (12 bits)
                count = (b1 & 0x0F) + 2      # run length 2..17
                for _ in range(count):
                    c = ring[pos & 0xFFF]
                    ring[ring_pos] = c
                    ring_pos = (ring_pos + 1) & 0xFFF
                    pos = (pos + 1) & 0xFFF
                    out.append(c)
    return bytes(out)