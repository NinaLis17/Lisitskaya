s="впкнп.ивапцгшун."
def sim(h):
    h.replace('.',"")
    kolvo=h.count(".")
    return sim,kolvo

izm_strok,t=sim(s)
print("строка без точек:",izm_strok)
print("количество удаленных сиволов:",t)