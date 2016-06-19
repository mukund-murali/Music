scale = ['F', 'G', 'A', 'B^', 'C', 'D', 'E', 'F']

all_chords = []

def get_proper_index(i):
    if i > len(scale) - 1:
        return ((i + 1) % len(scale))
    return i


def print_chord(chord):
    print "     {:3} {:3} {:3}".format(chord[0], chord[1], chord[2])


# This holds for each key all possible chords
per_key_chords = {}
for i, key in enumerate(scale):
    chord_indices = [
        i, get_proper_index(i + 2), get_proper_index(i + 4)
    ]
    chord = [scale[i] for i in chord_indices]
    # Writing all chords for this key in a dict
    for key in chord:
        chords = per_key_chords.get(key, [])
        chords.append(chord)
        per_key_chords[key] = chords
    all_chords.append(chord)

print '-' * 20
print 'All chords'
print '-' * 20
for chord in all_chords:
    print_chord(chord)

print '^' * 20
print ''
for key in scale:
    print ''
    print '"', key, '"'
    for chord in per_key_chords[key]:
        print_chord(chord)

print '-' * 20
