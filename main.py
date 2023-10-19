def tpl_sort(tpl):
    for i in tpl:
        if not isinstance(i, int):
            return tpl
    result = (sorted(tpl))
    return result

def slicer(tpl, element):
    if element not in tpl:
        return ()
    if tpl.count(element) == 1:
        return (tpl[tpl.index(element):])
    elif tpl.count(element) == 2:
        s = ''
        for i in tpl:
            s += str(i)
        return tpl[s.index(str(element)):s.rindex(str(element))+1]

def sieve(tpl):
    tpl = tuple(set(tpl))
    return tuple(reversed(tpl))

def del_from_tuple(tpl, element):
    if element not in tpl:
        print('element not in tuple')
        return tpl
    
    s = []
    for i in tpl:
        s.append(i)
    s.remove(element)
    
    return tuple(s)

def good_students(students):
    avg = 0
    for student in students:
        avg += student[2]
    avg /= len(students)

    names = []
    for student in students:
        if student[2] > avg:
            names.append(student[0])

    shortNames = ''
    for name in names:
        end = name.index(' ')
        shortNames += f'{name[:end]}, '

    return f"Ученики {shortNames[:-2]} в этом семестре хорошо учатся!"

students = (('Сапельников Денис Алексеевич', 16, 3.5, 'Новосибирск'),
            ("Федулов Дмитрий Игоревич", 17, 3.7, "Новосибирск"),
            ("Лохустин Кирилл Максимович", 17, 3.4, "Новосибирск"),
            ("Кондратенко Дмитрий Алекстандрович", 17, 3.9, "Чик"),
            ("Рылякова Дарья Максимовна", 17, 1.52, "Чулым"),
            ("Четвирикова Олеся Александровна", 17, 2.1, "Рубцовск"),
            ("Кожевников Марк Евгеньевич", 17, 3.3, "Новосибирск"))
    
print(good_students(students))
