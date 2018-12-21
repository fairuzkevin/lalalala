import psutil as ps
import json, time, urllib2, os
from datetime import timedelta as td
from apscheduler.schedulers.background import BackgroundScheduler

INSTANCE_ID = "d81f8227-8058-4721-b97d-71c7ca1d0753"
MONITORING_IP = "192.168.1.13"
MONITORING_PORT = "3000"
MONITORING_API = "/api/recv/"

class Resources(): 
 def get_cpu(self):
  return ps.cpu_percent(percpu=True, interval=1)

 def get_ram(self):
  ram = ps.virtual_memory()
  return {
   'total' : ram.total,
   'used' : ram.used, 
   'free' : ram.free, 
   'cached' : ram.cached, 
   'buffer' : ram.buffers
  }

 def _disk_usage(self, mount):
  usage = ps.disk_usage(mount)
  return {
   'total' : usage.total, 
   'used' : usage.used
  }
 
 def _disk_io(self):
  disks = {}
  for disk, iocount in ps.disk_io_counters(perdisk=True).iteritems():
   disks[disk] = {
       'count': {
        'r' : iocount.read_count,
        'w' : iocount.write_count
       },
       'bytes': {
        'r' : iocount.read_bytes,
        'w' : iocount.write_bytes
       }
        }

  return disks

 def get_disk(self):
  disks = {}
  disk_io = self._disk_io()

  for disk in ps.disk_partitions():
   dev_name = disk.device.split('/')[2]

   disks[dev_name] = disk_io[dev_name]
   disks[dev_name]['usage'] = self._disk_usage(disk.mountpoint)

  return disks

 def get_net_io(self):
  net = ps.net_io_counters()

  return {
   'in' : {
    'bytes' : net.bytes_recv,
    'pkt' : net.packets_recv,
    'err' : net.errin,
    'drop' : net.dropin
   },
   'out' : {
    'bytes' : net.bytes_sent,
    'pkt' : net.packets_sent,
    'err' : net.errout,
    'drop' : net.dropout
   }
  }

 def _conn_per_kind(self, kind):
  return len(ps.net_connections(kind=kind))

 def get_net_conn(self, ):
  tcp4 = self._conn_per_kind('tcp4')
  udp4 = self._conn_per_kind('udp4')

  tcp6 = self._conn_per_kind('tcp6')
  udp6 = self._conn_per_kind('udp6')

  return {
   'ipv4' : {
    'tcp' : tcp4, #tcp connections using ipv4
    'udp' : udp4, #udp connections using ipv4
   },
   'ipv6' : {
    'tcp' : tcp6, #tcp connections using ipv6
    'udp' : udp6, #udp connections using ipv6
   }
  }

 def _host_info(self):
  boot = ps.boot_time()
  uptime = time.time() - boot
  return {
   # 'uptime' : str(td(seconds=uptime))
   'uptime' : uptime
  }

 def get_stats(self):
  disks1 = self.get_disk()
  net_io1 = self.get_net_io()

  cpu = self.get_cpu()
  time.sleep(1)

  disks = self.get_disk()
  net_io = self.get_net_io()

  for disk in disks:
   read_rate = disks[disk]['bytes']['r'] - disks1[disk]['bytes']['r']
   write_rate = disks[disk]['bytes']['w'] - disks1[disk]['bytes']['w']

   disks[disk]['rates'] = {
         'r' : read_rate, 
         'w' : write_rate
           }

  net_conn = self.get_net_conn()

  for in_out in net_io:
   net_io[in_out]['b_rate'] = net_io[in_out]['bytes'] - net_io1[in_out]['bytes']
   net_io[in_out]['pkt_rate'] = net_io[in_out]['pkt'] - net_io1[in_out]['pkt']
   
  net = net_io
  net['conn'] = net_conn

  ram = self.get_ram()

  host = self._host_info()
  
  resr = {
    'cpu'  : cpu,
    'disk' : disks,
    'ram'  : ram,
    'network' : net,
    }

  stats = dict(host.items() + resr.items())

  return json.dumps(stats)#, sort_keys=True, indent=4)  

class SenderAgent():
 def send_stat(self):
  res = Resources()
  stats = res.get_stats()

  url = "http://"+MONITORING_IP+":"+MONITORING_PORT+MONITORING_API
  
  #req = urllib2.Request(url) #Request
  #req.add_header('Content-Type', 'application/json')
  #req.add_header('instanceid', INSTANCE_ID)
  
  #res = urllib2.urlopen(req, stats)
  #print time.strftime("[%Y-%m-%d %H:%M:%S] Sending stats : ")+res.read()
  print(stats)

 def start(self):
  #print stats
  #self.send_stat(stats)
  #"""
  scheduler = BackgroundScheduler()
  scheduler.add_job(
   self.send_stat, 
   trigger='cron', 
   minute="*/1", 
   id="Send_Stats"
   )
  scheduler.start()
  print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

  try:
   while True:
    time.sleep(2)
  except (KeyboardInterrupt, SystemExit):
   scheduler.shutdown()
  #"""

if __name__ == '__main__':
 agent = SenderAgent()
 agent.start()