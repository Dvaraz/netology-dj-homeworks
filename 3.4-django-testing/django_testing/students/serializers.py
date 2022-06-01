from django.db.models import Count
from rest_framework import serializers

from students.models import Course


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ("id", "name", "students")

    # def validate(self, data):
    #     students = Course.objects.filter(id=self.instance.id).annotate(num_students=Count('students'))
    #     if students[0].num_students >= 20 and (self.context["request"].method == 'POST' or len(data['students']) > 0):
    #         raise serializers.ValidationError('Can be only 20 students per course')
    #     return data
