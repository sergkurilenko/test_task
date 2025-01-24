def calculate_delivery_cost(distance, dimensions, is_fragile, workload):
    # Расчет стоимости в зависимости от расстояния
    try:
        if distance < 0:
            raise ValueError("Дистанция не может быть отрицательной")
        elif distance > 30:
            cost = 300
        elif distance > 10:
            cost = 200
        elif distance > 2:
            cost = 100
        elif distance >= 0 :
            cost = 50
    except:
        raise ValueError("Дистанция указана неверно")
    
    # Проверка на невозможность доставки хрупкого груза на расстояние более 30 км
    if is_fragile and distance > 30:
        raise ValueError("Хрупкие грузы нельзя возить на расстояние более 30 км")

    # Добавление стоимости в зависимости от габаритов
    if dimensions == "большие":
        cost += 200
    elif dimensions == "маленькие":
        cost += 100
    else:
        raise ValueError("Неверно указаны габариты, поддерживаемы значения: 'большие', 'маленькие'")

    # Добавление стоимости за хрупкость
    if not isinstance(is_fragile, bool):
        raise ValueError("Неверно указана хрупкость, поддерживаемы значения: True, False")
    elif is_fragile:
        cost += 300

    # Умножение на коэффициент загруженности
    if workload == "очень высокая":
        cost *= 1.6
    elif workload == "высокая":
        cost *= 1.4
    elif workload == "повышенная":
        cost *= 1.2
    else:
       cost *= 1
        

    # Проверка на минимальную стоимость доставки
    if cost < 400:
        cost = 400

    return cost