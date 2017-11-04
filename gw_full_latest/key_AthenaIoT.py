#
# AtheanIoT Config
#
# source_list : Emtpy = accept all sources, else array of source's to resrict metric collection to
# athenaDataDir : Location of AthenaIoT data_dir.
#  
source_list=[]
athenaDataDir = "config"

if athenaDataDir == "config":
    from subprocess import call
    ret = call(["athena-config", "get", "athena.data_dir"], stdout=athenaDataDir)
    if ret != 0:
        print "ERROR: Failed retreiving AthenaIoT Data Dir"
        exit(1)
