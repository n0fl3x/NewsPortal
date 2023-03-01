from django_filters import (
    FilterSet, ModelMultipleChoiceFilter, DateFilter, CharFilter)
from django.forms import DateInput

from .models import *


class PostsFilter(FilterSet):

    title = CharFilter(
        field_name='title',
        lookup_expr='icontains',
        label='Title or part of it',

    )

    category = ModelMultipleChoiceFilter(
        field_name='postcategory__category_through',
        queryset=Category.objects.all(),
        label='Category',
        conjoined=True,
    )

    date_of_creation = DateFilter(
        field_name='date_of_creation',
        lookup_expr='gte',
        label='Posted on date or later',
        widget=DateInput(
            format='%d.%m.%Y',
            attrs={'type': 'date'},
        ),
    )
