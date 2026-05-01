# 7-Segment Display - All Possible Combinations

Total combinations: **256** (2^8)

Segments: A, B, C, D, E, F, G, DP (mapped to pins GP8, GP7, GP5, GP4, GP14, GP15, GP27, GP28)

## Visual Reference
```
  AAA
 F   B
 F   B
  GGG
 E   C
 E   C
  DDD   DP
```

## Legend
- `█` = segment ON
- `·` = segment OFF

---

## All 256 Combinations

**0: Binary 00000000 - Segments: none**
```
  ···
 ·   ·
 ·   ·
  ···
 ·   ·
 ·   ·
  ···   ·
```

**1: Binary 00000001 - Segments: A**
```
  ███
 ·   ·
 ·   ·
  ···
 ·   ·
 ·   ·
  ···   ·
```

**2: Binary 00000010 - Segments: B**
```
  ···
 ·   █
 ·   █
  ···
 ·   ·
 ·   ·
  ···   ·
```

**3: Binary 00000011 - Segments: A,B**
```
  ███
 ·   █
 ·   █
  ···
 ·   ·
 ·   ·
  ···   ·
```

**4: Binary 00000100 - Segments: C**
```
  ···
 ·   ·
 ·   ·
  ···
 ·   █
 ·   █
  ···   ·
```

**5: Binary 00000101 - Segments: A,C**
```
  ███
 ·   ·
 ·   ·
  ···
 ·   █
 ·   █
  ···   ·
```

**6: Binary 00000110 - Segments: B,C**
```
  ···
 ·   █
 ·   █
  ···
 ·   █
 ·   █
  ···   ·
```

**7: Binary 00000111 - Segments: A,B,C**
```
  ███
 ·   █
 ·   █
  ···
 ·   █
 ·   █
  ···   ·
```

**8: Binary 00001000 - Segments: D**
```
  ···
 ·   ·
 ·   ·
  ···
 ·   ·
 ·   ·
  ███   ·
```

**9: Binary 00001001 - Segments: A,D**
```
  ███
 ·   ·
 ·   ·
  ···
 ·   ·
 ·   ·
  ███   ·
```

**10: Binary 00001010 - Segments: B,D**
```
  ···
 ·   █
 ·   █
  ···
 ·   ·
 ·   ·
  ███   ·
```

**11: Binary 00001011 - Segments: A,B,D**
```
  ███
 ·   █
 ·   █
  ···
 ·   ·
 ·   ·
  ███   ·
```

**12: Binary 00001100 - Segments: C,D**
```
  ···
 ·   ·
 ·   ·
  ···
 ·   █
 ·   █
  ███   ·
```

**13: Binary 00001101 - Segments: A,C,D**
```
  ███
 ·   ·
 ·   ·
  ···
 ·   █
 ·   █
  ███   ·
```

**14: Binary 00001110 - Segments: B,C,D**
```
  ···
 ·   █
 ·   █
  ···
 ·   █
 ·   █
  ███   ·
```

**15: Binary 00001111 - Segments: A,B,C,D**
```
  ███
 ·   █
 ·   █
  ···
 ·   █
 ·   █
  ███   ·
```

**16: Binary 00010000 - Segments: E**
```
  ···
 ·   ·
 ·   ·
  ···
 █   ·
 █   ·
  ···   ·
```

**17: Binary 00010001 - Segments: A,E**
```
  ███
 ·   ·
 ·   ·
  ···
 █   ·
 █   ·
  ···   ·
```

**18: Binary 00010010 - Segments: B,E**
```
  ···
 ·   █
 ·   █
  ···
 █   ·
 █   ·
  ···   ·
```

**19: Binary 00010011 - Segments: A,B,E**
```
  ███
 ·   █
 ·   █
  ···
 █   ·
 █   ·
  ···   ·
```

**20: Binary 00010100 - Segments: C,E**
```
  ···
 ·   ·
 ·   ·
  ···
 █   █
 █   █
  ···   ·
```

**21: Binary 00010101 - Segments: A,C,E**
```
  ███
 ·   ·
 ·   ·
  ···
 █   █
 █   █
  ···   ·
```

**22: Binary 00010110 - Segments: B,C,E**
```
  ···
 ·   █
 ·   █
  ···
 █   █
 █   █
  ···   ·
```

**23: Binary 00010111 - Segments: A,B,C,E**
```
  ███
 ·   █
 ·   █
  ···
 █   █
 █   █
  ···   ·
```

**24: Binary 00011000 - Segments: D,E**
```
  ···
 ·   ·
 ·   ·
  ···
 █   ·
 █   ·
  ███   ·
```

**25: Binary 00011001 - Segments: A,D,E**
```
  ███
 ·   ·
 ·   ·
  ···
 █   ·
 █   ·
  ███   ·
```

**26: Binary 00011010 - Segments: B,D,E**
```
  ···
 ·   █
 ·   █
  ···
 █   ·
 █   ·
  ███   ·
```

**27: Binary 00011011 - Segments: A,B,D,E**
```
  ███
 ·   █
 ·   █
  ···
 █   ·
 █   ·
  ███   ·
```

**28: Binary 00011100 - Segments: C,D,E**
```
  ···
 ·   ·
 ·   ·
  ···
 █   █
 █   █
  ███   ·
```

**29: Binary 00011101 - Segments: A,C,D,E**
```
  ███
 ·   ·
 ·   ·
  ···
 █   █
 █   █
  ███   ·
```

**30: Binary 00011110 - Segments: B,C,D,E**
```
  ···
 ·   █
 ·   █
  ···
 █   █
 █   █
  ███   ·
```

**31: Binary 00011111 - Segments: A,B,C,D,E**
```
  ███
 ·   █
 ·   █
  ···
 █   █
 █   █
  ███   ·
```

**32: Binary 00100000 - Segments: F**
```
  ···
 █   ·
 █   ·
  ···
 ·   ·
 ·   ·
  ···   ·
```

**33: Binary 00100001 - Segments: A,F**
```
  ███
 █   ·
 █   ·
  ···
 ·   ·
 ·   ·
  ···   ·
```

**34: Binary 00100010 - Segments: B,F**
```
  ···
 █   █
 █   █
  ···
 ·   ·
 ·   ·
  ···   ·
```

**35: Binary 00100011 - Segments: A,B,F**
```
  ███
 █   █
 █   █
  ···
 ·   ·
 ·   ·
  ···   ·
```

**36: Binary 00100100 - Segments: C,F**
```
  ···
 █   ·
 █   ·
  ···
 ·   █
 ·   █
  ···   ·
```

**37: Binary 00100101 - Segments: A,C,F**
```
  ███
 █   ·
 █   ·
  ···
 ·   █
 ·   █
  ···   ·
```

**38: Binary 00100110 - Segments: B,C,F**
```
  ···
 █   █
 █   █
  ···
 ·   █
 ·   █
  ···   ·
```

**39: Binary 00100111 - Segments: A,B,C,F**
```
  ███
 █   █
 █   █
  ···
 ·   █
 ·   █
  ···   ·
```

**40: Binary 00101000 - Segments: D,F**
```
  ···
 █   ·
 █   ·
  ···
 ·   ·
 ·   ·
  ███   ·
```

**41: Binary 00101001 - Segments: A,D,F**
```
  ███
 █   ·
 █   ·
  ···
 ·   ·
 ·   ·
  ███   ·
```

**42: Binary 00101010 - Segments: B,D,F**
```
  ···
 █   █
 █   █
  ···
 ·   ·
 ·   ·
  ███   ·
```

**43: Binary 00101011 - Segments: A,B,D,F**
```
  ███
 █   █
 █   █
  ···
 ·   ·
 ·   ·
  ███   ·
```

**44: Binary 00101100 - Segments: C,D,F**
```
  ···
 █   ·
 █   ·
  ···
 ·   █
 ·   █
  ███   ·
```

**45: Binary 00101101 - Segments: A,C,D,F**
```
  ███
 █   ·
 █   ·
  ···
 ·   █
 ·   █
  ███   ·
```

**46: Binary 00101110 - Segments: B,C,D,F**
```
  ···
 █   █
 █   █
  ···
 ·   █
 ·   █
  ███   ·
```

**47: Binary 00101111 - Segments: A,B,C,D,F**
```
  ███
 █   █
 █   █
  ···
 ·   █
 ·   █
  ███   ·
```

**48: Binary 00110000 - Segments: E,F**
```
  ···
 █   ·
 █   ·
  ···
 █   ·
 █   ·
  ···   ·
```

**49: Binary 00110001 - Segments: A,E,F**
```
  ███
 █   ·
 █   ·
  ···
 █   ·
 █   ·
  ···   ·
```

**50: Binary 00110010 - Segments: B,E,F**
```
  ···
 █   █
 █   █
  ···
 █   ·
 █   ·
  ···   ·
```

**51: Binary 00110011 - Segments: A,B,E,F**
```
  ███
 █   █
 █   █
  ···
 █   ·
 █   ·
  ···   ·
```

**52: Binary 00110100 - Segments: C,E,F**
```
  ···
 █   ·
 █   ·
  ···
 █   █
 █   █
  ···   ·
```

**53: Binary 00110101 - Segments: A,C,E,F**
```
  ███
 █   ·
 █   ·
  ···
 █   █
 █   █
  ···   ·
```

**54: Binary 00110110 - Segments: B,C,E,F**
```
  ···
 █   █
 █   █
  ···
 █   █
 █   █
  ···   ·
```

**55: Binary 00110111 - Segments: A,B,C,E,F**
```
  ███
 █   █
 █   █
  ···
 █   █
 █   █
  ···   ·
```

**56: Binary 00111000 - Segments: D,E,F**
```
  ···
 █   ·
 █   ·
  ···
 █   ·
 █   ·
  ███   ·
```

**57: Binary 00111001 - Segments: A,D,E,F**
```
  ███
 █   ·
 █   ·
  ···
 █   ·
 █   ·
  ███   ·
```

**58: Binary 00111010 - Segments: B,D,E,F**
```
  ···
 █   █
 █   █
  ···
 █   ·
 █   ·
  ███   ·
```

**59: Binary 00111011 - Segments: A,B,D,E,F**
```
  ███
 █   █
 █   █
  ···
 █   ·
 █   ·
  ███   ·
```

**60: Binary 00111100 - Segments: C,D,E,F**
```
  ···
 █   ·
 █   ·
  ···
 █   █
 █   █
  ███   ·
```

**61: Binary 00111101 - Segments: A,C,D,E,F**
```
  ███
 █   ·
 █   ·
  ···
 █   █
 █   █
  ███   ·
```

**62: Binary 00111110 - Segments: B,C,D,E,F**
```
  ···
 █   █
 █   █
  ···
 █   █
 █   █
  ███   ·
```

**63: Binary 00111111 - Segments: A,B,C,D,E,F**
```
  ███
 █   █
 █   █
  ···
 █   █
 █   █
  ███   ·
```

**64: Binary 01000000 - Segments: G**
```
  ···
 ·   ·
 ·   ·
  ███
 ·   ·
 ·   ·
  ···   ·
```

**65: Binary 01000001 - Segments: A,G**
```
  ███
 ·   ·
 ·   ·
  ███
 ·   ·
 ·   ·
  ···   ·
```

**66: Binary 01000010 - Segments: B,G**
```
  ···
 ·   █
 ·   █
  ███
 ·   ·
 ·   ·
  ···   ·
```

**67: Binary 01000011 - Segments: A,B,G**
```
  ███
 ·   █
 ·   █
  ███
 ·   ·
 ·   ·
  ···   ·
```

**68: Binary 01000100 - Segments: C,G**
```
  ···
 ·   ·
 ·   ·
  ███
 ·   █
 ·   █
  ···   ·
```

**69: Binary 01000101 - Segments: A,C,G**
```
  ███
 ·   ·
 ·   ·
  ███
 ·   █
 ·   █
  ···   ·
```

**70: Binary 01000110 - Segments: B,C,G**
```
  ···
 ·   █
 ·   █
  ███
 ·   █
 ·   █
  ···   ·
```

**71: Binary 01000111 - Segments: A,B,C,G**
```
  ███
 ·   █
 ·   █
  ███
 ·   █
 ·   █
  ···   ·
```

**72: Binary 01001000 - Segments: D,G**
```
  ···
 ·   ·
 ·   ·
  ███
 ·   ·
 ·   ·
  ███   ·
```

**73: Binary 01001001 - Segments: A,D,G**
```
  ███
 ·   ·
 ·   ·
  ███
 ·   ·
 ·   ·
  ███   ·
```

**74: Binary 01001010 - Segments: B,D,G**
```
  ···
 ·   █
 ·   █
  ███
 ·   ·
 ·   ·
  ███   ·
```

**75: Binary 01001011 - Segments: A,B,D,G**
```
  ███
 ·   █
 ·   █
  ███
 ·   ·
 ·   ·
  ███   ·
```

**76: Binary 01001100 - Segments: C,D,G**
```
  ···
 ·   ·
 ·   ·
  ███
 ·   █
 ·   █
  ███   ·
```

**77: Binary 01001101 - Segments: A,C,D,G**
```
  ███
 ·   ·
 ·   ·
  ███
 ·   █
 ·   █
  ███   ·
```

**78: Binary 01001110 - Segments: B,C,D,G**
```
  ···
 ·   █
 ·   █
  ███
 ·   █
 ·   █
  ███   ·
```

**79: Binary 01001111 - Segments: A,B,C,D,G**
```
  ███
 ·   █
 ·   █
  ███
 ·   █
 ·   █
  ███   ·
```

**80: Binary 01010000 - Segments: E,G**
```
  ···
 ·   ·
 ·   ·
  ███
 █   ·
 █   ·
  ···   ·
```

**81: Binary 01010001 - Segments: A,E,G**
```
  ███
 ·   ·
 ·   ·
  ███
 █   ·
 █   ·
  ···   ·
```

**82: Binary 01010010 - Segments: B,E,G**
```
  ···
 ·   █
 ·   █
  ███
 █   ·
 █   ·
  ···   ·
```

**83: Binary 01010011 - Segments: A,B,E,G**
```
  ███
 ·   █
 ·   █
  ███
 █   ·
 █   ·
  ···   ·
```

**84: Binary 01010100 - Segments: C,E,G**
```
  ···
 ·   ·
 ·   ·
  ███
 █   █
 █   █
  ···   ·
```

**85: Binary 01010101 - Segments: A,C,E,G**
```
  ███
 ·   ·
 ·   ·
  ███
 █   █
 █   █
  ···   ·
```

**86: Binary 01010110 - Segments: B,C,E,G**
```
  ···
 ·   █
 ·   █
  ███
 █   █
 █   █
  ···   ·
```

**87: Binary 01010111 - Segments: A,B,C,E,G**
```
  ███
 ·   █
 ·   █
  ███
 █   █
 █   █
  ···   ·
```

**88: Binary 01011000 - Segments: D,E,G**
```
  ···
 ·   ·
 ·   ·
  ███
 █   ·
 █   ·
  ███   ·
```

**89: Binary 01011001 - Segments: A,D,E,G**
```
  ███
 ·   ·
 ·   ·
  ███
 █   ·
 █   ·
  ███   ·
```

**90: Binary 01011010 - Segments: B,D,E,G**
```
  ···
 ·   █
 ·   █
  ███
 █   ·
 █   ·
  ███   ·
```

**91: Binary 01011011 - Segments: A,B,D,E,G**
```
  ███
 ·   █
 ·   █
  ███
 █   ·
 █   ·
  ███   ·
```

**92: Binary 01011100 - Segments: C,D,E,G**
```
  ···
 ·   ·
 ·   ·
  ███
 █   █
 █   █
  ███   ·
```

**93: Binary 01011101 - Segments: A,C,D,E,G**
```
  ███
 ·   ·
 ·   ·
  ███
 █   █
 █   █
  ███   ·
```

**94: Binary 01011110 - Segments: B,C,D,E,G**
```
  ···
 ·   █
 ·   █
  ███
 █   █
 █   █
  ███   ·
```

**95: Binary 01011111 - Segments: A,B,C,D,E,G**
```
  ███
 ·   █
 ·   █
  ███
 █   █
 █   █
  ███   ·
```

**96: Binary 01100000 - Segments: F,G**
```
  ···
 █   ·
 █   ·
  ███
 ·   ·
 ·   ·
  ···   ·
```

**97: Binary 01100001 - Segments: A,F,G**
```
  ███
 █   ·
 █   ·
  ███
 ·   ·
 ·   ·
  ···   ·
```

**98: Binary 01100010 - Segments: B,F,G**
```
  ···
 █   █
 █   █
  ███
 ·   ·
 ·   ·
  ···   ·
```

**99: Binary 01100011 - Segments: A,B,F,G**
```
  ███
 █   █
 █   █
  ███
 ·   ·
 ·   ·
  ···   ·
```

**100: Binary 01100100 - Segments: C,F,G**
```
  ···
 █   ·
 █   ·
  ███
 ·   █
 ·   █
  ···   ·
```

**101: Binary 01100101 - Segments: A,C,F,G**
```
  ███
 █   ·
 █   ·
  ███
 ·   █
 ·   █
  ···   ·
```

**102: Binary 01100110 - Segments: B,C,F,G**
```
  ···
 █   █
 █   █
  ███
 ·   █
 ·   █
  ···   ·
```

**103: Binary 01100111 - Segments: A,B,C,F,G**
```
  ███
 █   █
 █   █
  ███
 ·   █
 ·   █
  ···   ·
```

**104: Binary 01101000 - Segments: D,F,G**
```
  ···
 █   ·
 █   ·
  ███
 ·   ·
 ·   ·
  ███   ·
```

**105: Binary 01101001 - Segments: A,D,F,G**
```
  ███
 █   ·
 █   ·
  ███
 ·   ·
 ·   ·
  ███   ·
```

**106: Binary 01101010 - Segments: B,D,F,G**
```
  ···
 █   █
 █   █
  ███
 ·   ·
 ·   ·
  ███   ·
```

**107: Binary 01101011 - Segments: A,B,D,F,G**
```
  ███
 █   █
 █   █
  ███
 ·   ·
 ·   ·
  ███   ·
```

**108: Binary 01101100 - Segments: C,D,F,G**
```
  ···
 █   ·
 █   ·
  ███
 ·   █
 ·   █
  ███   ·
```

**109: Binary 01101101 - Segments: A,C,D,F,G**
```
  ███
 █   ·
 █   ·
  ███
 ·   █
 ·   █
  ███   ·
```

**110: Binary 01101110 - Segments: B,C,D,F,G**
```
  ···
 █   █
 █   █
  ███
 ·   █
 ·   █
  ███   ·
```

**111: Binary 01101111 - Segments: A,B,C,D,F,G**
```
  ███
 █   █
 █   █
  ███
 ·   █
 ·   █
  ███   ·
```

**112: Binary 01110000 - Segments: E,F,G**
```
  ···
 █   ·
 █   ·
  ███
 █   ·
 █   ·
  ···   ·
```

**113: Binary 01110001 - Segments: A,E,F,G**
```
  ███
 █   ·
 █   ·
  ███
 █   ·
 █   ·
  ···   ·
```

**114: Binary 01110010 - Segments: B,E,F,G**
```
  ···
 █   █
 █   █
  ███
 █   ·
 █   ·
  ···   ·
```

**115: Binary 01110011 - Segments: A,B,E,F,G**
```
  ███
 █   █
 █   █
  ███
 █   ·
 █   ·
  ···   ·
```

**116: Binary 01110100 - Segments: C,E,F,G**
```
  ···
 █   ·
 █   ·
  ███
 █   █
 █   █
  ···   ·
```

**117: Binary 01110101 - Segments: A,C,E,F,G**
```
  ███
 █   ·
 █   ·
  ███
 █   █
 █   █
  ···   ·
```

**118: Binary 01110110 - Segments: B,C,E,F,G**
```
  ···
 █   █
 █   █
  ███
 █   █
 █   █
  ···   ·
```

**119: Binary 01110111 - Segments: A,B,C,E,F,G**
```
  ███
 █   █
 █   █
  ███
 █   █
 █   █
  ···   ·
```

**120: Binary 01111000 - Segments: D,E,F,G**
```
  ···
 █   ·
 █   ·
  ███
 █   ·
 █   ·
  ███   ·
```

**121: Binary 01111001 - Segments: A,D,E,F,G**
```
  ███
 █   ·
 █   ·
  ███
 █   ·
 █   ·
  ███   ·
```

**122: Binary 01111010 - Segments: B,D,E,F,G**
```
  ···
 █   █
 █   █
  ███
 █   ·
 █   ·
  ███   ·
```

**123: Binary 01111011 - Segments: A,B,D,E,F,G**
```
  ███
 █   █
 █   █
  ███
 █   ·
 █   ·
  ███   ·
```

**124: Binary 01111100 - Segments: C,D,E,F,G**
```
  ···
 █   ·
 █   ·
  ███
 █   █
 █   █
  ███   ·
```

**125: Binary 01111101 - Segments: A,C,D,E,F,G**
```
  ███
 █   ·
 █   ·
  ███
 █   █
 █   █
  ███   ·
```

**126: Binary 01111110 - Segments: B,C,D,E,F,G**
```
  ···
 █   █
 █   █
  ███
 █   █
 █   █
  ███   ·
```

**127: Binary 01111111 - Segments: A,B,C,D,E,F,G**
```
  ███
 █   █
 █   █
  ███
 █   █
 █   █
  ███   ·
```

**128: Binary 10000000 - Segments: DP**
```
  ···
 ·   ·
 ·   ·
  ···
 ·   ·
 ·   ·
  ···   █
```

**129: Binary 10000001 - Segments: A,DP**
```
  ███
 ·   ·
 ·   ·
  ···
 ·   ·
 ·   ·
  ···   █
```

**130: Binary 10000010 - Segments: B,DP**
```
  ···
 ·   █
 ·   █
  ···
 ·   ·
 ·   ·
  ···   █
```

**131: Binary 10000011 - Segments: A,B,DP**
```
  ███
 ·   █
 ·   █
  ···
 ·   ·
 ·   ·
  ···   █
```

**132: Binary 10000100 - Segments: C,DP**
```
  ···
 ·   ·
 ·   ·
  ···
 ·   █
 ·   █
  ···   █
```

**133: Binary 10000101 - Segments: A,C,DP**
```
  ███
 ·   ·
 ·   ·
  ···
 ·   █
 ·   █
  ···   █
```

**134: Binary 10000110 - Segments: B,C,DP**
```
  ···
 ·   █
 ·   █
  ···
 ·   █
 ·   █
  ···   █
```

**135: Binary 10000111 - Segments: A,B,C,DP**
```
  ███
 ·   █
 ·   █
  ···
 ·   █
 ·   █
  ···   █
```

**136: Binary 10001000 - Segments: D,DP**
```
  ···
 ·   ·
 ·   ·
  ···
 ·   ·
 ·   ·
  ███   █
```

**137: Binary 10001001 - Segments: A,D,DP**
```
  ███
 ·   ·
 ·   ·
  ···
 ·   ·
 ·   ·
  ███   █
```

**138: Binary 10001010 - Segments: B,D,DP**
```
  ···
 ·   █
 ·   █
  ···
 ·   ·
 ·   ·
  ███   █
```

**139: Binary 10001011 - Segments: A,B,D,DP**
```
  ███
 ·   █
 ·   █
  ···
 ·   ·
 ·   ·
  ███   █
```

**140: Binary 10001100 - Segments: C,D,DP**
```
  ···
 ·   ·
 ·   ·
  ···
 ·   █
 ·   █
  ███   █
```

**141: Binary 10001101 - Segments: A,C,D,DP**
```
  ███
 ·   ·
 ·   ·
  ···
 ·   █
 ·   █
  ███   █
```

**142: Binary 10001110 - Segments: B,C,D,DP**
```
  ···
 ·   █
 ·   █
  ···
 ·   █
 ·   █
  ███   █
```

**143: Binary 10001111 - Segments: A,B,C,D,DP**
```
  ███
 ·   █
 ·   █
  ···
 ·   █
 ·   █
  ███   █
```

**144: Binary 10010000 - Segments: E,DP**
```
  ···
 ·   ·
 ·   ·
  ···
 █   ·
 █   ·
  ···   █
```

**145: Binary 10010001 - Segments: A,E,DP**
```
  ███
 ·   ·
 ·   ·
  ···
 █   ·
 █   ·
  ···   █
```

**146: Binary 10010010 - Segments: B,E,DP**
```
  ···
 ·   █
 ·   █
  ···
 █   ·
 █   ·
  ···   █
```

**147: Binary 10010011 - Segments: A,B,E,DP**
```
  ███
 ·   █
 ·   █
  ···
 █   ·
 █   ·
  ···   █
```

**148: Binary 10010100 - Segments: C,E,DP**
```
  ···
 ·   ·
 ·   ·
  ···
 █   █
 █   █
  ···   █
```

**149: Binary 10010101 - Segments: A,C,E,DP**
```
  ███
 ·   ·
 ·   ·
  ···
 █   █
 █   █
  ···   █
```

**150: Binary 10010110 - Segments: B,C,E,DP**
```
  ···
 ·   █
 ·   █
  ···
 █   █
 █   █
  ···   █
```

**151: Binary 10010111 - Segments: A,B,C,E,DP**
```
  ███
 ·   █
 ·   █
  ···
 █   █
 █   █
  ···   █
```

**152: Binary 10011000 - Segments: D,E,DP**
```
  ···
 ·   ·
 ·   ·
  ···
 █   ·
 █   ·
  ███   █
```

**153: Binary 10011001 - Segments: A,D,E,DP**
```
  ███
 ·   ·
 ·   ·
  ···
 █   ·
 █   ·
  ███   █
```

**154: Binary 10011010 - Segments: B,D,E,DP**
```
  ···
 ·   █
 ·   █
  ···
 █   ·
 █   ·
  ███   █
```

**155: Binary 10011011 - Segments: A,B,D,E,DP**
```
  ███
 ·   █
 ·   █
  ···
 █   ·
 █   ·
  ███   █
```

**156: Binary 10011100 - Segments: C,D,E,DP**
```
  ···
 ·   ·
 ·   ·
  ···
 █   █
 █   █
  ███   █
```

**157: Binary 10011101 - Segments: A,C,D,E,DP**
```
  ███
 ·   ·
 ·   ·
  ···
 █   █
 █   █
  ███   █
```

**158: Binary 10011110 - Segments: B,C,D,E,DP**
```
  ···
 ·   █
 ·   █
  ···
 █   █
 █   █
  ███   █
```

**159: Binary 10011111 - Segments: A,B,C,D,E,DP**
```
  ███
 ·   █
 ·   █
  ···
 █   █
 █   █
  ███   █
```

**160: Binary 10100000 - Segments: F,DP**
```
  ···
 █   ·
 █   ·
  ···
 ·   ·
 ·   ·
  ···   █
```

**161: Binary 10100001 - Segments: A,F,DP**
```
  ███
 █   ·
 █   ·
  ···
 ·   ·
 ·   ·
  ···   █
```

**162: Binary 10100010 - Segments: B,F,DP**
```
  ···
 █   █
 █   █
  ···
 ·   ·
 ·   ·
  ···   █
```

**163: Binary 10100011 - Segments: A,B,F,DP**
```
  ███
 █   █
 █   █
  ···
 ·   ·
 ·   ·
  ···   █
```

**164: Binary 10100100 - Segments: C,F,DP**
```
  ···
 █   ·
 █   ·
  ···
 ·   █
 ·   █
  ···   █
```

**165: Binary 10100101 - Segments: A,C,F,DP**
```
  ███
 █   ·
 █   ·
  ···
 ·   █
 ·   █
  ···   █
```

**166: Binary 10100110 - Segments: B,C,F,DP**
```
  ···
 █   █
 █   █
  ···
 ·   █
 ·   █
  ···   █
```

**167: Binary 10100111 - Segments: A,B,C,F,DP**
```
  ███
 █   █
 █   █
  ···
 ·   █
 ·   █
  ···   █
```

**168: Binary 10101000 - Segments: D,F,DP**
```
  ···
 █   ·
 █   ·
  ···
 ·   ·
 ·   ·
  ███   █
```

**169: Binary 10101001 - Segments: A,D,F,DP**
```
  ███
 █   ·
 █   ·
  ···
 ·   ·
 ·   ·
  ███   █
```

**170: Binary 10101010 - Segments: B,D,F,DP**
```
  ···
 █   █
 █   █
  ···
 ·   ·
 ·   ·
  ███   █
```

**171: Binary 10101011 - Segments: A,B,D,F,DP**
```
  ███
 █   █
 █   █
  ···
 ·   ·
 ·   ·
  ███   █
```

**172: Binary 10101100 - Segments: C,D,F,DP**
```
  ···
 █   ·
 █   ·
  ···
 ·   █
 ·   █
  ███   █
```

**173: Binary 10101101 - Segments: A,C,D,F,DP**
```
  ███
 █   ·
 █   ·
  ···
 ·   █
 ·   █
  ███   █
```

**174: Binary 10101110 - Segments: B,C,D,F,DP**
```
  ···
 █   █
 █   █
  ···
 ·   █
 ·   █
  ███   █
```

**175: Binary 10101111 - Segments: A,B,C,D,F,DP**
```
  ███
 █   █
 █   █
  ···
 ·   █
 ·   █
  ███   █
```

**176: Binary 10110000 - Segments: E,F,DP**
```
  ···
 █   ·
 █   ·
  ···
 █   ·
 █   ·
  ···   █
```

**177: Binary 10110001 - Segments: A,E,F,DP**
```
  ███
 █   ·
 █   ·
  ···
 █   ·
 █   ·
  ···   █
```

**178: Binary 10110010 - Segments: B,E,F,DP**
```
  ···
 █   █
 █   █
  ···
 █   ·
 █   ·
  ···   █
```

**179: Binary 10110011 - Segments: A,B,E,F,DP**
```
  ███
 █   █
 █   █
  ···
 █   ·
 █   ·
  ···   █
```

**180: Binary 10110100 - Segments: C,E,F,DP**
```
  ···
 █   ·
 █   ·
  ···
 █   █
 █   █
  ···   █
```

**181: Binary 10110101 - Segments: A,C,E,F,DP**
```
  ███
 █   ·
 █   ·
  ···
 █   █
 █   █
  ···   █
```

**182: Binary 10110110 - Segments: B,C,E,F,DP**
```
  ···
 █   █
 █   █
  ···
 █   █
 █   █
  ···   █
```

**183: Binary 10110111 - Segments: A,B,C,E,F,DP**
```
  ███
 █   █
 █   █
  ···
 █   █
 █   █
  ···   █
```

**184: Binary 10111000 - Segments: D,E,F,DP**
```
  ···
 █   ·
 █   ·
  ···
 █   ·
 █   ·
  ███   █
```

**185: Binary 10111001 - Segments: A,D,E,F,DP**
```
  ███
 █   ·
 █   ·
  ···
 █   ·
 █   ·
  ███   █
```

**186: Binary 10111010 - Segments: B,D,E,F,DP**
```
  ···
 █   █
 █   █
  ···
 █   ·
 █   ·
  ███   █
```

**187: Binary 10111011 - Segments: A,B,D,E,F,DP**
```
  ███
 █   █
 █   █
  ···
 █   ·
 █   ·
  ███   █
```

**188: Binary 10111100 - Segments: C,D,E,F,DP**
```
  ···
 █   ·
 █   ·
  ···
 █   █
 █   █
  ███   █
```

**189: Binary 10111101 - Segments: A,C,D,E,F,DP**
```
  ███
 █   ·
 █   ·
  ···
 █   █
 █   █
  ███   █
```

**190: Binary 10111110 - Segments: B,C,D,E,F,DP**
```
  ···
 █   █
 █   █
  ···
 █   █
 █   █
  ███   █
```

**191: Binary 10111111 - Segments: A,B,C,D,E,F,DP**
```
  ███
 █   █
 █   █
  ···
 █   █
 █   █
  ███   █
```

**192: Binary 11000000 - Segments: G,DP**
```
  ···
 ·   ·
 ·   ·
  ███
 ·   ·
 ·   ·
  ···   █
```

**193: Binary 11000001 - Segments: A,G,DP**
```
  ███
 ·   ·
 ·   ·
  ███
 ·   ·
 ·   ·
  ···   █
```

**194: Binary 11000010 - Segments: B,G,DP**
```
  ···
 ·   █
 ·   █
  ███
 ·   ·
 ·   ·
  ···   █
```

**195: Binary 11000011 - Segments: A,B,G,DP**
```
  ███
 ·   █
 ·   █
  ███
 ·   ·
 ·   ·
  ···   █
```

**196: Binary 11000100 - Segments: C,G,DP**
```
  ···
 ·   ·
 ·   ·
  ███
 ·   █
 ·   █
  ···   █
```

**197: Binary 11000101 - Segments: A,C,G,DP**
```
  ███
 ·   ·
 ·   ·
  ███
 ·   █
 ·   █
  ···   █
```

**198: Binary 11000110 - Segments: B,C,G,DP**
```
  ···
 ·   █
 ·   █
  ███
 ·   █
 ·   █
  ···   █
```

**199: Binary 11000111 - Segments: A,B,C,G,DP**
```
  ███
 ·   █
 ·   █
  ███
 ·   █
 ·   █
  ···   █
```

**200: Binary 11001000 - Segments: D,G,DP**
```
  ···
 ·   ·
 ·   ·
  ███
 ·   ·
 ·   ·
  ███   █
```

**201: Binary 11001001 - Segments: A,D,G,DP**
```
  ███
 ·   ·
 ·   ·
  ███
 ·   ·
 ·   ·
  ███   █
```

**202: Binary 11001010 - Segments: B,D,G,DP**
```
  ···
 ·   █
 ·   █
  ███
 ·   ·
 ·   ·
  ███   █
```

**203: Binary 11001011 - Segments: A,B,D,G,DP**
```
  ███
 ·   █
 ·   █
  ███
 ·   ·
 ·   ·
  ███   █
```

**204: Binary 11001100 - Segments: C,D,G,DP**
```
  ···
 ·   ·
 ·   ·
  ███
 ·   █
 ·   █
  ███   █
```

**205: Binary 11001101 - Segments: A,C,D,G,DP**
```
  ███
 ·   ·
 ·   ·
  ███
 ·   █
 ·   █
  ███   █
```

**206: Binary 11001110 - Segments: B,C,D,G,DP**
```
  ···
 ·   █
 ·   █
  ███
 ·   █
 ·   █
  ███   █
```

**207: Binary 11001111 - Segments: A,B,C,D,G,DP**
```
  ███
 ·   █
 ·   █
  ███
 ·   █
 ·   █
  ███   █
```

**208: Binary 11010000 - Segments: E,G,DP**
```
  ···
 ·   ·
 ·   ·
  ███
 █   ·
 █   ·
  ···   █
```

**209: Binary 11010001 - Segments: A,E,G,DP**
```
  ███
 ·   ·
 ·   ·
  ███
 █   ·
 █   ·
  ···   █
```

**210: Binary 11010010 - Segments: B,E,G,DP**
```
  ···
 ·   █
 ·   █
  ███
 █   ·
 █   ·
  ···   █
```

**211: Binary 11010011 - Segments: A,B,E,G,DP**
```
  ███
 ·   █
 ·   █
  ███
 █   ·
 █   ·
  ···   █
```

**212: Binary 11010100 - Segments: C,E,G,DP**
```
  ···
 ·   ·
 ·   ·
  ███
 █   █
 █   █
  ···   █
```

**213: Binary 11010101 - Segments: A,C,E,G,DP**
```
  ███
 ·   ·
 ·   ·
  ███
 █   █
 █   █
  ···   █
```

**214: Binary 11010110 - Segments: B,C,E,G,DP**
```
  ···
 ·   █
 ·   █
  ███
 █   █
 █   █
  ···   █
```

**215: Binary 11010111 - Segments: A,B,C,E,G,DP**
```
  ███
 ·   █
 ·   █
  ███
 █   █
 █   █
  ···   █
```

**216: Binary 11011000 - Segments: D,E,G,DP**
```
  ···
 ·   ·
 ·   ·
  ███
 █   ·
 █   ·
  ███   █
```

**217: Binary 11011001 - Segments: A,D,E,G,DP**
```
  ███
 ·   ·
 ·   ·
  ███
 █   ·
 █   ·
  ███   █
```

**218: Binary 11011010 - Segments: B,D,E,G,DP**
```
  ···
 ·   █
 ·   █
  ███
 █   ·
 █   ·
  ███   █
```

**219: Binary 11011011 - Segments: A,B,D,E,G,DP**
```
  ███
 ·   █
 ·   █
  ███
 █   ·
 █   ·
  ███   █
```

**220: Binary 11011100 - Segments: C,D,E,G,DP**
```
  ···
 ·   ·
 ·   ·
  ███
 █   █
 █   █
  ███   █
```

**221: Binary 11011101 - Segments: A,C,D,E,G,DP**
```
  ███
 ·   ·
 ·   ·
  ███
 █   █
 █   █
  ███   █
```

**222: Binary 11011110 - Segments: B,C,D,E,G,DP**
```
  ···
 ·   █
 ·   █
  ███
 █   █
 █   █
  ███   █
```

**223: Binary 11011111 - Segments: A,B,C,D,E,G,DP**
```
  ███
 ·   █
 ·   █
  ███
 █   █
 █   █
  ███   █
```

**224: Binary 11100000 - Segments: F,G,DP**
```
  ···
 █   ·
 █   ·
  ███
 ·   ·
 ·   ·
  ···   █
```

**225: Binary 11100001 - Segments: A,F,G,DP**
```
  ███
 █   ·
 █   ·
  ███
 ·   ·
 ·   ·
  ···   █
```

**226: Binary 11100010 - Segments: B,F,G,DP**
```
  ···
 █   █
 █   █
  ███
 ·   ·
 ·   ·
  ···   █
```

**227: Binary 11100011 - Segments: A,B,F,G,DP**
```
  ███
 █   █
 █   █
  ███
 ·   ·
 ·   ·
  ···   █
```

**228: Binary 11100100 - Segments: C,F,G,DP**
```
  ···
 █   ·
 █   ·
  ███
 ·   █
 ·   █
  ···   █
```

**229: Binary 11100101 - Segments: A,C,F,G,DP**
```
  ███
 █   ·
 █   ·
  ███
 ·   █
 ·   █
  ···   █
```

**230: Binary 11100110 - Segments: B,C,F,G,DP**
```
  ···
 █   █
 █   █
  ███
 ·   █
 ·   █
  ···   █
```

**231: Binary 11100111 - Segments: A,B,C,F,G,DP**
```
  ███
 █   █
 █   █
  ███
 ·   █
 ·   █
  ···   █
```

**232: Binary 11101000 - Segments: D,F,G,DP**
```
  ···
 █   ·
 █   ·
  ███
 ·   ·
 ·   ·
  ███   █
```

**233: Binary 11101001 - Segments: A,D,F,G,DP**
```
  ███
 █   ·
 █   ·
  ███
 ·   ·
 ·   ·
  ███   █
```

**234: Binary 11101010 - Segments: B,D,F,G,DP**
```
  ···
 █   █
 █   █
  ███
 ·   ·
 ·   ·
  ███   █
```

**235: Binary 11101011 - Segments: A,B,D,F,G,DP**
```
  ███
 █   █
 █   █
  ███
 ·   ·
 ·   ·
  ███   █
```

**236: Binary 11101100 - Segments: C,D,F,G,DP**
```
  ···
 █   ·
 █   ·
  ███
 ·   █
 ·   █
  ███   █
```

**237: Binary 11101101 - Segments: A,C,D,F,G,DP**
```
  ███
 █   ·
 █   ·
  ███
 ·   █
 ·   █
  ███   █
```

**238: Binary 11101110 - Segments: B,C,D,F,G,DP**
```
  ···
 █   █
 █   █
  ███
 ·   █
 ·   █
  ███   █
```

**239: Binary 11101111 - Segments: A,B,C,D,F,G,DP**
```
  ███
 █   █
 █   █
  ███
 ·   █
 ·   █
  ███   █
```

**240: Binary 11110000 - Segments: E,F,G,DP**
```
  ···
 █   ·
 █   ·
  ███
 █   ·
 █   ·
  ···   █
```

**241: Binary 11110001 - Segments: A,E,F,G,DP**
```
  ███
 █   ·
 █   ·
  ███
 █   ·
 █   ·
  ···   █
```

**242: Binary 11110010 - Segments: B,E,F,G,DP**
```
  ···
 █   █
 █   █
  ███
 █   ·
 █   ·
  ···   █
```

**243: Binary 11110011 - Segments: A,B,E,F,G,DP**
```
  ███
 █   █
 █   █
  ███
 █   ·
 █   ·
  ···   █
```

**244: Binary 11110100 - Segments: C,E,F,G,DP**
```
  ···
 █   ·
 █   ·
  ███
 █   █
 █   █
  ···   █
```

**245: Binary 11110101 - Segments: A,C,E,F,G,DP**
```
  ███
 █   ·
 █   ·
  ███
 █   █
 █   █
  ···   █
```

**246: Binary 11110110 - Segments: B,C,E,F,G,DP**
```
  ···
 █   █
 █   █
  ███
 █   █
 █   █
  ···   █
```

**247: Binary 11110111 - Segments: A,B,C,E,F,G,DP**
```
  ███
 █   █
 █   █
  ███
 █   █
 █   █
  ···   █
```

**248: Binary 11111000 - Segments: D,E,F,G,DP**
```
  ···
 █   ·
 █   ·
  ███
 █   ·
 █   ·
  ███   █
```

**249: Binary 11111001 - Segments: A,D,E,F,G,DP**
```
  ███
 █   ·
 █   ·
  ███
 █   ·
 █   ·
  ███   █
```

**250: Binary 11111010 - Segments: B,D,E,F,G,DP**
```
  ···
 █   █
 █   █
  ███
 █   ·
 █   ·
  ███   █
```

**251: Binary 11111011 - Segments: A,B,D,E,F,G,DP**
```
  ███
 █   █
 █   █
  ███
 █   ·
 █   ·
  ███   █
```

**252: Binary 11111100 - Segments: C,D,E,F,G,DP**
```
  ···
 █   ·
 █   ·
  ███
 █   █
 █   █
  ███   █
```

**253: Binary 11111101 - Segments: A,C,D,E,F,G,DP**
```
  ███
 █   ·
 █   ·
  ███
 █   █
 █   █
  ███   █
```

**254: Binary 11111110 - Segments: B,C,D,E,F,G,DP**
```
  ···
 █   █
 █   █
  ███
 █   █
 █   █
  ███   █
```

**255: Binary 11111111 - Segments: A,B,C,D,E,F,G,DP**
```
  ███
 █   █
 █   █
  ███
 █   █
 █   █
  ███   █
```

---

## Summary
- Total combinations: 256
- Segment mapping: A=GP8, B=GP7, C=GP5, D=GP4, E=GP14, F=GP15, G=GP27, DP=GP28
- Each segment can independently be ON or OFF
- Common anode: LOW (False) = segment ON, HIGH (True) = segment OFF
