print("The generator is 3 and the prime mod is 17")
idahoprivate = input("Enter Person 1 Private Key: ")
privittprivate = input("Enter Person 2 Private Key: ")
idahopublic = 3**int(idahoprivate) % 17
privittpublic = 3**int(privittprivate) % 17
idahofinal = int(privittpublic)**int(idahoprivate) % 17
privittfinal = int(idahopublic)**int(privittprivate) % 17
print(idahofinal)
print(privittfinal)
