# -*- coding: utf-8 -*-
import  random
secret = random.randint(0, 20)

while True:
    guess = int(raw_input("Ugani skrito število (Število je med 1 in 20):"))
    if guess == secret:
        print "Čestitke ugotovili ste skrito številko"
        break
    else:
        print "Niste ugotovili skrite številke"