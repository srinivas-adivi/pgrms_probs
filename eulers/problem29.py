def problem29():
    l = [a**b for a in range(2,101) for b in range(2,101)]
    print len(set(l))
problem29()
