zero = lambda f: lambda x: x
succ = lambda c: lambda f: lambda x: f(c(f)(x))
numerif = lambda c: c(lambda i: i+1 )(0)

def churchify(n):
    def _f(f):
        def _x(x):
            for i in range(n): x = f(x)
            return x
        return _x
    return _f

church_add = lambda m: lambda n: lambda s: lambda z: (m(s)(n(s)(z)))
church_mul = lambda m: lambda n: lambda s: m(n(s))
church_pow = lambda m: lambda n: lambda s: (n)(m)((s))

find_church = lambda fn,x,y: numerif(fn(churchify(x)))(churchify(y))
test_church = lambda fn,x,r,msg: test.assert_equals(find_church(fn,x,y),r,msg)

