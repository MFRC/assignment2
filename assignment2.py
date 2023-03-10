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
        y = 2023 - self.year
        while p+10 < y:
            p = p + 10
            a.append(p)
        return a

    def modifyYear(self, n):
        num = self.year
        res = ""
        stt = str(self.year)

        for i in range(n):
            res += stt[0]
            res += stt[1]
        num = num*n
        sttt = str(num)
        count = 1
        for i in sttt:
            if count % 2 == 1:
                res += i
            count += 1
        return res

    @staticmethod
    def checkGoodString(string):
        _num_count = 0
        for i in string:
            if i.isdigit():
                _num_count += 1
        if _num_count != 1:
            return False
        if _num_count == 1:
            if len(string) >= 9 and string[0].islower():
                return True
            else:
                return False


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
