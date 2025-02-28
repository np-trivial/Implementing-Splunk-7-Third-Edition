from subprocess import Popen
from subprocess import PIPE
from collections import defaultdict
import re


def add_to_key(fieldname, fields):
    return " " + fieldname + "=" + fields[fieldname]

output = Popen("netstat -n -p tcp", stdout=PIPE,
               shell=True).stdout.read()

counts = defaultdict(int)
for l in output.splitlines():
    if "ESTABLISHED" in l:
        pattern = r"(?P<protocol>\S+)\s+\d+\s+\d+\s+"
        pattern += r"(?P<local_addr>.*?)[^\d](?P<local_port>\d+)\s+"
        pattern += r"(?P<remote_addr>.*)[^\d](?P<remote_port>\d+)"
        m = re.match(pattern, l)
        fields = m.groupdict()

        if "local_port" in fields and "remote_port" in fields:
            if fields["local_addr"] == fields["remote_addr"]:
                continue
            try:
                if int(fields["local_port"]) < 1024:
                    key = "type=incoming"
                    key += add_to_key("local_addr", fields)
                    key += add_to_key("local_port", fields)
                    key += add_to_key("remote_addr", fields)
                else:
                    key = "type=outgoing"
                    key += add_to_key("remote_addr", fields)
                    key += add_to_key("remote_port", fields)
                    key += add_to_key("local_addr", fields)
            except:
                print "Unexpected error:", sys.exc_info()[0]

            counts[key] += 1

for k, v in sorted(counts.items()):
    print k + " count=" + str(v)

"""
Active Internet connections
Proto Recv-Q Send-Q  Local Address          Foreign Address        (state)
tcp4       0      0  192.168.0.20.63241     17.158.10.104.443      ESTABLISHED
tcp4      37      0  192.168.0.20.63173     204.236.220.91.443     CLOSE_WAIT
tcp4       0      0  192.168.0.20.55104     17.158.8.60.993        ESTABLISHED
"""
