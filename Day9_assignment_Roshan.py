import unittest
def generator():
    for i in range(1, 1000):
        temp = i
        result = 0
        while temp > 0:
            fir = temp % 10
            result += fir ** len(str(i))
            temp = temp // 10
        if (i == result):
            yield result

g=generator()
print(list(g))



def  checkprime(num):
    for i in range(2,num):
        if num%i==0:
            return False
    return True

class testprime(unittest.TestCase):
    def test_prime(self):
        result=checkprime(15)
        self.assertEqual(result,False)
if __name__=="__main__":
    unittest.main()