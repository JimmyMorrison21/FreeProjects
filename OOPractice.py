class V1:
    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.__checkpas()
    def __checkpas(self):
        z = 0
        for i in self.password:
            if i.isupper() == True :
                z += 1
        if len(self.password) < 8 or (z == 0):
            raise ValueError ('Слабый пароль')


    def save(self):
        with open('users','a') as r:
            r.write(f'{self.login,self.password}'+'\n'+'#')


x = V1('Jacky','Valentino')
x.save()