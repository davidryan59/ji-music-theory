import random
import csv
import math
from src.Factors import Factors
from src.Fraction import Fraction
from src.functions import isprime, gcd, factorise, factorise2
from tabulate import tabulate


# This selects the list of primes to work with
MAX_N = 100


note_names_m3 = [
    "Eb", "Bb",
    "F", "C", "G", "D", "A", "E", "B",
    "F#", "C#", "G#", "D#", "A#", "E#", "B#",
    "Fx", "Cx", "Gx", "Dx", "Ax", "Ex", "Bx",
]

ERR_RES = -1
def clean(row):
    try:
        return int(row[0])
    except Exception as e:
        return ERR_RES

# # input primes from CSV
# primes = []
# filename = f"primes_to_{MAX_N}.csv" 
# with open(filename, "r") as csvfile:
#     csvreader = csv.reader(csvfile)
#     primes = [clean(row) for row in csvreader if clean(row) != ERR_RES]

# print(f"{len(primes)} primes have been loaded from file {filename}")



tabulate_data = []
tabulate_headers = ["i \ j"]

# Separate out any rational number into:
# 1. a Pythagorean component
# 2. a product of higher prime commas
# d = 16
imin, imax = 6, 42
jmin, jmax = 4, 18
imin, imax = 8, 24
jmin, jmax = 6, 9
imult = 1
jmult = 1
# for i in range(6, 10+1):
add_headers = True
for i in range(imin, imax + 1):
    # for j in range(120, 130+1):
    tab_row = [i]
    for j in range(jmin, jmax + 1):
        if add_headers:
            tabulate_headers.append(j)
        i0 = i * imult
        j0 = j * jmult
        # fs = Factors(num=i, denom=2 ** (int(math.log(i)/math.log(2))))
        fs = Factors(num=i0, denom=j0)
        fs_notate = fs.get_ji_notation()
        # print(f"{i0}/{j0}   {fs.get_fraction()}   {fs_notate}")
        tab_row.append(fs_notate)
    
    add_headers = False
    tabulate_data.append(tab_row)


# # tabulate_data.sort(key=lambda row:row[1])  # Sort rows by symbol, which is 2nd row (index 1)
# print("")
# print(tabulate(tabulate_data, headers=tabulate_headers))




data = [
    [144, 144],
    [150, 144],
    [152, 144],
    [153, 144],
    [156, 144],
    [160, 144],
    [162, 144],
    [168, 144],
    [171, 144],
    [174, 144],
    [176, 144],
    [180, 144],
    [184, 144],
    [186, 144],
    [189, 144],
    [192, 144],
    [198, 144],
    [200, 144],
    [204, 144],
    [207, 144],
    [208, 144],
    [216, 144],
    [224, 144],
    [225, 144],
    [228, 144],
    [232, 144],
    [234, 144],
    [240, 144],
    [243, 144],
    [248, 144],
    [252, 144],
    [256, 144],
    [261, 144],
    [264, 144],
    [270, 144],
    [272, 144],
    [276, 144],
    [279, 144],
    [288, 144],
]

# for datum in data:
#     fs = Factors(num=datum[0], denom=datum[1])

#     print(fs.get_fraction(), fs.get_pitch_class_notation())
#     # print(fs.get_pitch_class_notation())


# data = [
#     [1, 1],
#     [3, 2],
#     [5, 4],
#     [6, 4],
#     [35, 21],
#     [60, 77],
#     [33, 22],
#     [15, 12],
# ]
# fss = [Factors(num=datum[0], denom=datum[1]) for datum in data]
# r = range(len(data))

# for i in r:
#     fs = fss[i]
#     for j in r:
#         if i >= j:
#             continue
#         fs2 = fss[j]
#         print(data[i], data[j], fs.get_fraction(), fs2.get_fraction(), fs==fs2, fs is fs2)

# print(fss)
# print(set(fss))



# s = [{1: 2, 3: 4}, {1: 2, 3: 4}, {1: 2, 3: 5}, {1: 2, 4: 5}]
# for s1 in s:
#     for s2 in s:
#         print (s1, s2, s1 == s2, s1 is s2)

# print(s)
# print(set(s))

utonal_pivot = [45, 8]
scale_notes = [1, 3, 5, 7, 9, 11, 13, 15]
transpose_scale = [[1, 1], [4, 3], [3, 2]]
# lim = Factors(num=scale_notes[0] * 2)
fs_utonal_pivot = Factors(num=utonal_pivot[0], denom=utonal_pivot[1])
fs1 = Factors.one()
fs2 = Factors(num=2)

res = set()
for a in transpose_scale:
    for b in scale_notes:
        fs_otonal = Factors(num=a[0]*b, denom=a[1]*scale_notes[0])
        fs_utonal = fs_utonal_pivot / fs_otonal
        for fs in [fs_otonal, fs_utonal]:
            # repeatedly multiply or divide until fs between 1/1 and 2/1
            while fs > fs2:
                fs /= fs2
            while fs < fs1:
                fs *= fs2
            res.add(fs)


# res = list(res)
# res.sort()
# print("")
# for fs in res:
#     print(fs.get_fraction(shorten=False), fs.get_pitch_class_notation())


# print("")
# print(f"There are {len(res)-1} notes in the octave")
# print("")

# data = [
#     12, 14, 16, 18, 21, 24, 47
# ]

# for d in data:
#     fs = Factors(num=d)
#     print(d, fs.get_ji_notation())


denom = 32
scale_txt = ""
notation_txt = ""
fs0 = Factors(num=256, denom=denom)
for i in range(128):
    freq = 32 + (i+1) * 4
    fs = Factors(num=freq, denom=denom)
    pn = (fs/fs0).get_ji_notation()
    # print(freq, pn)
    notation_txt += f'"{pn}|" '
    scale_txt += f"{freq}/{denom}\n"

# print("")
# print(scale_txt)
# print("")
# print(notation_txt)
# print("")






freq_list_list = []
note_name_list = []

scale = [
    [4, 4],
    [5, 4],
    [6, 4],
    [7, 4],
    [23, 11],
    [2, 1],
]

scale = [
    128,
130,
132,
135,
136,
138,
140,
144,
145,
150,
152,
153,
155,
156,
160,
162,
165,
168,
170,
171,
174,
176,
180,
184,
186,
189,
190,
192,
195,
198,
200,
204,
207,
208,
210,
216,
220,
224,
225,
228,
230,
232,
234,
240,
243,
248,
250,
252,
255,
256,
260,
261,
264,
270,
272,
276,
279,
280,
285,
288,
290,
300,
304,
306,
310,
312,
315,
320,
324,
330,
336,
340,
342,
345,
348,
352,
360,
368,
372,
375,
378,
380,
384,
390,
396,
400,
405,
408,
414,
416,
420,
432,
435,
440,
448,
450,
456,
460,
464,
465,
468,
480,
486,
496,
500,
504,
510,
512,
520,
522,
528,
540,
544,
552,
558,
560,
570,
576,
580,
600,
608,
612,
620,
624,
630,
640,
648,
660,
1024
]

scale_len = len(scale) - 1
counter = 0
for row in scale:
    # n = row[0]
    # m = row[1]
    n = row
    m = scale[0]
    fs = Factors(num=n, denom=m)
    freq_list_list.append(f"{n}/{m}")
    note_name_list.append(f'"{counter} {fs.get_pitch_class_notation()} "')
    counter += 1


template = """! <FILENAME>.ascl
!
<DESCRIPTION>>
!
<NOTES_IN_SCALE>
!
<LIST_OF_FREQS_ON_NEWLINES>
!
! @ABL NOTE_NAMES <LIST_OF_DOUBLEQUOTED_NOTE_NAMES_SPACE_SEPARATED>
! @ABL REFERENCE_PITCH <OCTAVE> <NOTE_NUMBER> <FREQ_HZ>
! @ABL NOTE_RANGE_BY_INDEX <MIN_NOTE_OCTAVE> <MIN_NOTE_NUMBER>
! @ABL SOURCE <SOURCE>
! @ABL LINK <LINK>"""


template = template.replace("<NOTES_IN_SCALE>", str(scale_len))
template = template.replace("<LIST_OF_FREQS_ON_NEWLINES>", "\n".join(freq_list_list[1:]))
template = template.replace("<LIST_OF_DOUBLEQUOTED_NOTE_NAMES_SPACE_SEPARATED>", " ".join(note_name_list[:-1]))
template = template.replace("<OCTAVE> <NOTE_NUMBER> <FREQ_HZ>", f"{3} {0} {128}")
template = template.replace("<MIN_NOTE_OCTAVE> <MIN_NOTE_NUMBER>", f"{3} {0}")
# print(template)
# print(template.replace("<LIST_OF_FREQS_ON_NEWLINES>", "1/1\n2/1"))

# print(freq_list_list)
# print(note_name_list)

# TODO: want to generate a .ascl file from this to import into Ableton


# scale1 = [4, 8, 9, 12]
# scale2 = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
# scale3 = [2, 3, 5]


start_index = 5
end_index = 7
scale1 = [8, 9, 12, 16]
# scale2 = [24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]
scale2 = [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
scale3 = [1, 2, 4, 8]
denom = scale1[0] * scale2[0] * scale3[0]

s = set()
for i in scale1:
    for j in scale2:
        for k in scale3:
            # s.add(i*j*k/denom)
            # s.add(Factors(num=i*j*k*128, denom=denom*3))
            # s.add(Factors(num=i*j*k))
            s.add(Factors(num=128 * i*j*k, denom=288 * 256))


print("")
s = list(s)
s.sort()
# s = [i for i in s if i >= 64 and i <= 1024]
s = s[start_index:-end_index]

print([a.get_fraction() for a in s])
print(len(s))

fs0 = Factors(num=5, denom=24)
fs_c4 = Factors(num=1)


tabulate_data = []
tabulate_headers = ["i \ j"]

fs00 = s[0]
scale = []
for i in range(len(s)):
    # print(i, s[i].get_fraction(), s[i].get_ji_notation())
    fs = s[i]
    fr = fs.get_fraction()
    scale.append([fr.num, fr.denom])
    print("Amy Hope")
    fs000 = fs / fs00
    fs00 = fs
    fs1 = fs / fs0
    fs2 = fs / fs_c4
    tabulate_data.append([i,  fs.get_ji_notation(), fs1.get_fraction(), fs.get_fraction().cents(dps=0), fs000.get_fraction(), fs000.get_ji_notation(), fs000.get_fraction().cents(dps=2)])


print("")
print(tabulate(tabulate_data, headers=tabulate_headers))
print("")
print(s[-1]/s[0])
print("")



from src.AbletonTuning import AbletonTuning
print("")


def note_namer_pitch_class_notation(fs: Factors, index: int):
    return fs.get_pitch_class_notation()


def note_namer_get_ji_notation(fs: Factors, index: int):
    return fs.get_ji_notation()



def note_namer_get_full_range_data(fs: Factors, index: int):
    return f"{index} {fs.get_ji_notation()} "








# --------------
# 128-NOTE SCALES

# Shared Setup
ref_pitch_oct = 0
ref_pitch_note = 0
ref_pitch_hz = 54.4692
note_range_min_oct = 0
note_range_min_note = 0
oct_num_in_note_name = True
note_namer_fn = note_namer_get_full_range_data


filename = "128-note_JI_scale"







# --------------
# Multi-NOTE SCALES

# 7-note shared setup
ref_pitch_oct = 4
ref_pitch_note = 0
ref_pitch_hz = 261.63
note_range_min_oct = -4
note_range_min_note = 0
oct_num_in_note_name = False
note_namer_fn = note_namer_pitch_class_notation

filename = "JI_5-limit-Miki"
scale = [
    # [16, 9],
    # [4, 3],
    [1, 1],
    [2, 1],
    [6, 5],
    # [9, 5],
    # [8, 5],
    # [27, 20],
    [3, 2],
    # [9, 8],
    # [27, 16],
    # [10, 9],
    # [5, 3],
    [5, 4],
    [7, 4],
    [9, 5],
    # [15, 8],
]

note_range_min_oct = -1
filename = "JI_12-24_12-note_Otonal"
scale = [
    [12, 12],
    [13, 12],
    [14, 12],
    [15, 12],
    [16, 12],
    [17, 12],
    [18, 12],
    [19, 12],
    [20, 12],
    [21, 12],
    [22, 12],
    [23, 12],
    [24, 12],
]

note_range_min_oct = -1
filename = "JI_12-24_12-note_Utonal"
scale = [
    [24, 24],
    [24, 23],
    [24, 22],
    [24, 21],
    [24, 20],
    [24, 19],
    [24, 18],
    [24, 17],
    [24, 16],
    [24, 15],
    [24, 14],
    [24, 13],
    [24, 12],
]

note_range_min_oct = -1
filename = "JI_12-24_12-note_9-limit_256"
scale = [
    [256, 256],
    [280, 256],
    [288, 256],
    [315, 256],
    [320, 256],
    [336, 256],
    [360, 256],
    [384, 256],
    [420, 256],
    [448, 256],
    [480, 256],
    [504, 256],
    [512, 256],
]

note_range_min_oct = 0
filename = "JI_16-32_16-note_Utonal"
scale = [
    [32, 32],
    [32, 31],
    [32, 30],
    [32, 29],
    [32, 28],
    [32, 27],
    [32, 26],
    [32, 25],
    [32, 24],
    [32, 23],
    [32, 22],
    [32, 21],
    [32, 20],
    [32, 19],
    [32, 18],
    [32, 17],
    [32, 16],
]

note_range_min_oct = 1
filename = "JI_24-48_24-note_Utonal"
scale = [
    [48, 48],
    [48, 47],
    [48, 46],
    [48, 45],
    [48, 44],
    [48, 43],
    [48, 42],
    [48, 41],
    [48, 40],
    [48, 39],
    [48, 38],
    [48, 37],
    [48, 36],
    [48, 35],
    [48, 34],
    [48, 33],
    [48, 32],
    [48, 31],
    [48, 30],
    [48, 29],
    [48, 28],
    [48, 27],
    [48, 26],
    [48, 25],
    [48, 24],
]

# note_range_min_oct = -1
# filename = "JI_12-24_12-note_9-limit_192"
# scale = [
#     [192, 192],
#     [210, 192],
#     [224, 192],
#     [240, 192],
#     [252, 192],
#     [256, 192],
#     [280, 192],
#     [288, 192],
#     [315, 192],
#     [320, 192],
#     [336, 192],
#     [360, 192],
#     [384, 192],
# ]

# note_range_min_oct = 1
# note_range_min_note = 12
# filename = "JI_24-48_24-note_Utonal"
# scale = [
#     [48, 48],
#     [48, 47],
#     [48, 46],
#     [48, 45],
#     [48, 44],
#     [48, 43],
#     [48, 42],
#     [48, 41],
#     [48, 40],
#     [48, 39],
#     [48, 38],
#     [48, 37],
#     [48, 36],
#     [48, 35],
#     [48, 34],
#     [48, 33],
#     [48, 32],
#     [48, 31],
#     [48, 30],
#     [48, 29],
#     [48, 28],
#     [48, 27],
#     [48, 26],
#     [48, 25],
#     [48, 24],
# ]



# # --------------
# # SEVEN-NOTE SCALES

# # 7-note shared setup
# ref_pitch_oct = 4
# ref_pitch_note = 0
# ref_pitch_hz = 261.63
# note_range_min_oct = -4
# note_range_min_note = 1
# oct_num_in_note_name = False
# note_namer_fn = note_namer_pitch_class_notation

# filename = "7-note_23-limit"
# scale = [
#     [12, 12],
#     [13, 12],
#     [15, 12],
#     [16, 12],
#     [18, 12],
#     [19, 12],
#     [23, 12],
#     [24, 12],
# ]

# filename = "7-note_5-limit_diatonic"
# scale = [
#     [24, 24],
#     [27, 24],
#     [30, 24],
#     [32, 24],
#     [36, 24],
#     [40, 24],
#     [45, 24],
#     [48, 24],
# ]



# filename = "Amy_Hope_tuning"
# scale = [
#     [26, 26],
#     [28, 26],
#     [30, 26],
#     [31, 26],
#     [35, 26],
#     [36, 26],
#     [38, 26],
#     [52, 26],
# ]


# ----------------
# PENTATONIC SCALES

# # Pentatonic Shared Setup
# ref_pitch_oct = 4
# ref_pitch_note = 0
# ref_pitch_hz = 261.63
# note_range_min_oct = -8
# note_range_min_note = 0
# oct_num_in_note_name = False
# note_namer_fn = note_namer_pitch_class_notation

# filename = "harmonic_otonal_pentatonic"
# scale = [
#     [5, 5],
#     [6, 5],
#     [7, 5],
#     [8, 5],
#     [9, 5],
#     [10, 5],
# ]

# filename = "harmonic_utonal_pentatonic"
# scale = [
#     [10, 10],
#     [10, 9],
#     [10, 8],
#     [10, 7],
#     [10, 6],
#     [10, 5],
# ]

# filename = "13-limit_pentatonic"
# scale = [
#     [12, 12],
#     [13, 12],
#     [15, 12],
#     [18, 12],
#     [20, 12],
#     [24, 12],
# ]

# filename = "major_5-limit_pentatonic"
# scale = [
#     [16, 16],
#     [18, 16],
#     [20, 16],
#     [24, 16],
#     [30, 16],
#     [32, 16],
# ]

# filename = "minor_5-limit_pentatonic"
# scale = [
#     [32, 32],
#     [32, 30],
#     [32, 24],
#     [32, 20],
#     [32, 18],
#     [32, 16],
# ]


# filename = "utonal_7-limit_pentatonic"
# scale = [
#     [32, 32],
#     [32, 28],
#     [32, 24],
#     [32, 21],
#     [32, 18],
#     [32, 16],
# ]


# filename = "otonal_7-limit_pentatonic"
# scale = [
#     [16, 16],
#     [18, 16],
#     [21, 16],
#     [24, 16],
#     [28, 16],
#     [32, 16],
# ]


freq_fractions = []
note_names = []
fscale = [Factors(note[0], note[1]) for note in scale]
fscale.sort()
fs0 = fscale[0]
for index in range(len(fscale)):
    fs = fscale[index]
    # note = scale[index]
    # num = note[0]
    # denom = note[1]
    # fs = Factors(num, denom)
    freq_fractions.append(f"{(fs / fs0).get_fraction(shorten=False)}")  # Scala format requires first fraction to be 1/1
    note_names.append(note_namer_fn(fs=fs, index=index))  # Note name of first note in scale might not be C4

ascl = AbletonTuning(
    # directory="/Users/davidryan/Downloads/ableton_tunings",
    directory="/Users/davidryan/OneDrive/OneDrive A/Ableton/ableton_tunings",
    filename=filename,
    freq_fractions=freq_fractions,
    note_names=note_names,
    oct_num_in_note_name=oct_num_in_note_name,
    ref_pitch_oct=ref_pitch_oct,
    ref_pitch_note=ref_pitch_note,
    ref_pitch_hz=ref_pitch_hz,
    note_range_min_oct=note_range_min_oct,
    note_range_min_note=note_range_min_note,
)
print(ascl)


ascl.savefile()



# print("")
# s = [i / denom for i in s]
# s = s[:128]
# print(s)
# print(len(s))


# for i in range(len(s)-1):
#     print(1200*math.log(s[i+1]/s[i])/math.log(2))

# print("")
# s2 = [s[0]*s[-1]/i for i in s]
# s2.sort()
# print(s2)

# print("")
# s3 = [*s, *s2]
# s3 = list(set(s3))
# s3.sort()
# print(s3)
# print(len(s3))


# print("")
# for i in range(len(s3)-1):
#     print(1200*math.log(s3[i+1]/s3[i])/math.log(2))

raise

l2 = math.log(2)
l3 = math.log(3)
res0 = []
for prime in primes:
# for prime in range(1000000, 2000000, 50000):

    if prime < 5:
        continue

    comma = Factors.get_prime_comma(prime)
    print(prime, comma.get_fraction(), comma)
    continue

    # Refactor this out to separate script, it is now a single function in Factors
    lp = math.log(prime)
    mid3 = 0.5 * lp/l3
    min3A = round(mid3 - 5.5)
    max3A = round(mid3 + 5.5)
    min3B = 0
    max3B = round(mid3 * 2)
    min3 = min(min3A, min3B)
    max3 = max(max3A, max3B)
    # print(round(mid3, 3), [min3, max3], [min3A, max3A], [min3B, max3B])

    # for bm in range(min3, max3 + 1):
    #     height2 = lp - bm * l3
    #     am = round(height2 / l2)
    #     cm = abs(lp - am * l2 - bm * l3) * (lp + abs(am) * l2 + abs(bm) * l3)
    #     cents = 1200 * (lp - am * l2 - bm * l3) / l2
    #     num = prime * 2 ** max(0, -am) * 3 ** max(0, -bm)
    #     denom = 2 ** max(0, am) * 3 ** max(0, bm)
    #     res.append([prime, num, denom, int(num/prime), denom, am, bm, round(cm, 6), round(cents, 3), abs(round(cents, 3))])

    res = []
    for b in range(-max3, -min3 + 1):
        height2 = lp + b * l3
        a = -round(height2 / l2)
        cm = abs(lp + a * l2 + b * l3) * (lp + abs(a) * l2 + abs(b) * l3)
        cents = 1200 * (lp + a * l2 + b * l3) / l2
        num = prime * 2 ** max(0, a) * 3 ** max(0, b)
        denom = 2 ** max(0, -a) * 3 ** max(0, -b)
        note_name = f"{note_names_m3[3 - b]}[{prime}]"
        res.append([prime, num, denom, int(num/prime), denom, a, b, round(cm, 6), round(cents, 3), note_name])
    
    A_INDEX = 5
    B_INDEX = 6   # index of `b`
    CM_INDEX = 7  # index of `cm` in array above
    CENTS_INDEX = 8  # index of `cents``
    res.sort(key=lambda item: item[CM_INDEX])

    # # Print several results
    # print("")
    # for r in res[:4]:
    #     print(r)

    # Print main result
    # print(res[0])

    res0.append(res[0])


# Check that powers work
p = 67
comma = Factors.get_prime_comma(p)
for pow in range(-50, 51):
    print(p, pow, comma, comma ** pow)




res00 = [*res0]
res0.sort(key=lambda row: abs(row[CENTS_INDEX]))  # sort by abs(cents) increasing

# Smallest commas
print("")
for row in res0[:20]:
    print(row)

# Largest commas
print("")
for row in res0[-50:]:
    print(row)

# res00.sort(reverse=True, key=lambda row: row[B_INDEX])  # sort by b decreasing


for i in range(100):
    n = 12 + int(random.random() * 13)
    m = 2 + int(random.random() * 11)
    print(f"{n}/{m} ", factorise2(n, m))
    


print(Factors(num = 20))
print(Factors(num = 60, denom = 210))
print(Factors(factors = {3:1, 2:-2, 5:0}))
print(Factors(num = 20) / Factors(num = 4))

# print("")
# for row in res00[:50]:
#     # if row[B_INDEX] > 0:  # only allow positive b
#         # print(row)
#         p = row[0]
#         a = row[A_INDEX]
#         b = row[B_INDEX]
#         dc = {p: 1, 2: a, 3: b}
#         fs_p = Factors(factors={p: 1})
#         fs_comma = Factors(factors=dc)
#         fs_pythag = fs_p / fs_comma
#         print("")
#         print(p)
#         print(fs_comma)
#         print(fs_pythag.get_fraction())


# print(Factors)

# for q in range(100):
#     p = int(3 * math.exp(q - 20))
#     print("")
#     print(p)
#     print(p, isprime(p))


# def print_it(fs):
#     print("")
#     print(fs)
#     print(fs.get_factor_dict())
#     print(fs.get_fraction())


# a = Factors(factors={2:2, 3:1})
# print_it(a)

# b = Factors(factors={2:4, 3:-4, 5:1})
# print_it(b)

# c = a * b
# print_it(c)

# d = a / b
# print_it(d)

# print_it(a)
# print_it(b)


# for a in range(48, 60 + 1):
#     for b in range(24, 30 + 1):
#         print(f"Fraction of {a} and {b} is {Fraction(a, b)}")


# for a in range(5040, 1000000, 30030):
#     print(a, factorise(a))

# p * 2^a * 3^b is close to 1
# log(p * 2^a * 3^b) is close to 0
# |log(p * 2^a * 3^b)| is a small positive number
# log(p * 2^|a| * 3^|b|)
