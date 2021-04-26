import time
import re
import tester_dictionaries as td
import tester_functions as tf
import tester_csvhandler as csvh

#TODO: add python script to automate iperf run in command line

class csv_data:
    client_IP = ''
    client_port = ''
    server_IP = ''
    server_port = ''

    transfer_total = ''
    transfer_max = ''
    transfer_min = ''

    bandwidth_avg = ''
    bandwidth_max = ''
    bandwidth_min = ''

    date = ''
    time_start = ''
    time_end = ''
    time_elapsed = ''
    signal_dropped = ''

def main() -> None:
    end_data = False
    t_start = time.localtime() #timestamp of program start
    lines = [] #gets filled with each line of iperf output
    connection_established = False
    data = csv_data()

    #loop continues while data is being output by iperf, terminates when iperf output stops
    while True:
        program_input = input()

        if not connection_established and program_input.split(' ')[0] == '[':
            connection_established = True
            print('connected, writing to file...')
        else:
            print(program_input)

        #empty line signals stop
        if program_input.strip() == '':
            if not end_data:
                end_data = True  
            else: 
                break

        lines.append(program_input)

    print('connection terminated')
    t_end = time.localtime()
    interval = []
    transfer = []
    bandwidth = []
    data.signal_dropped = False

    intervalRegex = re.compile(r'([0-9.]+-[0-9.]+)', re.VERBOSE)
    IPRegex = re.compile(r'\d\d\d\.\d\d\d\.\d\.[0-9]+', re.VERBOSE)
    dataRegex = re.compile(r'\d*\.\d+|\d+', re.VERBOSE)

    #Uses regex to organize iperf raw output to variables
    for i in lines:
        #signifies header
        if 'local' in i:
            data.client_IP, data.server_IP = IPRegex.findall(i)
            data.client_port = dataRegex.findall(i)[4]
            data.server_port = dataRegex.findall(i)[-1]

        #signifies end information
        elif 'sender' in i:
            data.transfer_total = float(dataRegex.findall(i)[-2]) * tf.unitSize(i, td.transferUnits)
            data.bandwidth_avg = float(dataRegex.findall(i)[-1]) * tf.unitSize(i, td.bandwidthUnits)
        
        elif 'receiver' in i:
            if float(dataRegex.findall(i)[-2]) * tf.unitSize(i, td.transferUnits) != data.transfer_total or float(dataRegex.findall(i)[-1]) * tf.unitSize(i, td.bandwidthUnits) != data.bandwidth_avg:
                data.signal_dropped = True

        #signifies data
        elif 'sec' in i:
            interval.append(intervalRegex.findall(i)[0])
            transfer.append(float(dataRegex.findall(i)[-2]) * tf.unitSize(i, td.transferUnits))
            bandwidth.append(float(dataRegex.findall(i)[-1]) * tf.unitSize(i, td.bandwidthUnits))

    #Sorts transfer and bandwidth arrays
    transfer_sort = transfer
    tf.mergeSort(transfer_sort, 0, len(transfer)-1)
    bandwidth_sort = bandwidth
    tf.mergeSort(bandwidth_sort, 0, len(bandwidth)-1)

    if connection_established:
        data.transfer_total = tf.transferFormat(data.transfer_total)
        data.transfer_max = tf.transferFormat(transfer_sort[len(transfer_sort)-1])
        data.transfer_min = tf.transferFormat(transfer_sort[0])

        data.bandwidth_avg = tf.bandwidthFormat(data.bandwidth_avg)
        data.bandwidth_max = tf.bandwidthFormat(bandwidth_sort[-2])
        data.bandwidth_min = tf.bandwidthFormat(bandwidth_sort[0])

        data.date = time.strftime("%m-%d-%y", t_start)
        data.time_start = time.strftime("%H:%M:%S", t_start)
        data.time_end = time.strftime("%H:%M:%S", t_end)
        data.time_elapsed = interval[-1].split('-')[1] #TODO: use data from time module to determine elapsed time

        csv_filename = 'ThroughputTest_%s.csv' % time.strftime('%m-%d-%y_%H-%M-%S', t_start)
        csvh.csv_handler(data, csv_filename)
        print('Data written to file %s.' % csv_filename)

    else:
        print('No connection; data not written.')

if __name__ == '__main__':
    main()