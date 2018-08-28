grep -v "^@" SRR072905/SRR072905.sam | grep -v 2110000 | cut -f 3 | sort | uniq -c
