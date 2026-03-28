import numpy as np

def calculate(list):

    if len(list) == 9 :
        num_list = np.array(list).reshape(3,3)

        keys = {
            'mean': np.mean,
            'variance': np.var ,
            'standard deviation': np.std,
            'max': np.max,
            'min':np.min,
            'sum':np.sum
}


        calculations = {
            'mean': [],
            'variance': [],
            'standard deviation': [],
            'max': [],
            'min': [],
            'sum': []
}


        for proc,key in keys.items() :
            calculations[proc]=[key(num_list,axis=0).tolist(),key(num_list,axis=1).tolist() ,key(num_list).tolist()]


    else:
        raise ValueError("List must contain nine numbers.")


    return calculations