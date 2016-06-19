scale = ['F', 'G', 'A', 'B^', 'C', 'D', 'E', 'F']

all_chords = []

def get_proper_index(i):
    if i > len(scale) - 1:
        return ((i + 1) % len(scale))
    return i


def print_chord(chord):
    print "     {:3} {:3} {:3}".format(chord[0], chord[1], chord[2])


# This holds for each key all possible chords
supporting_chords = {}
print '-' * 20
print 'All chords'
print '-' * 20
for i, key in enumerate(scale):
    first_i = i
    second_i = get_proper_index(first_i + 2)
    third_i = get_proper_index(second_i + 2)
    chord_indices = [
        i, get_proper_index(i + 2), get_proper_index(i + 4)
    ]
    chord = [scale[i] for i in chord_indices]
    # Writing all chords for this key in
    for key in chord:
        chords = supporting_chords.get(key, [])
        chords.append(chord)
        supporting_chords[key] = chords
    all_chords.append(chord)

for chord in all_chords:
    print_chord(chord)

print '^' * 20
print ''
for key in scale:
    print ''
    print '"', key, '"'
    for chord in supporting_chords[key]:
        print_chord(chord)

    print '-' * 20
