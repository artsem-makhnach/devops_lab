import datetime
import time
import config
import psutil


class Mem(object):
    def collect_mem(self):
        mem = psutil.virtual_memory()
        mem_usage = mem[2]
        mem_str = "Memory usage, %: " + str(mem_usage) + "; "
        return mem_str


class Cpu(object):
    def collect_cpu(self):
        cpu = psutil.cpu_percent(interval=1, percpu=True)
        cpu_str = ""
        for i in range(len(cpu)):
            cpu_str += " Core " + str(i + 1) + ": " + str(cpu[i]) + "; "
        return cpu_str


class Disk(object):
    def collect_disk(self):
        disk = psutil.disk_io_counters()
        disk_str = "Disk read, MBytes: "+str(disk[2]/(1024**2))+"; Disk write, MBytes: "+str(disk[3]/(1024**2))+"; "
        return disk_str


class Net(object):
    def collect_net(self):
        net = psutil.net_io_counters()
        net_str = "Net packets sent: " + str(net[2]) + "; Net packets received: " + str(net[3]) + ";"
        return net_str


class Monitoring(Mem, Cpu, Disk, Net):

    def __init__(self, output_format, minutes):
        self.output_format = output_format
        self.minutes = minutes

    def main(self):
        my_file = open("output." + self.output_format, 'w')
        iterator = 1
        try:
            while True:
                result = super(Monitoring, self).collect_cpu() + super(Monitoring, self).collect_mem() + super(Monitoring, self).collect_disk() + super(Monitoring, self).collect_net()
                timestamp = datetime.datetime.now().ctime()
                res_str = "SNAPSHOT " + str(iterator) + ": " + str(timestamp) + ": " + result
                my_file.write(res_str + "\n")
                # time.sleep(10)
                time.sleep(60 * self.minutes)
                iterator += 1
        except KeyboardInterrupt:
            print "Process has been stopped by User"
            print str(iterator) + " snapshot(s) have been captured"
        my_file.close()


MONITOR = Monitoring(config.OUTPUT, config.INTERVAL)
MONITOR.main()
