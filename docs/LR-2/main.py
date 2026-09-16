"""Решение лабораторной работы № 2 по NumPy."""

from pathlib import Path
from typing import Any

import matplotlib
import numpy as np
import pandas as pd
import seaborn as sns
from numpy.typing import NDArray

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402


Array = NDArray[Any]
PLOTS_DIR = Path("plots")


def create_vector() -> NDArray[np.int_]:
    """Создать вектор целых чисел от 0 до 9 включительно."""
    return np.arange(10)


def create_matrix() -> NDArray[np.float64]:
    """Создать матрицу 5 x 5 со случайными числами из диапазона [0, 1)."""
    return np.random.rand(5, 5)


def reshape_vector(vec: Array) -> Array:
    """Преобразовать вектор из формы (10,) в форму (2, 5)."""
    return vec.reshape(2, 5)


def transpose_matrix(mat: Array) -> Array:
    """Вернуть транспонированную копию представления матрицы."""
    return mat.T


def vector_add(a: Array, b: Array) -> Array:
    """Выполнить поэлементное сложение двух векторов."""
    return a + b


def scalar_multiply(vec: Array, scalar: int | float) -> Array:
    """Умножить каждый элемент вектора на скаляр."""
    return vec * scalar


def elementwise_multiply(a: Array, b: Array) -> Array:
    """Выполнить поэлементное умножение двух массивов."""
    return a * b


def dot_product(a: Array, b: Array) -> float:
    """Вычислить скалярное произведение двух векторов."""
    return float(np.dot(a, b))


def matrix_multiply(a: Array, b: Array) -> Array:
    """Выполнить матричное умножение двух массивов."""
    return a @ b


def matrix_determinant(a: Array) -> float:
    """Вычислить определитель квадратной матрицы."""
    return float(np.linalg.det(a))


def matrix_inverse(a: Array) -> NDArray[np.float64]:
    """Вычислить обратную матрицу."""
    return np.linalg.inv(a)


def solve_linear_system(a: Array, b: Array) -> NDArray[np.float64]:
    """Найти решение системы линейных уравнений Ax = b."""
    return np.linalg.solve(a, b)


def load_dataset(path: str | Path = "data/students_scores.csv") -> Array:
    """Загрузить числовые данные из CSV-файла в массив NumPy."""
    return pd.read_csv(path).to_numpy()


def statistical_analysis(data: Array) -> dict[str, float]:
    """Рассчитать основные описательные статистики массива."""
    return {
        "mean": float(np.mean(data)),
        "median": float(np.median(data)),
        "std": float(np.std(data)),
        "min": float(np.min(data)),
        "max": float(np.max(data)),
        "percentile_25": float(np.percentile(data, 25)),
        "percentile_75": float(np.percentile(data, 75)),
    }


def normalize_data(data: Array) -> NDArray[np.float64]:
    """Нормализовать данные в диапазон [0, 1] методом Min-Max."""
    minimum = np.min(data)
    maximum = np.max(data)
    value_range = maximum - minimum

    if value_range == 0:
        return np.zeros_like(data, dtype=float)

    return (data - minimum) / value_range


def plot_histogram(data: Array) -> None:
    """Построить и сохранить гистограмму оценок по математике."""
    PLOTS_DIR.mkdir(parents=True, exist_ok=True)
    figure, axes = plt.subplots(figsize=(8, 5))
    axes.hist(data, bins="auto", edgecolor="black")
    axes.set_title("Распределение оценок по математике")
    axes.set_xlabel("Оценка")
    axes.set_ylabel("Количество студентов")
    figure.tight_layout()
    figure.savefig(PLOTS_DIR / "histogram.png", dpi=150)
    plt.close(figure)


def plot_heatmap(matrix: Array) -> None:
    """Построить и сохранить тепловую карту матрицы корреляции."""
    PLOTS_DIR.mkdir(parents=True, exist_ok=True)
    figure, axes = plt.subplots(figsize=(7, 6))
    sns.heatmap(matrix, annot=True, cmap="coolwarm", ax=axes)
    axes.set_title("Корреляция результатов по предметам")
    figure.tight_layout()
    figure.savefig(PLOTS_DIR / "heatmap.png", dpi=150)
    plt.close(figure)


def plot_line(x: Array, y: Array) -> None:
    """Построить и сохранить график оценок студентов по математике."""
    PLOTS_DIR.mkdir(parents=True, exist_ok=True)
    figure, axes = plt.subplots(figsize=(8, 5))
    axes.plot(x, y, marker="o")
    axes.set_title("Оценки студентов по математике")
    axes.set_xlabel("Номер студента")
    axes.set_ylabel("Оценка")
    axes.grid(True, alpha=0.3)
    figure.tight_layout()
    figure.savefig(PLOTS_DIR / "line.png", dpi=150)
    plt.close(figure)


def test_create_vector() -> None:
    """Проверить создание вектора."""
    vector = create_vector()
    assert isinstance(vector, np.ndarray)
    assert vector.shape == (10,)
    assert np.array_equal(vector, np.arange(10))


def test_create_matrix() -> None:
    """Проверить создание случайной матрицы."""
    matrix = create_matrix()
    assert isinstance(matrix, np.ndarray)
    assert matrix.shape == (5, 5)
    assert np.all((matrix >= 0) & (matrix < 1))


def test_reshape_vector() -> None:
    """Проверить изменение формы вектора."""
    reshaped = reshape_vector(np.arange(10))
    assert reshaped.shape == (2, 5)
    assert reshaped[0, 0] == 0
    assert reshaped[1, 4] == 9


def test_transpose_matrix() -> None:
    """Проверить транспонирование матрицы."""
    matrix = np.array([[1, 2, 3], [4, 5, 6]])
    expected = np.array([[1, 4], [2, 5], [3, 6]])
    assert np.array_equal(transpose_matrix(matrix), expected)


def test_vector_add() -> None:
    """Проверить сложение векторов."""
    assert np.array_equal(
        vector_add(np.array([1, 2, 3]), np.array([4, 5, 6])),
        np.array([5, 7, 9]),
    )


def test_scalar_multiply() -> None:
    """Проверить умножение вектора на скаляр."""
    assert np.array_equal(
        scalar_multiply(np.array([1, 2, 3]), 2),
        np.array([2, 4, 6]),
    )


def test_elementwise_multiply() -> None:
    """Проверить поэлементное умножение."""
    assert np.array_equal(
        elementwise_multiply(
            np.array([1, 2, 3]),
            np.array([4, 5, 6]),
        ),
        np.array([4, 10, 18]),
    )


def test_dot_product() -> None:
    """Проверить скалярное произведение."""
    assert dot_product(np.array([1, 2, 3]), np.array([4, 5, 6])) == 32
    assert dot_product(np.array([2, 0]), np.array([3, 5])) == 6


def test_matrix_multiply() -> None:
    """Проверить матричное умножение."""
    first = np.array([[1, 2], [3, 4]])
    second = np.array([[2, 0], [1, 2]])
    assert np.array_equal(matrix_multiply(first, second), first @ second)


def test_matrix_determinant() -> None:
    """Проверить вычисление определителя."""
    matrix = np.array([[1, 2], [3, 4]])
    assert round(matrix_determinant(matrix), 5) == -2.0


def test_matrix_inverse() -> None:
    """Проверить вычисление обратной матрицы."""
    matrix = np.array([[1, 2], [3, 4]])
    inverse = matrix_inverse(matrix)
    assert np.allclose(matrix @ inverse, np.eye(2))


def test_solve_linear_system() -> None:
    """Проверить решение системы линейных уравнений."""
    coefficients = np.array([[2, 1], [1, 3]])
    constants = np.array([1, 2])
    solution = solve_linear_system(coefficients, constants)
    assert np.allclose(coefficients @ solution, constants)


def test_load_dataset(tmp_path: Path) -> None:
    """Проверить загрузку CSV-файла."""
    csv_path = tmp_path / "test_data.csv"
    csv_path.write_text(
        "math,physics,informatics\n78,81,90\n85,89,88",
        encoding="utf-8",
    )
    data = load_dataset(csv_path)
    assert data.shape == (2, 3)
    assert np.array_equal(data[0], [78, 81, 90])


def test_statistical_analysis() -> None:
    """Проверить статистический анализ."""
    result = statistical_analysis(np.array([10, 20, 30]))
    assert result["mean"] == 20
    assert result["min"] == 10
    assert result["max"] == 30


def test_normalization() -> None:
    """Проверить Min-Max-нормализацию."""
    normalized = normalize_data(np.array([0, 5, 10]))
    assert np.allclose(normalized, np.array([0, 0.5, 1]))
    assert np.array_equal(normalize_data(np.array([5, 5])), [0, 0])


def test_plot_histogram(tmp_path: Path, monkeypatch: Any) -> None:
    """Проверить сохранение гистограммы."""
    monkeypatch.chdir(tmp_path)
    plot_histogram(np.array([1, 2, 3, 4, 5]))
    assert (tmp_path / "plots" / "histogram.png").is_file()


def test_plot_heatmap(tmp_path: Path, monkeypatch: Any) -> None:
    """Проверить сохранение тепловой карты."""
    monkeypatch.chdir(tmp_path)
    matrix = np.array([[1, 0.5], [0.5, 1]])
    plot_heatmap(matrix)
    assert (tmp_path / "plots" / "heatmap.png").is_file()


def test_plot_line(tmp_path: Path, monkeypatch: Any) -> None:
    """Проверить сохранение линейного графика."""
    monkeypatch.chdir(tmp_path)
    plot_line(np.array([1, 2, 3]), np.array([4, 5, 6]))
    assert (tmp_path / "plots" / "line.png").is_file()


if __name__ == "__main__":
    print("Для проверки запустите: python -m pytest LR-2-main-solved.py -v")
