oids = (
    ('ifDescr_fa4', '1.3.6.1.2.1.2.2.1.2.5'),
    ('ifInOctets_fa4', '1.3.6.1.2.1.2.2.1.10.5'),
    ('ifInUcastPkts_fa4', '1.3.6.1.2.1.2.2.1.11.5'),
    ('ifOutOctets_fa4', '1.3.6.1.2.1.2.2.1.16.5'),
    ('ifOutUcastPkts_fa4', '1.3.6.1.2.1.2.2.1.17.5')
)
ino = [1,2,3,4,5]

for n, oid in oids:
    if 'InOctets' in n:
        print "%s %s" % (n, oid)

print 11 - ino[-1]
