import pytest
from rest_framework.test import APIClient
from model_bakery import baker

from students.models import Course, Student


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)
    return factory


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return factory


@pytest.mark.django_db
def test_get_course(client, student_factory, course_factory):
    # Arrange
    courses = course_factory(_quantity=3)
    course_id = courses[0].id

    # Act
    response = client.get(f'/api/v1/courses/{course_id}/')

    # Assert
    assert response.status_code == 200
    assert response.data['id'] == courses[0].id


@pytest.mark.django_db
def test_get_courses(client, student_factory, course_factory):
    # Arrange
    courses = course_factory(_quantity=3)

    # Act
    response = client.get('/api/v1/courses/')
    data = response.data

    # Assert
    assert response.status_code == 200
    assert len(data) == len(courses)
    for i, c in enumerate(data):
        assert c['name'] == courses[i].name


@pytest.mark.django_db
def test_filter_courses(client, student_factory, course_factory):
    # Arrange
    courses = course_factory(_quantity=3)
    name = courses[0].name
    course_id = courses[0].id

    # Act
    response_id = client.get(f'/api/v1/courses/?id={course_id}')
    response_name = client.get(f'/api/v1/courses/?name={name}')

    # Assert
    assert response_id.status_code == 200
    assert response_id.data[0]['name'] == name
    assert response_name.status_code == 200
    assert response_name.data[0]['id'] == course_id


@pytest.mark.django_db
def test_create_course(client):
    # Arrange
    count = Course.objects.count()

    # Act
    response = client.post('/api/v1/courses/', data={'id': 1, 'name': 'test_name'})

    # Assert
    assert response.status_code == 201
    assert Course.objects.count() == count + 1


@pytest.mark.django_db
def test_patch_course(client, student_factory, course_factory):
    # Arrange
    courses = course_factory(_quantity=10)
    course_id = courses[0].id

    # Act
    response = client.patch(f'/api/v1/courses/{course_id}/', data={'name': 'test_name'})

    # Assert
    assert response.status_code == 200
    assert response.data['name'] == 'test_name'


@pytest.mark.django_db
def test_delete_course(client, student_factory, course_factory):
    # Arrange
    courses = course_factory(_quantity=10)
    count = Course.objects.count()
    course_id = courses[0].id

    # Act
    response = client.delete(f'/api/v1/courses/{course_id}/')

    # Assert
    assert response.status_code == 204
    assert Course.objects.count() == count - 1
