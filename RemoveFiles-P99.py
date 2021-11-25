import os 

path = input("Enter the File Name which you want to delete :- ")


if os.path.exists(path):
     os.remove(path)         

else:
    print("The Path does not exists")

