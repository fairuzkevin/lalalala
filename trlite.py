import pexpect as pe
import os
import time

i = 0
count = 3

#test_1   = "ab -n "
test_10  = "ab -r -c 500 -t 20s -n 200000 -H 'Accept: application/json' -H 'X-Authorization: bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ0ZW5hbnQxQHRoaW5nc2JvYXJkLm9yZyIsInNjb3BlcyI6WyJURU5BTlRfQURNSU4iXSwidXNlcklkIjoiODcyNTVmZDAtMDhlNC0xMWU5LWE3MzktMzc1MjU3NTdkYWE2IiwiZW5hYmxlZCI6dHJ1ZSwiaXNQdWJsaWMiOmZhbHNlLCJ0ZW5hbnRJZCI6IjdjNTIxMmIwLTA4ZTQtMTFlOS1hNzM5LTM3NTI1NzU3ZGFhNiIsImN1c3RvbWVySWQiOiIxMzgxNDAwMC0xZGQyLTExYjItODA4MC04MDgwODA4MDgwODAiLCJpc3MiOiJ0aGluZ3Nib2FyZC5pbyIsImlhdCI6MTU0NTgxNzU4MSwiZXhwIjoxNTQ2MDc2NzgxfQ.3LcOQBgcy0xp65kz9d4KoznCeL7Zj2QlWtNx5cKY2wgkOg1OleOLYzmY2jBMWKzges98cpLP6rsmv5KatKDIVA' http://35.197.129.117/api/plugins/telemetry/DEVICE/cb3059a0-08e4-11e9-a739-37525757daa6/values/attributes?keys=temperature"
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
