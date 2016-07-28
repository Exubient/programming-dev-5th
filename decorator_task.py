def absolute(fn):
      def wrap(*args):
            ls=[];
            for x in args:
                  ls.append(abs(x))
            return fn(*ls)
      return wrap

      # ls=[abs(x) for x in args]
      # ls=map(abs,args)

@absolute
def mysum(*args):
      return sum(args)

print (mysum(-13,1,2))