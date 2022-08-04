s="""Address         Age       MAC Address     Interface       Flags
10.192.1.212    00:02:22  bc4a.56f3.f7cc  Vlan1001        
10.192.1.213    00:14:05  bc4a.56f3.f80c  Vlan1001        
10.192.1.214    00:01:53  bc4a.56f3.f80c  Vlan1001        
10.192.1.217    00:00:03  40a6.b736.4750  Vlan1001        
10.192.1.218    00:00:25  40a6.b735.9a30  Vlan1001        
10.192.1.219    00:08:49  40a6.b735.9b40  Vlan1001        
10.192.1.220    00:17:24  40a6.b735.d0f0  Vlan1001        
10.192.1.221    00:00:21  40a6.b735.d0f0  Vlan1001        
10.192.1.222    00:14:26  40a6.b735.d598  Vlan1001        
10.192.1.223    00:00:13  40a6.g736.1eb8  Vlan1001        
10.192.1.227    00:02:37  e8eb.34d6.550c  Vlan1001        
10.192.1.228    00:14:32  e8eb.34h6.550c  Vlan1001        
10.192.1.230    00:10:16  e8eb.34d2.1cec  Vlan1001        
10.192.1.231    00:05:05  e8eb.34d2.1cec  Vlan1001        
10.192.1.232    00:00:01  e8eb.34d2.192C  Vlan1001        
10.192.1.233    00:00:12  e8eb.34d6-294c  Vlan1001        
10.192.1.234    00:02:02  e8eb.34d6.27ac  Vlan1001        
10.192.1.235    00:06:58  e8eb.34d6:1fcc  Vlan1001        
10.192.1.236    00:00:26  e8eb.34d6.1fcc  Vlan1001        
10.192.1.237    00:04:16  e8eb.34D6.1f2c  Vlan1001        
10.192.1.238    00:08:54  e8eb.34d6.2a2c  Vlan1001        
192.168.111.0   00:05:17  689e.0b8c.890f  Ethernet1/61    
192.168.111.2   00:05:17  689e.0b8c.890f  Ethernet1/62  """

x=s.split("\n")
x.pop(0)
print(x)
s1="abcdefABCDEF0123456789."
for item in x:
    a=item.split()
    z=a[2]
    b=z.split(".")
    print(z)
    if len(b)==3:
        if len(b[0])==4 and len(b[1])==4 and len(b[2])==4:
            Valid=True
            for i in z:
                if i not in s1:
                    print("Mac is invalid")
                    Valid=False
                    break
            if Valid==True:
                print("Mac is valid")

        else:
            print("mac is invalid")

    else:
        print("mac is invalid")





