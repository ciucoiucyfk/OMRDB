import pickle
ak = ['a','a','a','a','a','a','a','a','a','a']
def write(dic):
    file= open('C:/Users/Abhinav/Documents/Class 12 Project Computer/bin/config.dat','wb')
    pickle.dump([dic,['master','a123','master']],file)
def read():
    file= open('C:/Users/Abhinav/Documents/Class 12 Project Computer/bin/config.dat','rb')
    print(pickle.load(file))
read()
