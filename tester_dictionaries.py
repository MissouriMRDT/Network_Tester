#transfer unit size to its size relative to a byte
transferUnits = {
    "KBytes" : 1000,
    "MBytes" : 1000000,
    "GBytes" : 1000000000,
    "TBytes" : 1000000000000,
    "Bytes" : 1
}

#bandwidth unit size to its size relative to a bit
bandwidthUnits = {
    "Kbits" : 1000,
    "Mbits" : 1000000,
    "Gbits" : 1000000000,
    "Tbits" : 1000000000000,
    "bits" : 1,
}

#pairs number of digits in a transfer value to its relevant unit
transferLenToUnit = {
    1 : " bits/sec",
    2 : " bits/sec",
    3 : " bits/sec",
    4 : " Kbits/sec",
    5 : " Kbits/sec",
    6 : " Kbits/sec",
    7 : " Mbits/sec",
    8 : " Mbits/sec",
    9 : " Mbits/sec",
    10 : " Gbits/sec",
    11 : " Gbits/sec",
    12 : " Gbits/sec",
    13 : " Tbits/sec",
    14 : " Tbits/sec",
    15 : " Tbits/sec"
}

#pairs number of digits in a bandwidth value to its relevant unit
bandwidthLenToUnit = {
    1 : " Bytes",
    2 : " Bytes",
    3 : " Bytes",
    4 : " KBytes",
    5 : " KBytes",
    6 : " KBytes",
    7 : " MBytes",
    8 : " MBytes",
    9 : " MBytes",
    10 : " GBytes",
    11 : " GBytes",
    12 : " GBytes",
    13 : " TBytes",
    14 : " TBytes",
    15 : " TBytes"
}