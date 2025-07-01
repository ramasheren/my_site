from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound

# Create your views here.

posts = [
    {
        'title': 'Pasta',
        'image': 'blog/images/post1.jpg',
        'content': 'Pasta is a traditional Italian dish made from wheat flour mixed with water or eggs and shaped into various forms. It\'s loved globally for its versatility, from simple spaghetti to creamy fettuccine. Whether tossed in tomato sauce or baked with cheese, pasta is comfort food at its finest.',
        'article': '''Title: Why Pasta Will Always Be My Comfort Food
Author: Rama Sheren

Content:

There's something magical about pasta. Maybe it's the way it swirls around your fork, or how perfectly it holds onto every drop of sauce. From spaghetti to penne, fettuccine to fusilli, pasta comes in so many forms that it's impossible to get bored.

What I love most about pasta is how versatile it is. You can toss it with olive oil and garlic for a quick lunch, or simmer a slow-cooked meat sauce that fills the whole kitchen with warmth. It's the kind of food that feels like a hug — filling, satisfying, and never complicated.

And yes, I have absolutely eaten pasta at 2 AM while debugging code. No regrets.'''   
    },
    {
        'title': 'Pizza',
        'image': 'blog/images/post2.jpg',
        'content': 'Pizza is a popular Italian dish consisting of a usually round, flat base of leavened wheat-based dough topped with tomatoes, cheese, and often various other ingredients (such as anchovies, olives, vegetables, meat, etc.), which is then baked at a high temperature, traditionally in a wood-fired oven.',
        'article': '''Title: The Perfect Pizza: A Slice of Heaven
Author: Rama Sheren

Content:

Pizza is more than just a meal; it's a cultural phenomenon. The perfect pizza starts with a great crust — thin and crispy on the outside, yet soft and chewy on the inside. Then comes the sauce, a simple blend of crushed tomatoes, garlic, and fresh basil, spread generously over the dough.

But the real magic happens with the toppings. Whether you prefer classic mozzarella and pepperoni or more adventurous choices like arugula and prosciutto, each bite should be a harmonious blend of flavors and textures.

And let's not forget the joy of sharing a pizza with friends. There's something about gathering around a hot pie, pulling apart slices, and enjoying each other's company that makes pizza truly special.'''   
    },
    {
        'title': 'Lasagna',
        'image': 'blog/images/post3.jpg',
        'content': 'Lasagna is a classic Italian dish made of layers of pasta, meat, cheese, and tomato sauce. It\'s a hearty and comforting meal that\'s perfect for feeding a crowd.',
        'article': '''Title: Lasagna: The Ultimate Comfort Food
Author: Rama Sheren

Content:

Lasagna is the ultimate comfort food. With its layers of pasta, rich meat sauce, and gooey cheese, it's a dish that brings people together. Whether you're enjoying a slice at a family gathering or savoring leftovers on a cozy night in, lasagna is always a good idea.

One of the best things about lasagna is its versatility. You can stick to the classic recipe or get creative with different ingredients. Want to add some spinach for a pop of color? Go for it! Prefer a white sauce instead of marinara? Why not!

And let's not forget the joy of baking a lasagna. The smell that fills the kitchen as it cooks is enough to make anyone's mouth water. It's a labor of love that pays off with every cheesy, delicious bite.'''
    }
]

def index(request):
    return render(request, "blog/index.html", {"posts": posts})

def post(request, postname):
    postname = postname.lower()
    for post in posts:
        if post['title'].lower() == postname:
            return render(request, "blog/post.html", {"post": post})
    return HttpResponseNotFound("Post not found")
