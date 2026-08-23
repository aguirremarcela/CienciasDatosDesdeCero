# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

# Esto es un comentario
nombre = "Ana"
edad = 25
print(f"Hola {nombre}, tienes {edad} años")

#users
users = [
    {"id": 0, "name": "Hero"},
    {"id": 1, "name": "Dunn"},
    {"id": 2, "name": "Sue"},
    {"id": 3, "name": "Chi"},
    {"id": 4, "name": "Thor"},
    {"id": 5, "name": "Clive"},
    {"id": 6, "name": "Hicks"},
    {"id": 7, "name": "Devin"},
    {"id": 8, "name": "Kate"},
    {"id": 9, "name": "Klein"}
]
print(users[0])          # Muestra el primer usuario
print(users[0]["name"])  # Muestra solo el nombre del primero
print(users[2]["id"])  
# Datos de amistad- lista de pares identificadores
friendship_pairs=[(0,1),(0,2),(1,2),(1,3),(2,3),(3,4),(4,5),(5,6),(5,7),(6,8),(7,8),(8,9)]
#Inicializar el dict con una lista vacia para cada id de usuario:
friendships={user["id"]:[] for user in users}
#y pasar por todos los pares de amistad para llenarlo:

for i, j in friendship_pairs:
    friendships[i].append(j)
    friendships[j].append(i)
    
def number_of_friends(user):
    "How many friends does _user_ have?"
    user_id= user["id"]
    friend_ids= friendships[user_id]
    return len(friend_ids)
total_connections= sum(number_of_friends(user)
                       for user in users)
num_users=len(users) #longitud de la lista de usuarios

avg_connections= total_connections/num_users
print(avg_connections)

#Crea una lista(user_id, number_of_friends)
number_of_friends_by_id=[(user["id"],number_of_friends(user))
                         for user in users]
number_of_friends_by_id.sort(
    key=lambda id_and_friends: id_and_friends[1],
     reverse=True)

#Cientificos de datos que podria conocer 
def foaf_ids_bad(user):
    "foaf is short for friend of friend"
    return[foaf_id
           for friend_id in friendships[user["id"]]
           for foaf_id in friendships[friend_id]]

print(foaf_ids_bad(users[0])) #[0, 2, 3, 0, 1, 3]
print(friendships[0])

from collections import Counter
def friends_of_friends(user):
    user_id=user["id"]
    return Counter(
        foaf_id
        for friend_id in friendships[user_id]
        for foaf_id in friendships[friend_id]
        if foaf_id != user_id
        and foaf_id not in friendships[user_id]
        )
print(friends_of_friends(users[3])) #Counter({0: 2, 5: 1})
# Esto se lee como a Chi (id 3) tiene dos amigos mutuo con Hero(id 0) pero solo
# uno con Clive(id 5)
#Intereses comunes
interests = [
(0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
(0, "Spark"), (0, "Storm"), (0, "Cassandra"),
(1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
(1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
(2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
(3, "statistics"), (3, "regression"), (3, "probability"),
(4, "machine learning"), (4, "regression"), (4, "decision trees"),
(4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
(5, "Haskell"), (5, "programming languages"), (6, "statistics"),
(6, "probability"), (6, "mathematics"), (6, "theory"),
(7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
(7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
(8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
(9, "Java"), (9, "MapReduce"), (9, "Big Data")
]
def data_scientists_who_like(target_interest):
    "Find the ids of all users who like the target interest."
    return [user_id
            for user_id, user_interest in interests
            if user_interest == target_interest]
print(data_scientists_who_like("Big Data")) # [0, 8, 9]

from collections import defaultdict
# Las claves son intereses, los valores son listas de user_ids con ese interés
user_ids_by_interest = defaultdict(list)
for user_id, interest in interests:
    user_ids_by_interest[interest].append(user_id)
    
# Las claves son user_ids, los valores son listas de intereses para ese user_id
interests_by_user_id = defaultdict(list)  
for user_id, interest in interests:
    interests_by_user_id[user_id].append(interest)

def most_common_interests_with(user):
    return Counter(
        interested_user_id
        for interest in interests_by_user_id[user["id"]]
        for interested_user_id in user_ids_by_interest[interest]
        if interested_user_id != user["id"]
        )
    
# Ver qué intereses tiene el usuario 0 (Hero)
print(interests_by_user_id[0])  
# Output: ['Hadoop', 'Big Data', 'HBase', 'Java', 'Spark', 'Storm',
# 'Cassandra']

# Ver qué usuarios tienen interés en "Python"
print(user_ids_by_interest["Python"])  
# Output: [2, 3, 5]

# Ejemplo 1: Usuario 0 (Hero)
hero = users[0]  # {"id": 0, "name": "Hero"}
resultado_hero = most_common_interests_with(hero)
print(resultado_hero)
# Output: Counter({9: 3, 1: 2, 8: 1, 5: 1})



# Ejemplo 2: Usuario 5 (Clive)
clive = users[5]  # {"id": 5, "name": "Clive"}
resultado_clive = most_common_interests_with(clive)
print(resultado_clive)
# Output: Counter({3: 2, 2: 1, 0: 1, 9: 1})


## Salarios y experiencia 
salaries_and_tenures = [(83000, 8.7), (88000, 8.1),
(48000, 0.7), (76000, 6),
(69000, 6.5), (76000, 7.5),
(60000, 2.5), (83000, 10),
(48000, 1.9), (63000, 4.2)]
# Las claves son años, los valores son listas de los salarios por antigüedad.
salary_by_tenure = defaultdict(list)
for salary, tenure in salaries_and_tenures:
    salary_by_tenure[tenure].append(salary)
# Las claves son años, cada valor es el salario medio para dicha antigüedad.
average_salary_by_tenure = {
tenure: sum(salaries) / len(salaries)
for tenure, salaries in salary_by_tenure.items()
}
# lo anterior nos da poca info . Entonces nos conviene agrupar los años 
#de experiencia 
def tenure_bucket(tenure):
    if tenure < 2:
        return "less than two"
    elif tenure < 5:
        return "between two and five"
    else:
        return "more than five"
    
# Las claves son buckets de años de antigüedad, los valores son listas de
#salarios para bucket
salary_by_tenure_bucket = defaultdict(list)
for salary, tenure in salaries_and_tenures:
    bucket = tenure_bucket(tenure)
    salary_by_tenure_bucket[bucket].append(salary)


# Las claves son buckets de años de antigüedad, los valores son el salario
#medio para bucket
average_salary_by_bucket = {
tenure_bucket: sum(salaries) / len(salaries)
for tenure_bucket, salaries in salary_by_tenure_bucket.items()
}
print(average_salary_by_bucket)
#Output :
#{'more than five': 79166.66666666667, 'less than two': 48000.0,
# 'between two and five': 61500.0}

#Cuentas de pago 
def predict_paid_or_unpaid(years_experience):
    if years_experience < 3.0:
        return "paid"
    elif years_experience < 8.5:
        return "unpaid"
    else:
        return "paid"
    
# Veamos 
print(predict_paid_or_unpaid(2))
#Output :paid
print(predict_paid_or_unpaid(3))
#Output :unpaid

##Temas de interes

words_and_counts = Counter(word

for user, interest in interests
for word in interest.lower().split())

for word, count in words_and_counts.most_common():
    if count > 1:
        print(word, count)