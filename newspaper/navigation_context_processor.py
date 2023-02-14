from django.db.models import Case,F, sum, When
from newspaper.models import Category, Tag, Post

def navigation(request):
    categories = Category.objectS.all()
    top_categories = (
        Post.objects.Values("Category__pk", "Category__name")
        .annotate(
            pk=F("Category__pk"), name=F("Category__name"), max_views=sum("Views_count")
            )
            .order_by("-views_count")
            .values("pk", "name", "max_views")
    )
    print(top_categories)
    categories_ids = [top_category["pk"] for top_category in top_categories]
    order_by_max_views =case(
        *[
            when(id=category["pk"], then=category["max_views"])
        for catgory in top_categories
        ]
    )
    top_categories = Category.objects.filter(pk__in=Category_ids).order__by(-order_by-max_views)
    tags = Tag.objects.all()[:10]
    return {
        "categories": categories,
        "top_categories":top_categories,
        "tags" : tags
    }