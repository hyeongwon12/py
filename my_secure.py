def sname(name):
    return(name[0])+'**'


def sn(no):
    return(no[0:8])+'******'


def sp(ph):
    return ph.replace(ph[4:8,'****'])

print
(sname("가나다"))
print(sn(961228-1171338))
print(sp(123-8344-3692))

   