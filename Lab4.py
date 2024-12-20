from point import Point_n
import matplotlib.pyplot as plt

def main():
    # Створення чотирьох точок
    points = [
        Point_n(10, 20),
        Point_n(30, 40),
        Point_n(-50, 60),
        Point_n(70, -80)
    ]

    # Виведення координат початкових точок
    print("Координати початкових точок:")
    for i, point in enumerate(points, start=1):
        print(f"Точка {i}: ({point.x}, {point.y})")

    # Обчислення відстані між четвертою та третьою точками
    distance = points[3].distance_to(points[2])
    print(f"Відстань між точками 4 і 3: {distance:.2f}")

    # Переміщення другої точки на 17 вліво
    points[1].move(-17, 0)

    # Виведення координат після змін
    print("\nКоординати після змін:")
    for i, point in enumerate(points, start=1):
        print(f"Точка {i}: ({point.x}, {point.y})")

    # Візуалізація точок до та після змін
    x_initial = [10, 30, -50, 70]
    y_initial = [20, 40, 60, -80]
    x_after = [point.x for point in points]
    y_after = [point.y for point in points]

    plt.figure(figsize=(10, 5))

    # Початкові точки
    plt.subplot(1, 2, 1)
    plt.scatter(x_initial, y_initial, color='blue', label='Початкові точки')
    for i, (x, y) in enumerate(zip(x_initial, y_initial), start=1):
        plt.text(x, y, f" {i}", fontsize=9)
    plt.title("Початкові точки")
    plt.grid()
    plt.legend()

    # Точки після змін
    plt.subplot(1, 2, 2)
    plt.scatter(x_after, y_after, color='red', label='Точки після змін')
    for i, (x, y) in enumerate(zip(x_after, y_after), start=1):
        plt.text(x, y, f" {i}", fontsize=9)
    plt.title("Точки після змін")
    plt.grid()
    plt.legend()

    plt.show()

    # Збереження точок у текстовий файл
    with open("points.txt", "w") as f:
        for i, point in enumerate(points, start=1):
            f.write(f"({i}) {point.x}:{point.y}\n")
    print("\nКоординати точок збережено у файл 'points.txt'.")

if __name__ == "__main__":
    main()
