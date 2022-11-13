'''
You are tasked to find cloud resource usage hours from logs emitted by cloud resources.

The cloud resource's send event everytime a cloud resource is created
e.g. say compute.create.start, compute.create.end. Once the resource
is created the resource sends an hourly heartbeat message saying that the compute resource exists
i.e compute.exists.

The heartbeat message may be received anytime in the hour as long as we get
the hourly heart beat we can include that entire hour (clock hour) in our usage.
Say we get a compute.create.start event at 01:15:00 we can include the entire hour from 01:00:00
to 2:00:00 in hour usage calculation. If we get a exists event at 02:15:00 we can include
the entire hour from 02:00:00 to 03:00:00 in your usage calculation

Here is a sample log for a resource myvm001 that was created on 2020-08-01T00:15:00
and deleted on 2020-08-01T03:18:02.

tenant_id,timestamp,resource_id,resource_type,resource_name,resource_quantity,event_type
98112, 2020-08-01T00:15:00, 7001, compute, myvm001,XL, compute.create.start
98112,2020-08-01T00:18:00,7001,compute,myvm001,XL,compute.create.end
98112,2020-08-01T01:15:01,7001,compute,myvm001,XL,compute.exists
98112,2020-08-01T02:15:00,7001,compute,myvm001,XL,compute.exists
98112,2020-08-01T03:15:00,7001,compute,myvm001,XL,compute.delete.start
98112,2020-08-01T03:18:02,7001,compute,myvm001,XL,compute.delete.end

The result from your program should be usage hours

tenant_id,resource_id,resource_type,resource_name,resource_quantity,usage_hours
98112,70001,compute,myvm001,XL,4	

class Tenant:
	def __init__(self, time, to_charge, hours):
  	self.time = time
    self.to_charge = to_charge
    self.total_hours = hours

def calculateHoursForCharge(lst):
	mappedList = []
  counter = {} # dict[resource, Tenant]
  for i in range(lst)
  	line = []
    for word in lst[i]:
      line.append(word)
    mapped.append(line)
    
  for i in range(mappedList):
  	if mappedList[i][2] not in counter and mappedList[i][:-1] in ["compute.create.start"]:
    	counter[mappedList[i][2]] = Tenan(mappedList[i][1], False, 1)
    else:
    	resource = counter[mappedList[i][2]]
      if not resource.to_charge:
      	if mappedList[i][:-1] in ["compute.create.end"]
        	resource.to_charge = True
          resource.hours = time(mappedList[i][1]) - time(resurce.time)
          resource.hours = mappedList[i][1]
      	else:
        	if mappedList[i][:-1] in ["compute.exists"]:
          	resouce.hours +=  time(mappedList[i][1]) - time(resurce.time) if 1 else 0
          elif mappedList[i][:-1] in ["compute.delete.start"]:
          	resouce.hours +=  time(mappedList[i][1]) - time(resurce.time) if 1 else 0
          #elif mappedList[i][:-1] in ["compute.delete.end"]:
          
          
      for k, v in cunter:
      	if v.to_charge:
        	print(k + ":" + v.hours)
'''
from datetime import datetime

class Tenant:
    def __init__(self, time, to_charge, hours):
        self.time = time
        self.to_charge = to_charge
        self.total_hours = hours

def calculateHoursForCharge(lst):
    mappedList = []
    counter = {} # dict[resource, Tenant]
    for i in range(len(lst)):
        line = lst[i].split(',')
        line.append(line)
        mappedList.append(line)
    
    for i in range(len(mappedList)):
        if mappedList[i][2] not in counter and mappedList[i][6] in ["compute.create.start"]:
            counter[mappedList[i][2]] = Tenant(mappedList[i][1], False, 0)
        else:
            resource = counter[mappedList[i][2]]
            if mappedList[i][6] in ["compute.create.end"]:
                resource.to_charge = True
                delta = datetime.fromisoformat(mappedList[i][1]) - datetime.fromisoformat(resource.time)
                resource.total_hours += 1 if delta.total_seconds() / (60 * 60) < 2 else 0
            else:
                if mappedList[i][6] in ["compute.exists"]:
                    delta = datetime.fromisoformat(mappedList[i][1]) - datetime.fromisoformat(resource.time)
                    resource.total_hours += 1 if delta.total_seconds() / (60 * 60) < 2 else 0
                elif mappedList[i][6] in ["compute.delete.start"]:
                    delta = datetime.fromisoformat(mappedList[i][1]) - datetime.fromisoformat(resource.time)
                    resource.total_hours += 1 if delta.total_seconds() / (60 * 60) < 2 else 0
            resource.time = mappedList[i][1]
                #elif mappedList[i][:-1] in ["compute.delete.end"]:
          
          
    for k, v in counter.items():
        if v.to_charge:
            print(str(k) + ":" + str(v.total_hours))

lst = ["98112,2020-08-01T00:15:00,7001,compute,myvm001,XL,compute.create.start",
    "98112,2020-08-01T00:18:00,7001,compute,myvm001,XL,compute.create.end",
    "98112,2020-08-01T01:15:01,7001,compute,myvm001,XL,compute.exists",
    "98112,2020-08-01T02:15:00,7001,compute,myvm001,XL,compute.exists",
    "98112,2020-08-01T03:15:00,7001,compute,myvm001,XL,compute.delete.start",
    "98112,2020-08-01T03:18:02,7001,compute,myvm001,XL,compute.delete.end"]

calculateHoursForCharge(lst)