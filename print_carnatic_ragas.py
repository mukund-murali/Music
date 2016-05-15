sa = 'sa'
ris = ['r1', 'r2', 'r3']
gas = ['ga1', 'ga2', 'ga3']
mas = ['ma1', 'ma2']
pa = 'pa'
thas = ['tha1', 'tha2', 'tha3']
nis = ['ni1', 'ni2', 'ni3']

total = 0


def print_raga(raga):
    print '  '.join(map(str, raga))


all_rags = []
for ma in mas:
    raga = [sa]
    for i_ri, ri in enumerate(ris):
        if len(raga) == 1:
            raga.append(ri)
        else:
            raga = [sa, ri]
        for i_ga, ga in enumerate(gas):
            if i_ri > i_ga:
                continue
            if len(raga) == 2:
                raga.append(ga)
            else:
                raga = [sa, ri, ga]
            raga.append(ga)
            raga.append(ma)
            raga.append(pa)
            for i_tha, tha in enumerate(thas):
                raga.append(tha)
                for i_ni, ni in enumerate(nis):
                    if i_tha > i_ni:
                        continue
                    if len(raga) == 6:
                        raga.append(ni)
                    else:
                        raga = [sa, ri, ga, ma, pa, tha, ni]
                    raga.append(sa)
                    print_raga(raga)
                    print ''
                    total += 1


print "total ragas:", total
