from .median_of_2_sorted_arrays import Solution
import pytest


@pytest.fixture
def setup_envt():
    print("making a Solution object")
    return Solution()


def test_median_value_2(setup_envt):
    solution=setup_envt
    list_1=[1,3]
    list_2=[2]
    assert setup_envt.findMedianSortedArrays(list_1,list_2) == 2.0

def test_median_value_2_point_5(setup_envt):

    list_1=[1,2]
    list_2=[3,4]
    assert setup_envt.findMedianSortedArrays(list_1,list_2) == 2.5