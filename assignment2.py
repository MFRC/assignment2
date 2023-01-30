import socket


class Assignment2:
    def __init__(self, year):
        self.year = year

    def tellAge(self, currentYear):
        age = currentYear - self.year
        print("Your age is {}".format(age))

    def listAnniversaries(self):
        a = []
        p = 0
        while p <= 2023 - self.year:
            a.append(p)
            p = p + 10
        return a

    def modifyYear(self, n):
        num = n
        res = ""
        arr = str(num)
        for i in range(n):
            res += arr[:2]
        num = num*n
        lst = str(num)
        arr1 = lst[::2]
        res += arr1
        return res

    @staticmethod
    def checkGoodString(string):
        if len(string) < 9:
            return False
        if not string[0].islower():
            return False
        _num_count = 0
        for i in string:
            if i.isdigit():
                _num_count += 1
            if _num_count > 1:
                return False

        return True

    @staticmethod
    def connectTcp(host, port):

        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            host_address = socket.gethostbyname(host)
            s.connect((host_address, port))
            s.close()
            return True
        except:
            return False
