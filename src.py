import random 
import copy 

def poisson(rate):
    return random.expovariate(rate)

class Customer:
    def __init__(self, id, arrival_time, mu, status):
        self.id = id 
        self.arrival_time = arrival_time
        self.service_time = poisson(mu)         
        self.status = status            # 0: init, 1: service, 2: finish

Q = 0 
S = [1, 5, 10]
lambds = [0.01, 0.1, 1, 10]
mus = [0.01, 0.04, 0.16, 0.64, 2.56, 10.24]
runs, N = 10, 100000

for s in S:
    print('\n(S = %d) Erlang | block prob' %(s))
    print('-------------------------------')

    for lambd in lambds:
        for mu in mus:
            block_prob = 0                                  # blocking prob  
            for run in range(runs):
                
                system, table = [], []                      # initialize  
                capacity, num_wait = s, 0
                arrival, block = 0, 0  
                system_time = 0;   

                for i in range(0, N):

                    # generate the customer 
                    customer = Customer(arrival, poisson(lambd), mu, 0)
                    arrival += 1

                    if (capacity == 0):                      # no space -> block
                        block += 1
                    else:
                        if ((capacity - num_wait) > 0):
                            customer.status = 1             # start servicing
                            capacity -= 1 
                        else:
                            customer.status = 0 
                            num_wait += 1
                            capacity -= 1
                        system.append(customer)

                    # next 
                    next_arrival = poisson(lambd)
                    system_time += next_arrival
                    depart = 0 
                    system_cp = copy.copy(system)

                    # check the customers in the system 
                    for customer in system:
                        if customer.status == True:
                            t = customer.service_time - next_arrival
                            if t <= 0:
                                customer.status = 2             # finish 
                                capacity += 1
                                depart += 1 
                                table.append(-t) 
                                system_cp.remove(customer)
                            else:
                                customer.service_time = t       # still service 

                        # queue -> system 
                        else:
                            if depart > 0:    
                                num_wait -= 1                 
                                depart -= 1
                                customer.status = 1 
                                customer.service_time -= table[0]; 
                                if (customer.service_time <= 0):
                                    customer.status = 2         # finish 
                                    depart += 1
                                    capacity += 1
                                    table.remove(table[0])
                                    table.append(-customer.service_time)
                                    system_cp.remove(customer)
                                else:
                                    table.remove(table[0])
                            else:
                                break 

                    system = system_cp                          # update the system 
                    table = []

                block_prob += float(block / arrival)
            block_prob = float(block_prob / runs)
            print("    %10.4f | %.4f" % (float(lambd / mu), block_prob))

