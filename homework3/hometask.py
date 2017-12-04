import datetime
import time
import config
import psutil


def my_func(output_format, minutes):
    my_file = open("output."+output_format, 'w')
    iterator = 1
    try:
        while True:
            cpu = psutil.cpu_percent(interval=1, percpu=True)
            cpu_str = ""
            for i in range(len(cpu)):
                cpu_str += " Core "+str(i+1)+": "+str(cpu[i])+"; "
            mem = psutil.virtual_memory()
            mem_usage = mem[2]
            mem_str = "Memory usage, %: "+str(mem_usage)+"; "
            disk = psutil.disk_io_counters()
            disk_str = "Disk read, MBytes: "+str(disk[2]/(1024**2))+"; Disk write, MBytes: "+str(disk[3]/(1024**2))+"; "
            net = psutil.net_io_counters()
            net_str = "Net packets sent: "+str(net[2])+"; Net packets received: "+str(net[3])+";"
            result = cpu_str+mem_str+disk_str+net_str
            timestamp = datetime.datetime.now().ctime()
            res_str = "SNAPSHOT "+str(iterator)+": "+str(timestamp)+": "+result
            my_file.write(res_str+"\n")
            time.sleep(60*minutes)
            iterator += 1
    except KeyboardInterrupt:
        print "Process has been stopped by User"
    my_file.close()
    return iterator


COUNT = my_func(config.OUTPUT, config.INTERVAL)
print str(COUNT)+" snapshot(s) have been captured"




