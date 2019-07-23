def write_csv(name, stage):
  import csv, time
  now = time.ctime()
  cnvtime = time.strptime(now)
  time.strftime("%Y/%m/%d %H:%M", cnvtime) 
  with open('./record.csv','a') as f:
    writer = csv.writer(f)
    writer.writerow([time.strftime("%Y/%m/%d %H:%M", cnvtime) , name, stage])

write_csv("aaaa", 5)