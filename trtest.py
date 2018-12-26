import pexpect as pe
import os
import time

i = 0
count = 11

#test_1   = "ab -n "
test_10  = "ab -r -c 500 -t 20s -n 200000 -H 'Accept: application/json' -H 'X-Authorization: bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ0ZW5hbnQxQHRoaW5nc2JvYXJkLm9yZyIsInNjb3BlcyI6WyJURU5BTlRfQURNSU4iXSwidXNlcklkIjoiODcyNTVmZDAtMDhlNC0xMWU5LWE3MzktMzc1MjU3NTdkYWE2IiwiZW5hYmxlZCI6dHJ1ZSwiaXNQdWJsaWMiOmZhbHNlLCJ0ZW5hbnRJZCI6IjdjNTIxMmIwLTA4ZTQtMTFlOS1hNzM5LTM3NTI1NzU3ZGFhNiIsImN1c3RvbWVySWQiOiIxMzgxNDAwMC0xZGQyLTExYjItODA4MC04MDgwODA4MDgwODAiLCJpc3MiOiJ0aGluZ3Nib2FyZC5pbyIsImlhdCI6MTU0NTgxNzU4MSwiZXhwIjoxNTQ2MDc2NzgxfQ.3LcOQBgcy0xp65kz9d4KoznCeL7Zj2QlWtNx5cKY2wgkOg1OleOLYzmY2jBMWKzges98cpLP6rsmv5KatKDIVA' http://35.197.129.117/api/plugins/telemetry/DEVICE/cb3059a0-08e4-11e9-a739-37525757daa6/values/attributes?keys=temperature"
test_100 = "ab -r -c 1000 -t 20s -n 200000 -H 'Accept: application/json' -H 'X-Authorization: bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ0ZW5hbnQxQHRoaW5nc2JvYXJkLm9yZyIsInNjb3BlcyI6WyJURU5BTlRfQURNSU4iXSwidXNlcklkIjoiODcyNTVmZDAtMDhlNC0xMWU5LWE3MzktMzc1MjU3NTdkYWE2IiwiZW5hYmxlZCI6dHJ1ZSwiaXNQdWJsaWMiOmZhbHNlLCJ0ZW5hbnRJZCI6IjdjNTIxMmIwLTA4ZTQtMTFlOS1hNzM5LTM3NTI1NzU3ZGFhNiIsImN1c3RvbWVySWQiOiIxMzgxNDAwMC0xZGQyLTExYjItODA4MC04MDgwODA4MDgwODAiLCJpc3MiOiJ0aGluZ3Nib2FyZC5pbyIsImlhdCI6MTU0NTgxNzU4MSwiZXhwIjoxNTQ2MDc2NzgxfQ.3LcOQBgcy0xp65kz9d4KoznCeL7Zj2QlWtNx5cKY2wgkOg1OleOLYzmY2jBMWKzges98cpLP6rsmv5KatKDIVA' http://35.197.129.117/api/plugins/telemetry/DEVICE/cb3059a0-08e4-11e9-a739-37525757daa6/values/attributes?keys=temperature"
test_120 = "ab -r -c 1500 -t 20s -n 200000 -H 'Accept: application/json' -H 'X-Authorization: bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ0ZW5hbnQxQHRoaW5nc2JvYXJkLm9yZyIsInNjb3BlcyI6WyJURU5BTlRfQURNSU4iXSwidXNlcklkIjoiODcyNTVmZDAtMDhlNC0xMWU5LWE3MzktMzc1MjU3NTdkYWE2IiwiZW5hYmxlZCI6dHJ1ZSwiaXNQdWJsaWMiOmZhbHNlLCJ0ZW5hbnRJZCI6IjdjNTIxMmIwLTA4ZTQtMTFlOS1hNzM5LTM3NTI1NzU3ZGFhNiIsImN1c3RvbWVySWQiOiIxMzgxNDAwMC0xZGQyLTExYjItODA4MC04MDgwODA4MDgwODAiLCJpc3MiOiJ0aGluZ3Nib2FyZC5pbyIsImlhdCI6MTU0NTgxNzU4MSwiZXhwIjoxNTQ2MDc2NzgxfQ.3LcOQBgcy0xp65kz9d4KoznCeL7Zj2QlWtNx5cKY2wgkOg1OleOLYzmY2jBMWKzges98cpLP6rsmv5KatKDIVA' http://35.197.129.117/api/plugins/telemetry/DEVICE/cb3059a0-08e4-11e9-a739-37525757daa6/values/attributes?keys=temperature"
test_250 = "ab -r -c 2000 -t 20s -n 200000 -H 'Accept: application/json' -H 'X-Authorization: bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ0ZW5hbnQxQHRoaW5nc2JvYXJkLm9yZyIsInNjb3BlcyI6WyJURU5BTlRfQURNSU4iXSwidXNlcklkIjoiODcyNTVmZDAtMDhlNC0xMWU5LWE3MzktMzc1MjU3NTdkYWE2IiwiZW5hYmxlZCI6dHJ1ZSwiaXNQdWJsaWMiOmZhbHNlLCJ0ZW5hbnRJZCI6IjdjNTIxMmIwLTA4ZTQtMTFlOS1hNzM5LTM3NTI1NzU3ZGFhNiIsImN1c3RvbWVySWQiOiIxMzgxNDAwMC0xZGQyLTExYjItODA4MC04MDgwODA4MDgwODAiLCJpc3MiOiJ0aGluZ3Nib2FyZC5pbyIsImlhdCI6MTU0NTgxNzU4MSwiZXhwIjoxNTQ2MDc2NzgxfQ.3LcOQBgcy0xp65kz9d4KoznCeL7Zj2QlWtNx5cKY2wgkOg1OleOLYzmY2jBMWKzges98cpLP6rsmv5KatKDIVA' http://35.197.129.117/api/plugins/telemetry/DEVICE/cb3059a0-08e4-11e9-a739-37525757daa6/values/attributes?keys=temperature"
test_500 = "ab -r -c 2500 -t 20s -n 200000 -H 'Accept: application/json' -H 'X-Authorization: bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ0ZW5hbnQxQHRoaW5nc2JvYXJkLm9yZyIsInNjb3BlcyI6WyJURU5BTlRfQURNSU4iXSwidXNlcklkIjoiODcyNTVmZDAtMDhlNC0xMWU5LWE3MzktMzc1MjU3NTdkYWE2IiwiZW5hYmxlZCI6dHJ1ZSwiaXNQdWJsaWMiOmZhbHNlLCJ0ZW5hbnRJZCI6IjdjNTIxMmIwLTA4ZTQtMTFlOS1hNzM5LTM3NTI1NzU3ZGFhNiIsImN1c3RvbWVySWQiOiIxMzgxNDAwMC0xZGQyLTExYjItODA4MC04MDgwODA4MDgwODAiLCJpc3MiOiJ0aGluZ3Nib2FyZC5pbyIsImlhdCI6MTU0NTgxNzU4MSwiZXhwIjoxNTQ2MDc2NzgxfQ.3LcOQBgcy0xp65kz9d4KoznCeL7Zj2QlWtNx5cKY2wgkOg1OleOLYzmY2jBMWKzges98cpLP6rsmv5KatKDIVA' http://35.197.129.117/api/plugins/telemetry/DEVICE/cb3059a0-08e4-11e9-a739-37525757daa6/values/attributes?keys=temperature"
test_550 = "ab -r -c 3000 -t 20s -n 200000 -H 'Accept: application/json' -H 'X-Authorization: bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ0ZW5hbnQxQHRoaW5nc2JvYXJkLm9yZyIsInNjb3BlcyI6WyJURU5BTlRfQURNSU4iXSwidXNlcklkIjoiODcyNTVmZDAtMDhlNC0xMWU5LWE3MzktMzc1MjU3NTdkYWE2IiwiZW5hYmxlZCI6dHJ1ZSwiaXNQdWJsaWMiOmZhbHNlLCJ0ZW5hbnRJZCI6IjdjNTIxMmIwLTA4ZTQtMTFlOS1hNzM5LTM3NTI1NzU3ZGFhNiIsImN1c3RvbWVySWQiOiIxMzgxNDAwMC0xZGQyLTExYjItODA4MC04MDgwODA4MDgwODAiLCJpc3MiOiJ0aGluZ3Nib2FyZC5pbyIsImlhdCI6MTU0NTgxNzU4MSwiZXhwIjoxNTQ2MDc2NzgxfQ.3LcOQBgcy0xp65kz9d4KoznCeL7Zj2QlWtNx5cKY2wgkOg1OleOLYzmY2jBMWKzges98cpLP6rsmv5KatKDIVA' http://35.197.129.117/api/plugins/telemetry/DEVICE/cb3059a0-08e4-11e9-a739-37525757daa6/values/attributes?keys=temperature"
test_600 = "ab -r -c 3500 -t 20s -n 200000 -H 'Accept: application/json' -H 'X-Authorization: bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ0ZW5hbnQxQHRoaW5nc2JvYXJkLm9yZyIsInNjb3BlcyI6WyJURU5BTlRfQURNSU4iXSwidXNlcklkIjoiODcyNTVmZDAtMDhlNC0xMWU5LWE3MzktMzc1MjU3NTdkYWE2IiwiZW5hYmxlZCI6dHJ1ZSwiaXNQdWJsaWMiOmZhbHNlLCJ0ZW5hbnRJZCI6IjdjNTIxMmIwLTA4ZTQtMTFlOS1hNzM5LTM3NTI1NzU3ZGFhNiIsImN1c3RvbWVySWQiOiIxMzgxNDAwMC0xZGQyLTExYjItODA4MC04MDgwODA4MDgwODAiLCJpc3MiOiJ0aGluZ3Nib2FyZC5pbyIsImlhdCI6MTU0NTgxNzU4MSwiZXhwIjoxNTQ2MDc2NzgxfQ.3LcOQBgcy0xp65kz9d4KoznCeL7Zj2QlWtNx5cKY2wgkOg1OleOLYzmY2jBMWKzges98cpLP6rsmv5KatKDIVA' http://35.197.129.117/api/plugins/telemetry/DEVICE/cb3059a0-08e4-11e9-a739-37525757daa6/values/attributes?keys=temperature"
test_650 = "ab -r -c 4000 -t 20s -n 200000 -H 'Accept: application/json' -H 'X-Authorization: bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ0ZW5hbnQxQHRoaW5nc2JvYXJkLm9yZyIsInNjb3BlcyI6WyJURU5BTlRfQURNSU4iXSwidXNlcklkIjoiODcyNTVmZDAtMDhlNC0xMWU5LWE3MzktMzc1MjU3NTdkYWE2IiwiZW5hYmxlZCI6dHJ1ZSwiaXNQdWJsaWMiOmZhbHNlLCJ0ZW5hbnRJZCI6IjdjNTIxMmIwLTA4ZTQtMTFlOS1hNzM5LTM3NTI1NzU3ZGFhNiIsImN1c3RvbWVySWQiOiIxMzgxNDAwMC0xZGQyLTExYjItODA4MC04MDgwODA4MDgwODAiLCJpc3MiOiJ0aGluZ3Nib2FyZC5pbyIsImlhdCI6MTU0NTgxNzU4MSwiZXhwIjoxNTQ2MDc2NzgxfQ.3LcOQBgcy0xp65kz9d4KoznCeL7Zj2QlWtNx5cKY2wgkOg1OleOLYzmY2jBMWKzges98cpLP6rsmv5KatKDIVA' http://35.197.129.117/api/plugins/telemetry/DEVICE/cb3059a0-08e4-11e9-a739-37525757daa6/values/attributes?keys=temperature"
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
		  print "test 1 selesai"
		  print "resting for 10 seconds"
		  time.sleep(10) #break for 5 minutes
		  pass

	if i == 2:
		  j=0
		  print "Testing 1000 user"
		  fout = open("terserah3.txt","wb")
		  read_count = 30
		  for j in range(read_count):
		  	    ex = pe.spawn(test_100)
		  	    ex.logfile = fout
		  	    ex.expect(pe.EOF, timeout=None)
		  	    print "test = %d" %j
		  print "test 1 selesai"
		  print "resting for 10 seconds"
		  time.sleep(10) #break for 5 minutes
		  pass

    if i == 3:
		  j=0
		  print "Testing 1500 user"
		  fout = open("terserah4.txt","wb")
		  read_count = 30
		  for j in range(read_count):
		  	    ex = pe.spawn(test_120)
		  	    ex.logfile = fout
		  	    ex.expect(pe.EOF, timeout=None)
		  	    print "test = %d" %j
		  print "test 1 selesai"
		  print "resting for 10 seconds"
		  time.sleep(10) #break for 5 minutes
		  pass

	if i == 4:
		  j=0
		  print "Testing 2000 user"
		  fout = open("terserah5.txt","wb")
		  read_count = 30
		  for j in range(read_count):
		  	    ex = pe.spawn(test_250)
		  	    ex.logfile = fout
		  	    ex.expect(pe.EOF, timeout=None)
		  	    print "test = %d" %j
		  print "test 1 selesai"
		  print "resting for 10 seconds"
		  time.sleep(10) #break for 5 minutes
		  pass

	if i == 5:
		  j=0
		  print "Testing 2500 user"
		  fout = open("terserah6.txt","wb")
		  read_count = 30
		  for j in range(read_count):
		  	    ex = pe.spawn(test_500)
		  	    ex.logfile = fout
		  	    ex.expect(pe.EOF, timeout=None)
		  	    print "test = %d" %j
		  print "test 1 selesai"
		  print "resting for 10 seconds"
		  time.sleep(10) #break for 5 minutes
		  pass

	if i == 6:
		  j=0
		  print "Testing 3000 user"
		  fout = open("terserah7.txt","wb")
		  read_count = 30
		  for j in range(read_count):
		  	    ex = pe.spawn(test_550)
		  	    ex.logfile = fout
		  	    ex.expect(pe.EOF, timeout=None)
		  	    print "test = %d" %j
		  print "test 1 selesai"
		  print "resting for 10 seconds"
		  time.sleep(10) #break for 5 minutes
		  pass


	if i == 7:
		  j=0
		  print "Testing 3500 user"
		  fout = open("terserah8.txt","wb")
		  read_count = 30
		  for j in range(read_count):
		  	    ex = pe.spawn(test_600)
		  	    ex.logfile = fout
		  	    ex.expect(pe.EOF, timeout=None)
		  	    print "test = %d" %j
		  print "test 1 selesai"
		  print "resting for 10 seconds"
		  time.sleep(10) #break for 5 minutes
		  pass

	if i == 8:
		  j=0
		  print "Testing 3500 user"
		  fout = open("terserah8.txt","wb")
		  read_count = 30
		  for j in range(read_count):
		  	    ex = pe.spawn(test_650)
		  	    ex.logfile = fout
		  	    ex.expect(pe.EOF, timeout=None)
		  	    print "test = %d" %j
		  print "test 1 selesai"
		  print "resting for 10 seconds"
		  time.sleep(10) #break for 5 minutes
		  pass

	if i == 9:
		print "sukses"



