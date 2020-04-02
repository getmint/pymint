class Variable(object):
    def __init__(self, var):
        self.__var = var

    def __repr__(self):
        return "<Variable {}>".format(self.__var.__repr__())

    def __str__(self):
        return self.__var.__str__()

    def __bytes__(self):
        return self.__var.__bytes__()

    def __format__(self, format_spec):
        return self.__var.__format__(format_spec)

    def __lt__(self, other):
        return self.__var.__lt__(other)

    def __le__(self, other):
        return self.__var.__le__(other)

    def __eq__(self, other):
        return self.__var.__eq__(other)

    def __ne__(self, other):
        return self.__var.__ne__(other)

    def __gt__(self, other):
        return self.__var.__gt__(other)

    def __ge__(self, other):
        return self.__var.__ge__(other)

    def __hash__(self):
        return self.__var.__hash__()

    def __bool__(self):
        return self.__var.__bool__()

    def __getattr__(self, name):
        return self.__var.__getattribute__(name)

    def __setattr__(self, name, value):
        # TODO: Use this to track changes
        if name != "_Variable__var":
            self.__var.__setattr__(name, value)
        else:
            super(Variable, self).__setattr__(name, value)

    def __delattr__(self, name):
        self.__var.__delattr__(name)

    def __dir__(self):
        return self.__var.__dir__()

    def __call__(self, *args):
        return self.__var.__call__(*args)

    def __len__(self):
        return self.__var.__len__()

    def __length_hint__(self):
        return self.__var.__length_hint__()

    def __getitem__(self, key):
        return self.__var.__getitem__(key)

    def __setitem__(self, key, value):
        return self.__var.__setitem__(key, value)

    def __delitem__(self, key):
        return self.__var.__delitem__(key)

    def __iter__(self):
        return self.__var.__iter__()

    def __reversed__(self):
        return self.__var.__reversed__()

    def __contains__(self, item):
        return self.__var.__contains__(item)

    def __add__(self, other):
        return self.__var.__add__(other)

    def __sub__(self, other):
        return self.__var.__sub__(other)

    def __mul__(self, other):
        return self.__var.__mul__(other)

    def __matmul__(self, other):
        return self.__var.__matmul__(other)

    def __truediv__(self, other):
        return self.__var.__truediv__(other)

    def __floordiv__(self, other):
        return self.__var.__floordiv__(other)

    def __mod__(self, other):
        return self.__var.__mod__(other)

    def __divmod__(self, other):
        return self.__var.__divmod__(other)

    def __pow__(self, other, modulo=None):
        return self.__var.__pow__(other, modulo)

    def __lshift__(self, other):
        return self.__var.__lshift__(other)

    def __rshift__(self, other):
        return self.__var.__rshift__(other)

    def __and__(self, other):
        return self.__var.__and__(other)

    def __xor__(self, other):
        return self.__var.__xor__(other)

    def __or__(self, other):
        return self.__var.__or__(other)

    def __radd__(self, other):
        return self.__var.__radd__(other)

    def __rsub__(self, other):
        return self.__var.__rsub__(other)

    def __rmul__(self, other):
        return self.__var.__rmul__(other)

    def __rmatmul__(self, other):
        return self.__var.__rmatmul__(other)

    def __rtruediv__(self, other):
        return self.__var.__rtruediv__(other)

    def __rfloordiv__(self, other):
        return self.__var.__rfloordiv__(other)

    def __rmod__(self, other):
        return self.__var.__rmod__(other)

    def __rdivmod__(self, other):
        return self.__var.__rdivmod__(other)

    def __rpow__(self, other, modulo=None):
        return self.__var.__rpow__(other, modulo)

    def __rlshift__(self, other):
        return self.__var.__rlshift__(other)

    def __rrshift__(self, other):
        return self.__var.__rrshift__(other)

    def __rand__(self, other):
        return self.__var.__rand__(other)

    def __rxor__(self, other):
        return self.__var.__rxor__(other)

    def __ror__(self, other):
        return self.__var.__ror__(other)

    # TODO: Use these to track changes

    def __iadd__(self, other):
        self.__var += other
        return self

    def __isub__(self, other):
        self.__var -= other
        return self

    def __imul__(self, other):
        self.__var *= other
        return self

    def __imatmul__(self, other):
        self.__var @= other
        return self

    def __itruediv__(self, other):
        self.__var /= other
        return self

    def __ifloordiv__(self, other):
        self.__var //= other
        return self

    def __imod__(self, other):
        self.__var %= other
        return self

    def __ipow__(self, other, modulo=None):
        self.__var **= other
        return self

    def __ilshift__(self, other):
        self.__var <<= other
        return self

    def __irshift__(self, other):
        self.__var >>= other
        return self

    def __iand__(self, other):
        self.__var &= other
        return self

    def __ixor__(self, other):
        self.__var ^= other
        return self

    def __ior__(self, other):
        self.__var |= other
        return self

    # Up to here.

    def __neg__(self):
        return self.__var.__neg__()

    def __pos__(self):
        return self.__var.__pos__()

    def __abs__(self):
        return self.__var.__abs__()

    def __invert__(self):
        return self.__var.__invert__()

    def __complex__(self):
        return self.__var.__complex__()

    def __int__(self):
        return self.__var.__int__()

    def __float__(self):
        return self.__var.__float__()

    def __index__(self):
        return self.__var.__index__()

    def __round__(self, ndigits=None):
        return self.__var.__round__()

    def __trunc__(self):
        return self.__var.__trunc__()

    def __floor__(self):
        return self.__var.__floor__()

    def __ceil__(self):
        return self.__var.__ceil__()

    def __enter__(self):
        return self.__var.__enter__()

    def __exit__(self, exc_type, exc_value, traceback):
        return self.__var.__exit__(exc_type, exc_value, traceback)

    def __await__(self):
        return self.__var.__await__()
