kontinye = True

while kontinye:
    nonb = input("Antre yon nonb ant 0 a 10 pou afiche tab miltiplikasyon l: ")
    while (not nonb.isdigit()):
        nonb = input("Antre yon nonb ant 0 a 10 pou afiche tab miltiplikasyon l: ")
    nonb = int(nonb)
    while (nonb < 0 or nonb > 10):
        nonb = int(input("Antre yon nonb ant 0 a 10 pou afiche tab miltiplikasyon l: "))
    for n in range(1,11):
        print(n, "X", nonb, "=", n*nonb)
    print()
    anko = input("Tape 'W' si w vle afiche yon lòt tab epi 'N' si w vle fini pwogram nan: ").upper()
    if anko == "W":
        kontinye = True
    else:
        kontinye = False
