#!/usr/bin/env python3
# pylint: disable=no-value-for-parameter

# import click
from jumpscale.loader import j
# import stellar_sdk
import os
# from  jumpscale.clients.stellar.exceptions import UnAuthorized

class get_input():
    def __init__(self):
	    self.zdb_number=input('Number of ZDB\'s :')
	    self.zdb_password = input('ZDB password :')
	    self.zdb_size = input('ZDB size :')
	    self.zdb_mode = input('ZDB mode :')
    
    def calculate_something(size):
        self.zdb_size_gb = size * 1024
        print('In method: ',self.zdb_size_gb)

def select_working_pool(my_pools):
    
    # local temp store
    tmp_cus=0
    tmp_sus=0

    # select the largest pool information to pay-as-you-go for the reservation
    for pool in my_pools:
        if pool.cus >= tmp_cus or pool.sus >= tmp_sus:
            if pool.cus != 0 and pool.sus != 0:
                pool_id=pool.pool_id
            else:
                print('Cannot use pool_id:', pool_id,' One of the required capacity units is empty')
        tmp_cus=pool.cus
        tmp_sus=pool.sus 
    print('Selected pool to deploy ZDB\'s:', pool_id)
    
    return(pool_id)

def deploy_zdbs(pool_id, zdb_password, zdb_size, zdb_mode, debug_on):

    # get all the data for the selected capacity pool
    my_pool=zos.pools.get(pool_id)
    # for each node in the pool 
    for node in my_pool.node_ids:
        zdb_deploy=zos.zdb.create(node_id=node, \
            pool_id=my_pool.pool_id, \
            password=zdb_password, \
            disk_type='HDD', \
            size=zdb_size, \
            public='TRUE', \
            mode=zdb_mode)
        if debug_on == 1:
            print(zdb_deploy)
            input('Data formatted for deployment.....')
        id=zos.workloads.deploy(zdb_deploy) 
        result_workload = zos.workloads.get(id) 
        if debug_on == 1:
            input('Workload result:')
            print(result_workload)
            input('Decomission workload?')
        zos.workloads.decomission(id)

def main():

    # load the SAL to make/break reservation
    zos=j.sals.zos.get() 
	
    # run rhw program
    my_pools=zos.pools.list()
    select_working_pool(my_pools)
    new=get_input()

    print('Number: ',new.zdb_number)
    print('Password: ',new.zdb_password)
    print('Size: ',new.zdb_size)
    print('Size (DB):',new.calculate_something(new.zdb_size))
    print('Mode :',new.zdb_mode)

	#pool_id=select_working_pool(my_pools)
	# deploy_zdbs

	# select capacity pool for deployment
    #hello

if __name__ == '__main__':
    main()



# refresh the infromaiton in the pool and print it.
#ipool=zos.pools.get(18714)
#print(pool.active_su)

#zos.workloads.decomission(33312)  

#pool=zos.pools.get(18714)
#pool.active_workload_ids
#[32617, 32621, 32620, 33267, 33269, 33268, 33275, 33278, 33276, 33277, 33281]
