
print ('Выберите режим работы программы, 1 - ввод вопросов и правильных ответов, 2 - ответы на вопросы')
regim = int(input ('Введите 1 или 2:'))

if regim == 1:
	file = open ('homework1_2.txt','w')
	quest = []
	ans = []
	i = int(input ('Введите количество вопросов:'))
	k = 1 #Счетчик вопросов на всякий случай
	while i:
		quest.append(input ('Вопрос:'))
		
		ans.append(input('Ответ:'))
		i -=1
		k +=1
	print (quest,'\n')
	print (ans,'\n')
	
	file.write(str(quest))
	file.close()



# elif regim == 2:
#     n = 0 # счетчик правильных ответов
#     m = 1 # счетчик вопросов
#     print ('Привет!\n')
#     print ('Ответь пожалуйста на вопросы:\n')
#     while m <= 3:
# 	    print ('Вопрос',m,':',quest[m-1])
#     	ans1 = input ()
#     	if ans1 == ans[m-1]:
#     		n+=1
#     		print ('Правильный ответ! Ура!')
#     		print ('Всего правильных ответов:',n)
#     	else:
#     		print ('К сожалению ваш ответ неправильный\n','Правильных ответов:',n)
#     	m+=1
#     print ('Вы ответили на ',n,'правильных вопросов!')
