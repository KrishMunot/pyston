def f(a, b=2, *args, **kw):
    pass

c = f.func_code
print c.co_argcount
print c.co_varnames
print hex(c.co_flags & 0x0c)

def f(l=[]):
    print l
f()
f.func_defaults[0].append(5)
f()

def f():
    pass
print f.func_defaults
