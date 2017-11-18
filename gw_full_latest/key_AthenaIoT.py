#
# AtheanIoT Config
#
# source_list : Emtpy = accept all sources, else array of source's to resrict metric collection to
# athenaDataDir : Location of AthenaIoT data_dir.
#  
source_list=[]
athenaDataDir = "config"

if athenaDataDir == "config":
    from subprocess import check_output
    athenaDataDir = check_output(["athena-config", "get", "athena.data_dir"]).rstrip("\n")
    if athenaDataDir == "nil":
        print "ERROR: Failed retreiving AthenaIoT Data Dir"
        exit(1)
