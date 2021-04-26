import csv

def csv_handler(data, filename):
    fieldnames = ['Trial', 'Title', 'Data']

    rows = [
        {'Trial': ''},

        {'Trial': '1',
        'Title': 'Client IP',
        'Data': data.client_IP},

        {'Title': 'Client Port No.',
        'Data': data.client_port},

        {'Title': 'Server IP',
        'Data': data.server_IP},

        {'Title': 'Server Port No.',
        'Data': data.server_port},

        {'Title': 'Total transfer size',
        'Data': data.transfer_total},

        {'Title': 'Max transfer size',
        'Data': data.transfer_max},

        {'Title': 'Min transfer size',
        'Data': data.transfer_min},

        {'Title': 'Avg Bandwidth',
        'Data': data.bandwidth_avg},

        {'Title': 'Max Bandwidth',
        'Data': data.bandwidth_max},

        {'Title': 'Min Bandwidth',
        'Data': data.bandwidth_min},

        {'Title': 'Date',
        'Data': data.date},

        {'Title': 'Start Time',
        'Data': data.time_start},

        {'Title': 'End Time',
        'Data': data.time_end},

        {'Title': 'Time Elapsed',
        'Data': data.time_elapsed},

        {'Title': 'Signal Dropped',
        'Data': data.signal_dropped},
    ]

    '''
    TODO:
    Buffer Length: Duration (in seconds) between pings
    Avg Bandwidth: add whether this number is above or below avg
    Interruptions: periods with low bandwidth, add timestamps using interval[]
    Raw data:      play around with formatting

    TODO: Figure out how to add sequential trial numbers
    TODO: System info of server and client
    TODO: Format CSV better
    TODO: Graph
    '''

    #writing to csv file
    #TODO: when creating csv files, save to specified folder and tell user where file is saved
    with open(filename, 'w', encoding='UTF8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)