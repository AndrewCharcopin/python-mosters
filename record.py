class Record():
  
  def __init__(self, name, stage):
    self.time = self.get_current_time()
    self.name = name
    self.stage = stage
  
  def get_current_time():
    now = time.ctime()
    cnvtime = time.strptime(now)
    return time.strftime("%Y/%m/%d %H:%M", cnvtime) 

  def get_current_time(self):
    import time
    now = time.ctime()
    cnvtime = time.strptime(now)
    return time.strftime("%Y/%m/%d %H:%M", cnvtime)     

  def write_csv(self):
    import csv
    import pprint
    with open('./record.csv','a') as f:
      writer = csv.writer(f)
      writer.writerow([self.time, self.name, self.stage])
  
  #return datas in array like [[self.time, self.name, self.stage],[...]]
  def read_csv(self):
    import csv
    import pprint
    with open('./record.csv') as f:
      reader = csv.reader(f)
      datas = [row for row in reader]
      return datas

