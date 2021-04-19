#throughput tester
#aggregates information about current network connection into an insightful summary using iperf3

import time
import csv
import re
import tester_dictionaries as td
import tester_functions as tf
    
def main() -> None:

    end_data = False
    t_start = time.localtime() #timestamp of program start
    lines = [] #gets filled with each line of iperf output
    
    connection_established = False

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

    #TODO: find a way to input frequency

    interval = []
    transfer = []
    bandwidth = []

    signal_dropped = False

    #all variables used in for loop are declared empty to allow data to be written to csv file
    #if an if statement in does not get triggered
    client_IP = server_IP = client_port = server_port = transfer_total = bandwidth_avg = ''

    intervalRegex = re.compile(r'([0-9.]+-[0-9.]+)', re.VERBOSE)
    IPRegex = re.compile(r'\d\d\d\.\d\d\d\.\d\.[0-9]+', re.VERBOSE)
    dataRegex = re.compile(r'\d*\.\d+|\d+', re.VERBOSE)

    #Uses regex to organize iperf raw output to variables
    for i in lines:

        #signifies header
        if 'local' in i:
            client_IP, server_IP = IPRegex.findall(i)
            client_port = dataRegex.findall(i)[4]
            server_port = dataRegex.findall(i)[-1]

        #signifies end information
        elif 'sender' in i:
            transfer_total = float(dataRegex.findall(i)[-2]) * tf.unitSize(i, td.transferUnits)
            bandwidth_avg = float(dataRegex.findall(i)[-1]) * tf.unitSize(i, td.bandwidthUnits)
        
        elif 'receiver' in i:
            if float(dataRegex.findall(i)[-2]) * tf.unitSize(i, td.transferUnits) != transfer_total or float(dataRegex.findall(i)[-1]) * tf.unitSize(i, td.bandwidthUnits) != bandwidth_avg:
                signal_dropped = True

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

    #csv header
    fieldnames = ['Trial', 'Title', 'Data']

    #csv data
    #TODO: Figure out how to add sequential trial numbers
    #TODO: Format
    if connection_established:
        rows = [
            {'Trial': ''},

            {'Trial': '1',
            'Title': 'Client IP',
            'Data': client_IP},

            {'Title': 'Client Port No.',
            'Data': client_port},

            {'Title': 'Server IP',
            'Data': server_IP},

            {'Title': 'Server Port No.',
            'Data': server_port},

            #{'Title': 'Frequency',
            #'Data': ''},

            #{'Title': 'Protocol',
            #'Data': ''},

            #{'Title': 'Buffer Length',
            #'Data': ''},

            {'Title': 'Total transfer size',
            'Data': tf.transferFormat(transfer_total)},

            {'Title': 'Max transfer size',
            'Data': tf.transferFormat(transfer_sort[len(transfer_sort)-1])},

            {'Title': 'Min transfer size',
            'Data': tf.transferFormat(transfer_sort[0])},

            {'Title': 'Avg Bandwidth',
            'Data': tf.bandwidthFormat(bandwidth_avg)},

            {'Title': 'Max Bandwidth',
            'Data': tf.bandwidthFormat(bandwidth_sort[-2])},

            {'Title': 'Min Bandwidth',
            'Data': tf.bandwidthFormat(bandwidth_sort[0])},

            {'Title': 'Date',
            'Data': time.strftime("%m-%d-%y", t_start)},

            {'Title': 'Start Time',
            'Data': time.strftime("%H:%M:%S", t_start)},

            {'Title': 'End Time',
            'Data': time.strftime("%H:%M:%S", t_end)},

            {'Title': 'Time Elapsed',
            'Data': interval[-1].split('-')[1]}, #TODO: use data from time module to determine elapsed time

            {'Title': 'Signal Dropped',
            'Data': signal_dropped},

            #{'Title': 'Interruptions',
            #'Data': ''},

            #{'Title': 'Raw data',
            #'Data': ''}
        ]

    '''
    Buffer Length: Duration (in seconds) between pings
    Avg Bandwidth: add whether this number is above or below avg
    Interruptions: periods with low bandwidth, add timestamps using interval[]
    Raw data:      play around with formatting

    TODO: System info of server and client
    TODO: Graph
    '''


    #writing to csv file
    with open('ThroughputTest_%s.csv' % time.strftime('%m-%d-%y_%H-%M-%S', t_start), 'w', encoding='UTF8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    if connection_established:
        print('Data written to file %s.' % f.name)
    else:
        print('No connection; data not written.')

if __name__ == '__main__':
    main()