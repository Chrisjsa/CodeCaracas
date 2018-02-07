from django.shortcuts import render_to_response, get_object_or_404
from .models import Autor, Post, Category
from django.http import Http404

max_post = 2


def last_3():
    lp = Post.objects.order_by("-Post_Creation_Date")[:3]
    return lp


def categories():
    return Category.objects.all()


def posts():
    return Post.objects.order_by("-Post_Creation_Date")


def check_max_pages(po):
    max_pages = po.count()/max_post
    return max_pages


def limited(a, b):
    if a > b:
        raise Http404("Página No Encontrada")


def paginate(page, list_post, aux_char, detail):
    if page == 1:
        if page >= check_max_pages(list_post):
            pages = [0, 1, 0, aux_char, detail]
        else:
            pages = [0, 1, 2, aux_char, detail]
    else:
        limited(page-1, check_max_pages(list_post))
        if page >= check_max_pages(list_post):
            pages = [page-1, page, 0, aux_char, detail]
        else:
            pages = [page - 1, page, page + 1, aux_char, detail]
    return pages


def home(request):
    return render_to_response('index.html', {"last": last_3()})


def blog(request):
    pages = paginate(1, posts(), "b", "")
    return render_to_response("blog.html", {"categories": categories(), "posts": posts()[0:max_post], "last": last_3(),
                                            "pages": pages})


def blog_next(request, page):
    a = (page * max_post) - max_post
    b = page * max_post
    pages = paginate(page, posts(), "b", "")
    next_posts = Post.objects.order_by("-Post_Creation_Date")[a:b]
    return render_to_response("blog.html",
                              {"categories": categories(), "posts": next_posts, "last": last_3(), "pages": pages})


def single_post(request, title_post):
    post = Post.objects.get(Post_Title=title_post)
    autor = Autor.objects.get(pk=post.Post_Autor.pk)

    return render_to_response("single-post.html",
                              {"autor": autor, "categories": categories(), "post": post, "last": last_3()})


def post_by_category(request, name_category):
    category = get_object_or_404(Category, Category_Name=name_category)
    posts_cat = category.post_set.order_by("-Post_Creation_Date")
    pages = paginate(1, posts_cat, "c", name_category)
    return render_to_response("blog.html",
                              {"posts": posts_cat[0:max_post], "categories": categories(), "last": last_3(),
                               "pages": pages})


def post_by_category_next(request, name_category, page):
    a = (page * max_post) - max_post
    b = page * max_post
    category = get_object_or_404(Category, Category_Name=name_category)
    next_posts_cat = category.post_set.order_by("-Post_Creation_Date")
    pages = paginate(page, next_posts_cat, "c", name_category)
    return render_to_response("blog.html", {"posts": next_posts_cat[a:b], "categories": categories(), "last": last_3(),
                                            "pages": pages})


def post_by_autor(request, name_autor):
    autors = get_object_or_404(Autor, Autor_Name=name_autor)
    posts_aut = autors.post_set.order_by("-Post_Creation_Date")
    pages = paginate(1, posts_aut, "a", name_autor)
    return render_to_response("blog.html",
                              {"posts": posts_aut[0:max_post], "categories": categories(), "last": last_3(),
                               "pages": pages})


def post_by_autor_next(request, name_autor, page):
    a = (page * max_post) - max_post
    b = page * max_post
    autors = get_object_or_404(Autor, Autor_Name=name_autor)
    next_posts_aut = autors.post_set.order_by("-Post_Creation_Date")
    pages = paginate(page, next_posts_aut, "a", name_autor)
    return render_to_response("blog.html",
                              {"posts": next_posts_aut[a:b], "categories": categories(), "last": last_3(),
                               "pages": pages})
