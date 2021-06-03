import schedule, csv, time
from easysnmp import Session

def poll(host, comm, ver, mib):
    session = Session(hostname=host, community=comm, version=ver)
    output = session.get(mib)
    print(output)

with open('polling_config.csv') as pc:
    pc_inv = csv.reader(pc)
    for row in pc_inv:
        host = row[0]
        freq = int(row[1])
        comm = row[2]
        ver = int(row[3])
        for mib in row[4:]:
            schedule.every(freq).seconds.do(poll(host, comm, ver, mib))

while True:
    schedule.run_pending()
    time.sleep(1)
