s="""Interface Secondary VLAN(Type) Status Reason
-------------------------------------------------------------------------------
Vlan1 -- down Administratively down
Vlan10 -- down VLAN/BD is down
Vlan139 -- up --
Vlan1001 -- up --
Vlan1101 -- down VLAN/BD is down
Vlan1102 -- down VLAN/BD is down
Vlan1103 -- down VLAN/BD is down
Vlan1104 -- down VLAN/BD is down
Vlan1105 -- down VLAN/BD is down
Vlan1111 -- down VLAN/BD is down
Vlan1112 -- down VLAN/BD is down
Vlan1122 -- down VLAN/BD is down
Vlan1132 -- down VLAN/BD is down
Vlan1201 -- down VLAN/BD is down
Vlan1202 -- down VLAN/BD is down
Vlan1203 -- down VLAN/BD is down
Vlan1204 -- down VLAN/BD is down
Vlan1205 -- down VLAN/BD is down
Vlan1211 -- down VLAN/BD is down
Vlan1212 -- down VLAN/BD is down
Vlan1222 -- down VLAN/BD is down
Vlan1232 -- down VLAN/BD is down
Vlan2352 -- down VLAN/BD does not exist
Vlan2353 -- down VLAN/BD does not exist
Vlan3522 -- up --
Vlan3960 -- up --
Vlan3961 -- up --
Vlan3962 -- up --
Vlan3963 -- up --
Vlan3964 -- up --"""

x=s.split("\n")
x.pop(0)
x.pop(0)
d={}
print(x)
for i in x:
    a=i.split(" ")
    d[a[0]]=a[2]
print(d)