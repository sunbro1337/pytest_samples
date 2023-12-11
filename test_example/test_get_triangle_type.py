import pytest
import allure
from src_example.main import get_triangle_type, TriangleType

DEBUG_TRIANGLE_CLASS = True


@pytest.fixture()
@allure.title("true_scalene_triangle")
def true_scalene_triangle():
    return 5, 7, 9


@pytest.fixture()
@allure.title("wrong_scalene_triangle")
def wrong_scalene_triangle():
    return 1, 2, 3


@pytest.fixture()
@allure.title("equilateral_triangle")
def equilateral_triangle():
    return 1, 1, 1


@pytest.fixture()
@allure.title("ture_isosceles_triangle")
def ture_isosceles_triangle():
    return 2, 2, 3


@pytest.fixture()
@allure.title("wrong_isosceles_triangle")
def wrong_isosceles_triangle():
    return 2, 2, 4


class TestScaleneTriangle:
    @allure.title("test_scalene_triangle")
    @allure.description("test_scalene_triangle")
    @allure.tag("Smoke")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_isosceles_triangle(self, true_scalene_triangle):
        with allure.step("test_true_scalene_triangle"):
            assert get_triangle_type(
                a=true_scalene_triangle[0],
                b=true_scalene_triangle[1],
                c=true_scalene_triangle[2]
            ) == "scalene"

    @allure.title("test_wrong_scalene_triangle")
    @allure.description("wrong_scalene_triangle")
    @allure.tag("Smoke")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_wrong_triangle(self, wrong_scalene_triangle):
        with allure.step("test_wrong_triangle"):
            assert get_triangle_type(
                a=wrong_scalene_triangle[0],
                b=wrong_scalene_triangle[1],
                c=wrong_scalene_triangle[2]
            ) == "wrong triangle"


class TestEquilateralTriangle:
    @allure.title("test_equilateral_triangle")
    @allure.description("test_equilateral_triangle")
    @allure.tag("Smoke")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_isosceles_triangle(self, equilateral_triangle):
        with allure.step("true_equilateral_triangle"):
            assert get_triangle_type(
                a=equilateral_triangle[0],
                b=equilateral_triangle[1],
                c=equilateral_triangle[2]
            ) == "equilateral"


class TestIsoscelesTriangle:
    @allure.title("test_ture_isosceles_triangle")
    @allure.description("test_ture_isosceles_triangle")
    @allure.tag("Smoke")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_isosceles_triangle(self, ture_isosceles_triangle):
        with allure.step("test_ture_isosceles_triangle"):
            assert get_triangle_type(
                a=ture_isosceles_triangle[0],
                b=ture_isosceles_triangle[1],
                c=ture_isosceles_triangle[2]
            ) == "isosceles"

    @allure.title("test_wrong_isosceles_triangle")
    @allure.description("test_wrong_isosceles_triangle")
    @allure.tag("Smoke")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_wrong_triangle(self, wrong_isosceles_triangle):
        with allure.step("test_wrong_triangle"):
            assert get_triangle_type(
                a=wrong_isosceles_triangle[0],
                b=wrong_isosceles_triangle[1],
                c=wrong_isosceles_triangle[2]
            ) == "wrong triangle"


@pytest.mark.skipif(DEBUG_TRIANGLE_CLASS is False, reason="DEBUG_TRIANGLE_CLASS is False")
class TestTriangleTypeClass:
    @allure.title("test_isosceles_type")
    @allure.description("test_isosceles_type")
    @allure.tag("Smoke")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_triangles_types(self):
        with allure.step("test_isosceles_type"):
            assert TriangleType.isosceles  == "isosceles"
        with allure.step("test_isosceles_type"):
            assert TriangleType.scalene  == "scalene"
        with allure.step("test_isosceles_type"):
            assert TriangleType.equilateral  == "equilateral"
        with allure.step("test_wrong_type"):
            assert TriangleType.wrong == "wrong"
