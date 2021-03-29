#访问列表元素
bicycle = ['trek','cannondale','redline','specialized']
print(bicycle[0]) #0就是第一个，以此类推
print(bicycle[-1]) #-1就是最后一个，以此类推
print(bicycle[0].title())

#练习
name = ['john','diva','kevin','jane']
print('i like '+name[0])

#修改，添加和删除元素
motocycles = ['honda','yamaha','suzuki']
motocycles[0] = 'ducati' #修改某一处的元素
print(motocycles)
motocycles.append('ducati') #在末尾增加一个元素
print(motocycles)
motocycles.insert(0,'ducati') #在某处增加一个元素
print(motocycles)
del motocycles[0] #永久删除某个元素
print(motocycles)

popped_motocycles = motocycles.pop(1)
print(motocycles)
print(popped_motocycles) #删除某一处的元素，但可以接着使用

motocycles.remove('ducati')
print(motocycles) #根据元素的值来删除

too_expensive = 'suzuki' #在remove中保留被删去的元素
motocycles.remove(too_expensive)
print(motocycles)
print(too_expensive)


#练习
guests = ['john','kevin','jane']
print(guests[0] + ' cannot come tonight')
guests[0] = 'joe'
print(guests)
guests.insert(0,'vic')
guests.insert(2,'han')
guests.append('lu')
print(guests)
popped_guests = guests.pop(0)
print(popped_guests)
popped_guests = guests.pop(0)
print(popped_guests)
popped_guests = guests.pop(0)
print(popped_guests)
popped_guests = guests.pop(0)
print(popped_guests)
print(guests)
del guests[0]
del guests[0]
print(guests)

#组织列表
cars = ['bmw','audi','toyota','subaru']
cars.sort() #对列表进行永久排序
print(cars)

cars = ['bmw','audi','toyota','subaru']
print(sorted(cars)) #暂时给列表排序
car = sorted(cars,reverse=True) #给列表暂时反向排序
print(car)

cars.reverse() #倒着打印列表
print(cars)

print(len(cars)) #确定列表的长度

#练习
destinations = ['italy','paris','london','norway','denmark']
print(sorted(destinations))
destination = sorted(destinations,reverse=True)
print(destination)
destinations.reverse()
print(destinations)
destinations.reverse()
print(destinations)
destinations.sort()
print(destinations)