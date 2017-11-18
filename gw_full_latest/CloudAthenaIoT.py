#-------------------------------------------------------------------------------
# Copyright 2017 Ed McLain - Digital Motion LLC
# 
# emclain@digitalmotion.tech
#
# This file is part of the low-cost LoRa gateway developped at University of Pau
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with the program.  If not, see <http://www.gnu.org/licenses/>.
#-------------------------------------------------------------------------------

import os
import sys
import json
import time
import key_AthenaIoT

try:
    key_AthenaIoT.source_list
except AttributeError:
    key_AthenaIoT.source_list = []

#------------------------------------------------------------
#store internet pending data
#------------------------------------------------------------

def saveToAthena(sensor, metrics):
    try:
        data = {}
        data['type'] = 'metric'
        data['id'] = sensor
        data['metrics'] = metrics
        data['timestamp'] = time.time()
        fname = "{}/input/lorawan-{}.json".format(key_AthenaIoT.athenaDataDir, data['timestamp'])
        with open(fname, 'w') as json_file:
            json.dump(data, json_file)
    except IOError as e:
        print "Unable to open file: {}".format(e)

#------------------------------------------------------------
# main
#------------------------------------------------------------

def main(ldata, pdata, rdata, tdata, gwid):
    
    # Parse packet data into its pieces
    arr = map(int,pdata.split(','))
    dst=arr[0]
    ptype=arr[1]
    src=arr[2]
    seq=arr[3]
    datalen=arr[4]
    SNR=arr[5]
    RSSI=arr[6]
    
    if (str(src) in key_AthenaIoT.source_list) or (len(key_AthenaIoT.source_list) == 0):
        inboundMetrics = ldata.split("#")
        outboundMetrics = {}
        for metric in inboundMetrics:
            if metric != '':
                newMetric = metric.split(':')
                if len(newMetric) > 1:
                    print "newMetric: {} / Val: {}".format(newMetric[0], newMetric[1])
                    outboundMetrics[newMetric[0]] = newMetric[1]
                else
                    print "Bad Metric: {}".format(newMetric)
        outboundMetrics['rssi'] = RSSI
        outboundMetrics['snr'] = SNR
        saveToAthena(src, outboundMetrics)
    else:
        print "Source is not is source list, no processing with CloudNoInternet.py"

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
