'''
This script would have template for reading and writing files for the google code jam thing.

@author: nanda
'''
##############################################################################
class memoized(object):
   '''Decorator. Caches a function's return value each time it is called.
   If called later with the same arguments, the cached value is returned 
   (not reevaluated).
   '''
   def __init__(self, func):
      self.func = func
      self.cache = {}
   def __call__(self, *args):
      try:
         return self.cache[args]
      except KeyError:
         value = self.func(*args)
         self.cache[args] = value
         return value
      except TypeError:
         # uncachable -- for instance, passing a list as an argument.
         # Better to not cache than to blow up entirely.
         return self.func(*args)
   def __repr__(self):
      '''Return the function's docstring.'''
      return self.func.__doc__
   def __get__(self, obj, objtype):
      '''Support instance methods.'''
      return functools.partial(self.__call__, obj)
#############################################################################
@memoized
def get_square(x):
    return x * x


##############################################################################
# This part would contain the logic for solving actual puzzle.
def solve_puzzle1(input):
    r, t = input.split(" ")
    r = long(r)
    t = long(t)
    print r, t
    s1 = get_square(r)
    s2 = get_square(r+1)
    
    f = s2 - s1
    
    ans = 0
    while(True):
        #print float(t*2/2*f + (ans - 1)*4)
        #print ans
        if ans <= float(t*2/(2*f + (ans - 1)*4)):
            ans += 1
        else:
            break
        
    return ans
    
    
def solve_puzzle(input):
    r, t = input.split(" ")
    r = long(r)
    t = long(t)
    print r, t
    ans = 0
    temp = 0
    while(t >= 0):        
        s1 = get_square(r)
        s2 = get_square(r+1)
    
        temp = (s2 - s1)
        t = t - temp
        r += 2
        if t >= 0:
            ans += 1
    return ans

##############################################################################
def main():
    # Test Input
    #in_file_name = "Test.in"
    #out_file_name = "Test.out"
    
    # Code for Reading and writing.
    # Small Files.
    in_file_name = "A-small-attempt0.in"
    #in_file_name = "Test.in"
    out_file_name = "A-small-attempt0.out"
    
    in_file =  "d:\codejam\problems\\" + in_file_name
    out_file = "d:\codejam\problems\\" + out_file_name
    
    reader = open(in_file)
    writer = open(out_file, 'w')
    
    reader.readline()
    for case_no, input in enumerate(reader):
        result = solve_puzzle(input)
        print "Case #" + str(case_no+1)+ ": " , result
        writer.write("Case #" + str(case_no+1)+ ": " + str(result) + "\n")   
    writer.close()
    
##############################################################################
if __name__== "__main__":
    main()