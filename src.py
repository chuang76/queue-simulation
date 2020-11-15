import random 
import copy 

def poisson(rate):
    return random.expovariate(rate)

class Customer:
    def __init__(self, id, arrival_time, mu, status):
        self.id = id 
        self.arrival_time = arrival_time
        self.service_time = poisson(mu)         
        self.status = status

Q = 0 
S = [1, 5, 10]
lambds = [0.01, 0.1, 1, 10]
mus = [0.01, 0.04, 0.16, 0.64, 2.56, 10.24]
runs, N = 10, 100000

# print('\nQ = 0')
for s in S:
    print('\n(S = %d) Erlang | block prob' %(s))
    print('-------------------------------')

    for lambd in lambds:
        for mu in mus:
            block_prob = 0                                  # blocking probability 
            for run in range(runs):
                
                system = []                                 # initialize  
                space_server, num_wait = s, 0
                arrival, block = 0, 0      

                # 1st customer 
                system.append(Customer(0, poisson(lambd), mu, True))
                arrival += 1
                space_server -= 1 

                for i in range(1, N):
                    
                    depart = 0                               # number of departure
                    next_arrival = poisson(lambd)

                    # departure 
                    system_cp = copy.copy(system)
                    for c in system:
                        if c.status == True:                 # service
                            t = c.service_time - next_arrival
                            if t <= 0:                       # should leave 
                                system_cp.remove(c)          # remove 
                                space_server += 1            # leave an empty space 
                            else:
                                c.service_time = t           # still process, update the service time 
                    system = system_cp                       # update the system 
                    
                    # queue -> server 
                    for c in system:                         
                        if space_server > 0:               
                            if c.status == False:    
                                c.status = True              # start servicing   
                                num_wait -= 1                
                                space_server -= 1 
                        else:
                            break 

                    # current customer 
                    arrival += 1
                    if space_server > 0:                     # there are still some empty spaces in the server, service directly 
                        c = Customer(i, next_arrival, mu, True)
                        system.append(c)
                        space_server -= 1
                    elif (num_wait < Q * s):                 # queue < Q * s
                        c = Customer(i, next_arrival, mu, False)
                        system.append(c)
                        num_wait += 1 
                    else:
                        block += 1

                block_prob += float(block / arrival)

            block_prob = float(block_prob / runs)
            print("    %10.4f | %.4f" % (float(lambd / mu), block_prob))

