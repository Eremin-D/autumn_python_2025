# todo: Преобразуйте переменную age и foo в число
# age = "23"
# foo = "23abc"

age = "23"
foo = "23abc"

age_ = int(age)
foo_ = int(foo)

print(type(age_))
print(type(foo_))


# Преобразуйте переменную age в Boolean
# age = "123abc"

age = "123abc"
bool_ = bool(age)
print(bool_)

# Преобразуйте переменную flag в Boolean
# flag = 1

flag = 1
flag_ = bool(flag)
print(flag_)

# Преобразуйте значение в Boolean
# str_one = "Privet"
# str_two = ""

str_one = "Privet"
str_two = "" # ложное - строка

print(bool("Privet"))
print(bool(""))

# Преобразуйте значение 0 и 1 в Boolean

zero = 0
one = 1

zero_ = bool(zero)
one_ = bool(one)
print(zero_)
print(one_)

# Преобразуйте False в строку

bool_ = False
str_ = str(bool_)
print(str_)
print(type(str_))
