import datetime
# import numpy as np
# import matplotlib.pyplot as plt

def predict_vm(ecs_lines, input_lines):
    # Do your work from here#
    result = []
    if ecs_lines is None:
        print 'ecs information is none'
        return result
    if input_lines is None:
        print 'input file information is none'
        return result

    ### Analysis ecs_lines ###################################
    flavor = [None]*len(ecs_lines)  # flavor type
    date = [None]*len(ecs_lines)    # apply date
    date_seq = []   # apply gap of date
    i = -1
    for line in ecs_lines:
        i += 1
        line = line.strip()
        odom = line.split()
        flavor[i] = int(filter(str.isdigit, odom[1]))

        date_demo = odom[2].split('-')
        date[i] = map(int,date_demo)

        d1 = datetime.datetime(date[0][0], date[0][1], date[0][2])
        d2 = datetime.datetime(date[i][0], date[i][1], date[i][2])
        days = (d2-d1).days
        date_seq.append(days)

    ### Analysis input_lines ###################################
    computer_type = []
    flavor_type = []
    flavor_type_number = []
    opt_dim = []
    time_span = []
    time_span_seq = []
    i = 0
    for line in input_lines:
        if line == '\n':
            i += 1
            continue
        if i == 0:
            demo = line.split()
            computer_type.append(map(int,demo))
        if i == 1:
            odom1 = line.split()
            flavor_demo = int(filter(str.isdigit, odom1[0]))
            flavor_type.append(flavor_demo)
        if i == 2:
            line = line.strip()
            opt_dim.append(line)
        if i == 3:
            odom = line.split()
            odom = odom[0].split('-')
            time_span.append(map(int,odom))  # attention about the date

    d1 = datetime.datetime(time_span[0][0], time_span[0][1], time_span[0][2])
    d2 = datetime.datetime(time_span[1][0], time_span[1][1], time_span[1][2])
    days = (d2 - d1).days
    time_span_seq.append(days)

    flavor_type_number.append(flavor_type[0])
    del flavor_type[0]

    ### Prediction Algorithm ##################################
    AR_P = 6    # AR model Order
    final_list = []




    ### picture ###############################################

    # date_x = [0]*(date_seq[-1]+1)
    # x_label = range(0, date_seq[-1]+1)
    # for i in date_seq:
    #     date_x[i] += 1
    #
    # plt.figure()
    # plt.plot(x_label, date_x)
    # plt.grid()
    # plt.show()

    ### result ###############################################
    result.append(flavor_type_number[0])
    for line in flavor_type:
        result.append('flavor'+str(line)+' '+str(1))
    result.append('')
    result.append(flavor_type_number[0])
    for i in range(1, flavor_type_number[0]+1, 1):
        result.append(str(i)+' '+'flavor'+str(flavor_type[i-1])+' '+str(1))


    return result
