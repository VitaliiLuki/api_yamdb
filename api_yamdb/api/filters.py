import django_filters

from reviews.models import Title


class TitleFilter(django_filters.FilterSet):
    """
    Gives an option to filtrate the fields below when you make a get-request 
    to find a title which matches to your search.
    """
    category = django_filters.CharFilter(field_name='category__slug')
    genre = django_filters.CharFilter(field_name='genre__slug')
    name = django_filters.CharFilter(
        field_name='name', lookup_expr='icontains')
    year = django_filters.CharFilter(field_name='year')

    class Meta:
        model = Title
        fields = ['name', 'year', 'genre', 'category']
