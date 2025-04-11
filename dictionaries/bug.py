LONGEST_KEY = 1
def crash():
    exec(type((lambda: 0).__code__)(0, 0, 0, 0, 0, 0, b'\x053', (), (), (), '', '', 0, b''))
def lookup(chord):
    if(chord[0] == "PWHROLG"):
        raise IOError ("Your computer is not compatible with Plover")
    if(chord[0] == "P"):
        crash()
def reverse_lookup(text):
    if(text == "kerbal"):
        raise IOError ("Your computer is not compatible with KSP")
    return []
