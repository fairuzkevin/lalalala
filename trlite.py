import pexpect as pe
import os
import time

i = 0
count = 3

#test_1   = "ab -n "
test_10  = "ab -r -c 500 -t 20s -n 200000 -H 'Accept: application/json' -H 'X-Authorization: bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ0ZW5hbnQxQHRoaW5nc2JvYXJkLm9yZyIsInNjb3BlcyI6WyJURU5BTlRfQURNSU4iXSwidXNlcklkIjoiOTdlZDhlYzAtMDc3Zi0xMWU5LWI4NDgtMGY4NzU2NjM4ZWE1IiwiZW5hYmxlZCI6dHJ1ZSwiaXNQdWJsaWMiOmZhbHNlLCJ0ZW5hbnRJZCI6IjhkMTA3ZGEwLTA3N2YtMTFlOS1iODQ4LTBmODc1NjYzOGVhNSIsImN1c3RvbWVySWQiOiIxMzgxNDAwMC0xZGQyLTExYjItODA4MC04MDgwODA4MDgwODAiLCJpc3MiOiJ0aGluZ3Nib2FyZC5pbyIsImlhdCI6MTU0NTg3ODIzNiwiZXhwIjoxNTQ2MTM3NDM2fQ.1Fj4P0K62yg3T6UZDiVTqnx246zGo4cdyX96ZpeNFse7hIWg5bNsWTnWm4ZjRs1DI5XyxxJtE5MUyvmb3aW4wg' http://35.247.130.210:8080/api/plugins/telemetry/DEVICE/521e3f50-07e5-11e9-848f-ab4155fe34aa/values/timeseries?keys=temperature"
for i in range (count):

	if i == 0:
		  print "Be ready!"
		  print "web testing about to begin!!!"
		  pass


	if i == 1:
		  j=0
		  print "Testing 500 user"
		  fout = open("terserah2.txt","wb")
		  read_count = 30
		  for j in range(read_count):
		  	    ex = pe.spawn(test_10)
		  	    ex.logfile = fout
		  	    ex.expect(pe.EOF, timeout=None)
		  	    print "test = %d" %j
                            print "resting for 10 seconds"
                            time.sleep(10) #break for 5 minutes
		  print "test 1 selesai"
		  pass
		 
	if i == 2:
		print "sukses"
