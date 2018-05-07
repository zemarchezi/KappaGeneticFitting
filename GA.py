# Program using genetic algorithm to fit data with kappa or maxwellian 
# Created by Marcos Grala
import numpy as np
import evolution as evo
import energy as data
import os, datetime
import fnmatch


######    main program           #################################################333
def main():
    populationSize = 200 # total size of popultion, maybe in the future reduce over time
    threshold = 0.10 # number of top population that will be used for reproduction
    mutationRateBest = 0.001 # chance to mutate de best solution
    numberOfEvolution = 100001 # max number o time steps

    functionType = input("Function ('kappa' or 'maxwellian'): ") ## only works with kappa and maxwellian

    ev_ins = str(input("Event Instant ('yyyymmdd hr:min:sec'): "))

    year = int(ev_ins[0:4])
    month = int(ev_ins[4:6])
    day = int(ev_ins[6:8])
    hour = int(ev_ins[9:11])
    minute = int(ev_ins[12:14])
    second = int(ev_ins[15:17])

    event_instant = datetime.datetime(year, month, day, hour, minute, second) ## instant for data selection

    #13 42 40
    #10 00 00
    xt,yt = data.flux_values(event_instant)
    index = []
    #removing nan from arrays
    for i in xrange(len(xt)):
        if np.isnan(xt[i]) or np.isnan(yt[i]) or yt[i]<1.0:
            index.append(i)

        x = np.delete(xt,index)
        y = np.delete(yt,index)


    # x = x[0:-1]
    # y = y[0:-1]
    #x = np.asarray(x)
    #y = np.asarray(y)
    #print x,y
    #
    #  creates data for test
    #
    # kappa is defined here as
    # y = A x ( 1 + B x )^-C
    #
    # and maxwellian as
    # y = A x exp(-B x)
    #
    # Use three coeficients for kappa and two for maxwellian
    # if vector of y is given ignore this
    if len(y) == 0:
        if functionType=="kappa":
            coefs = [100,0.001,12]
            y,mean = evo.kappa(x,coefs)
        elif functionType == "maxwellian":
            coefs = [100,0.001]
            print "aqui"
            y,mean = evo.function(x,coefs)

    else:
    	mean = sum(y)/len(y)

    ####
    # main evolution of the code
    evo.evolve(functionType,populationSize,threshold,mutationRateBest,
          numberOfEvolution,x,y,mean, event_instant)


if __name__ =="__main__":
    main()
