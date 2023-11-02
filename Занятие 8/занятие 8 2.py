s=" я решаю задачи по программированию"
def alf(s):
    slovo=s.split()
    sort_slowo=[]
    for i in slovo:
        sort_s=''.join(sorted(i))
        sort_slowo.append(sort_s)

    sort_s=' '.join(sort_slowo)
    return sort_s

izm_s=alf(s)
print(izm_s)