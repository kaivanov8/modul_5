# Свой YouTube
import time

class User:
    def __init__(self, nickname, password, age):
        self.name = nickname
        self.password = hash(password)
        self.age = age
class Video:
    def __init__(self,title, duration, time_now = 0 ,adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

class UrTube:
    users = []
    videos = []
    current_user =''

    def add(self,*args):
        for i in range(0,len(args)):
            flag = True
            element_of_list = (args[i].title,args[i].duration,args[i].time_now,args[i].adult_mode)
            for j in range(0,len(self.videos)):
                element_in_list= self.videos[j]
                if element_of_list[0] == element_in_list[0]:
                    flag=False
            if flag :
                self.videos.append(element_of_list)

    def get_videos(self, word_):
        list_=[]
        word_= word_.upper()
        for i in ur.videos:
            m = i[0].upper()
            if  m.__contains__(word_):
                list_.append(i[0])
        return list_

    def watch_video(self,name_film):
        if ur.current_user ==  '':
            print ("Ввойдите в аккаунт, чтобы смотреть видео.")
            return
        for kie in ur.videos:
            if kie[3] and ur.current_user[2] < 18:
                print('Вам нет 18 лет, пожалуйста покиньте страницу.')
                return
            if name_film == kie[0]:
                for j in range(kie[2],kie[1]):
                    print (j+1,end=' ')
                    time.sleep(0.2)
                print('Конец видео')

    def log_in(self,nickname,password):
        if self.users.__contains__((nickname,hash(password))):
            ur.current_user = User(nickname,hash(password))

    def register(self,nickname,password,age):
        for element_user_list in ur.users:
            if element_user_list[0] == nickname:
                print(f'Пользователь {nickname} уже существует')
                return
        ur.users.append((nickname,hash(password),age))

        ur.current_user = (nickname,hash(password),age)

ur = UrTube()
v1 = Video("Лучший язык программирования 2024 года",120,0,False)
v2 = Video("Для чего девушкам парень программист?",10,0,adult_mode = True)
ur.add(v1,v1,v2,v2) # добавление видео
print(ur.get_videos('лучший'),' - содержит "лучший"')       # Проверка поиска
print(ur.get_videos('ПРОГ'),' - содержит "ПРОГ"')           # Проверка поиска
ur.watch_video('Для чего девушкам парень программист?')     #       Проверка пользователя на вход
ur.register('vasya_pupkin','123df',13)   #           и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist','222v',25)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin','11гнпрнр23v',55)
ur.watch_video("Лучший язык программирования 2024 года!")   # воспроизведение несуществующего видео
