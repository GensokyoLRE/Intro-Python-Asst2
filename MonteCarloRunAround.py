"""
Program: MonteCarloRunAround.py
Author: Phillip "Shizuku" Cuesta
Last modified: 9/12/18
Program randoms floats to add or subtract to get the first 6 numbers of pi correct
in an amount of iterations, then calculate avg time per run and avg iterations of the
code per run.
"""
import random
import time

userIterations, totalIterations, totalPasses, iterations, passes, bigRuns, maxRuns = 0, 0, 0, 0, 0, 1, 10
timeTotal, totalTime, completeTime, piCheck, thePi = 0.0, 0.0, 0.0, 0.0, 3.14159
#print("DEBUG: thePi is: " + str(thePi))
lockOn = False
"""
Default run total is 10 total runs of the code from start to finish.
lockOn checks for match with thePi (3.14159) and handles each run dependent 
on a matching set of piCheck's first 6 numbers.
"""

while bigRuns <= maxRuns:
    lockOn = False
    # Verify the check will happen per iteration.
    startTime = time.time()
    # Start the clock (we speedrunners)
    x, y, = 0.0, 0.0
    passes, iterations = 0, 0
    # Reset all values to avoid cross-contamination
    while not lockOn:
        x = random.random()
        y = random.random()
        # Randoms between 0.0 and 1.0 for case checking if it's inside or not.
        if (x != 0.00) and (y != 0.00):
            inside_circle = x * x + y * y <= 1
            iterations += 1
            piCheck = abs(4*(passes/iterations))
            # Preps a check between this and the first 5 decimals/first 6 numbers of pi.
            if inside_circle:
                # Checks for a hit inside.
                passes += 1
            if round(piCheck, 5) == thePi:
                # Missiles locked, thus we call it. (We found a close match, boolean change is now needed.
                lockOn = True

    totalIterations += iterations
    completeTime += time.time() - startTime
    totalTime += completeTime
    totalPasses += passes
    # Four lines of score keeping. Side note: Ask Prof. if there's a way to record a "gold split".
    print("Run " + str(bigRuns) + " had " + str(iterations)
          + " iterations to get within pi range at " + str(round(completeTime, 5)) + " seconds.\n")
    # Say how long it took and how many iterations we needed.
    bigRuns += 1

print("Total iterations: " + str(totalIterations) + "    Total time: " + str(round(totalTime, 5))
      + " seconds\nAverage iteration count is: " + str(round((totalIterations /maxRuns), 0))
      + "    Average runtime is: " + str(round((totalTime/maxRuns), 5)) + " seconds\nTotal within circle is: "
      + str(totalPasses) + " hits.")
# Declare everything in order of: Iteration total, Time total, Avg iterations, Avg runtime, Total hits in circle

input("\nPress Enter to continue...")
# Verify program has hit end and results are readable.

# Aaaaaand.... TIME. Will make a "speedrunning" version of this.
