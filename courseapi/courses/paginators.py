from rest_framework import pagination


class ItemPagination(pagination.PageNumberPagination):
    page_size = 10

class TeacherPagination(pagination.PageNumberPagination):
    page_size = 5

class CommentPaginator(pagination.PageNumberPagination):
    page_size = 5