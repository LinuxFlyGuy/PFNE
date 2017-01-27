oids = (
    ('ifDescr_fa4', '1.3.6.1.2.1.2.2.1.2.5'),
    ('ifInOctets_fa4', '1.3.6.1.2.1.2.2.1.10.5'),
    ('ifInUcastPkts_fa4', '1.3.6.1.2.1.2.2.1.11.5'),
    ('ifOutOctets_fa4', '1.3.6.1.2.1.2.2.1.16.5'),
    ('ifOutUcastPkts_fa4', '1.3.6.1.2.1.2.2.1.17.5')
)

def test(saying, oid):
    print "%s %s" % (saying, oid)

for n, oid in oids:
    test(n, oid)
    test(n, oid)
