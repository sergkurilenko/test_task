import pytest
from delivery import calculate_delivery_cost

# Тест 1: Хрупкий груз на расстояние более 30 км (должно вызывать ошибку)
def test_fragile_over_30km():
    with pytest.raises(ValueError):
        calculate_delivery_cost(35, "маленькие", True, "обычная")

# Тест 2: Хрупкий груз на расстояние 20 км, маленькие габариты, повышенная загруженность
def test_fragile_20km_small_dimensions_increased_workload():
    assert calculate_delivery_cost(20, "маленькие", True, "повышенная") == 720  # (200 + 100 + 300) * 1.2

# Тест 3: Нехрупкий груз на расстояние 5 км, большие габариты, высокая загруженность
def test_non_fragile_5km_large_dimensions_high_workload():
    assert calculate_delivery_cost(5, "большие", False, "высокая") == 420  # (100 + 200) * 1.4

# Тест 4: Нехрупкий груз на расстояние 1 км, маленькие габариты, обычная загруженность
def test_non_fragile_1km_small_dimensions_normal_workload():
    assert calculate_delivery_cost(1, "маленькие", False, "обычная") == 400  # 50 + 100 = 150, но минимальная стоимость 400

# Тест 5: Хрупкий груз на расстояние 15 км, большие габариты, очень высокая загруженность
def test_fragile_15km_large_dimensions_very_high_workload():
    assert calculate_delivery_cost(15, "большие", True, "очень высокая") == 1120  # (200 + 200 + 300) * 1.6

# Тест 6: Нехрупкий груз на расстояние 40 км, маленькие габариты, обычная загруженность
def test_non_fragile_40km_small_dimensions_normal_workload():
    assert calculate_delivery_cost(40, "маленькие", False, "обычная") == 400  # 300 + 100 = 400

# Тест 7: Нехрупкий груз на расстояние 25 км, большие габариты, повышенная загруженность
def test_non_fragile_25km_large_dimensions_increased_workload():
    assert calculate_delivery_cost(25, "большие", False, "повышенная") == 480  # (200 + 200) * 1.2

# Тест 8: Хрупкий груз на расстояние 10 км, маленькие габариты, высокая загруженность
def test_fragile_10km_small_dimensions_high_workload():
    assert calculate_delivery_cost(10, "маленькие", True, "высокая") == 700  # (100 + 100 + 300) * 1.4

# Тест 9: Нехрупкий груз на расстояние 2 км, большие габариты, обычная загруженность
def test_non_fragile_2km_large_dimensions_normal_workload():
    assert calculate_delivery_cost(2, "большие", False, "обычная") == 400  # 50 + 200 = 250, но минимальная стоимость 400

# Тест 10: Хрупкий груз на расстояние 30 км, маленькие габариты, обычная загруженность
def test_fragile_30km_small_dimensions_normal_workload():
    assert calculate_delivery_cost(30, "маленькие", True, "обычная") == 600  # 200 + 100 + 300

# Тесты для расстояния по методу граничных значений
def test_large_fragile_distance_0km():
    """Проверка минимального расстояния (0 км) для больших хрупких товаров."""
    assert calculate_delivery_cost(0, "большие", True, "обычная") == 550  # 50 + 200 + 300 = 550

def test_large_fragile_distance_1_9km():
    """Проверка значения чуть ниже границы 2 км для больших хрупких товаров."""
    assert calculate_delivery_cost(1.9, "большие", True, "обычная") == 550  # 100 + 200 + 300 = 550

def test_large_fragile_distance_2km():
    """Проверка границы 2 км для больших хрупких товаров."""
    assert calculate_delivery_cost(2, "большие", True, "обычная") == 550  # 50 + 200 + 300 = 550

def test_large_fragile_distance_2_1km():
    """Проверка значения чуть выше границы 2 км для больших хрупких товаров."""
    assert calculate_delivery_cost(2.1, "большие", True, "обычная") == 600  # 100 + 200 + 300 = 600

def test_large_fragile_distance_9_9km():
    """Проверка значения чуть ниже границы 10 км для больших хрупких товаров."""
    assert calculate_delivery_cost(9.9, "большие", True, "обычная") == 600  # 100 + 200 + 300 = 600

def test_large_fragile_distance_10km():
    """Проверка границы 10 км для больших хрупких товаров."""
    assert calculate_delivery_cost(10, "большие", True, "обычная") == 600  # 100 + 200 + 300 = 600

def test_large_fragile_distance_10_1km():
    """Проверка значения чуть выше границы 10 км для больших хрупких товаров."""
    assert calculate_delivery_cost(10.1, "большие", True, "обычная") == 700  # 200 + 200 + 300 = 700

def test_large_fragile_distance_29_9km():
    """Проверка значения чуть ниже границы 30 км для больших хрупких товаров."""
    assert calculate_delivery_cost(29.9, "большие", True, "обычная") == 700  # 200 + 200 + 300 = 600

def test_large_fragile_distance_30km():
    """Проверка границы 30 км для больших хрупких товаров."""
    assert calculate_delivery_cost(30, "большие", True, "обычная") == 700  # 200 + 200 + 300 = 700

def test_large_fragile_distance_30_1km():
    """Проверка значения чуть выше границы 30 км для больших хрупких товаров (должно вызывать ошибку)."""
    with pytest.raises(ValueError):
        calculate_delivery_cost(30.1, "большие", True, "обычная")

def test_large_fragile_distance_100km():
    """Проверка большого расстояния (100 км) для больших хрупких товаров (должно вызывать ошибку)."""
    with pytest.raises(ValueError):
        calculate_delivery_cost(100, "большие", True, "обычная")

# негативные тесты

def test_negative_distance():
    """Проверка отрицательного расстояния (должно вызывать ошибку)."""
    with pytest.raises(ValueError):
        calculate_delivery_cost(-10, "большие", True, "обычная")

def test_bad_distance():
    """Проверка нечислового расстояния (должно вызывать ошибку)."""
    with pytest.raises(ValueError):
        calculate_delivery_cost("АААА", "большие", True, "обычная")

def test_bad_size():
    """Проверка неподдерживаемого размера (должно вызывать ошибку)."""
    with pytest.raises(ValueError):
        calculate_delivery_cost(8, "ОГРОМНЫЕ", True, "обычная")

def test_bad_fragility():
    """Проверка неподдерживаемой хрупкости (должно вызывать ошибку)."""
    with pytest.raises(ValueError):
        calculate_delivery_cost(8, "большие", "хрупкое", "обычная")
