import math

def gaussian_function(x, std):
    ret_val = 1.0
    ret_val /= math.sqrt(2 * 3.14159 * std * std)
    ret_val *= math.exp( -1 * (x) * (x) / (2 * std * std))
    # return ( 1.0 / math.sqrt(2 * 3.14159 * std * std)) * math.exp( -1 * (x) * (x) / (2 * std * std))
    return ret_val

def blur(s):

    # print "Working set: "
    # print s

    std_dev = len(s) / 4.0
    offset = int(math.floor(len(s) / 2))
    # get mean 
    mean = 0
    for element in s:
        mean += element
    mean /= len(s)

    # The guassian blur weighting method doesn't fully add up to 100%, so 
    #  prepare to scale the final value in order to make it more accurate
    scaler = 0
    for i in range(-1 * offset, offset + 1):
        scaler += gaussian_function(i, std_dev)
    scaler = 1.0 / scaler

    gaussian_average = 0
    for i in range(-1 * offset, offset + 1):
        weight = gaussian_function(i, std_dev)
        gaussian_average += weight * s[i + offset]
        # print "Value %f has weight %f" % (s[i + offset], weight)

    # print "Smoothed set to single value: ",
    # print gaussian_average
    return gaussian_average * scaler

def smooth_set(s, r):
    print "Smoothing set of length %s" % len(s) 
    # r must be 
    if r % 2 == 0:
        r += 1
    std_dev = math.ceil(r / 4)
    smoothed_set = []
    offset = int(math.floor(r/2))

    #Add zeros to the top of the list
    for i in range(0, offset):
        smoothed_set.append(0)

    #Smooth every point along the data set
    for i in range(offset, len(s) - offset):
        data_point_set = []
        # Populate the set to get the point average
        for j in range(-1 * offset, offset + 1):
            data_point_set.append(s[j+i])
        #Blur the set into a single value
        smoothed_set.append(blur(data_point_set))

    #Add zeros to the bottom of the list
    for i in range(0, offset):
        smoothed_set.append(0)
    
    print "Smoothed set is length %s" % len(smoothed_set) 
    return smoothed_set

if __name__ == '__main__':
    test_set = [
        1.414169373,
        2.291647854,
        3.462278959,
        4.245235636,
        4.801282788,
        6.485003300,
        6.962123873,
        8.478276601,
        9.209819986,
        9.625263723
    ]

    a = smooth_set(test_set,3)
    print a
    
