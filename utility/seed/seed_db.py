from steewi.users.models import User
from steewi.products.models import Product, ProductComment
import random
import factory

names = """Aegnor
Aerin
Aghan
Amandil
Amarië
Amlach
Amras
Amrod
Ancalagon
Andreth
Andróg
Angrim
Angrod
Annael
Ar-Adûnakhôr
Mablung
Maedhros
Maeglin
Maglor
Mahtan
Malach
Mandos
Manwë
Marach
Mardil Voronwë
Melian
Melkor
Meneldil
Morwen
Míriel
Mîm""".split()
password = "secure_password_369"

adj = ['cool', 'mighty', 'new', 'fabulous', 'fantastic', 'the best']
noun_1 = ['bread', 'ham', 'egg', 'milk', 'windshield', 'screen', 'device', 'house']
noun_2 = ['washer', 'cooker', 'cleaner', 'shaker', 'boiler', 'shredder', 'generator']

descr = ["Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed a sollicitudin nulla. Nullam eu placerat turpis, fringilla tincidunt orci. Curabitur mollis mi ante, ut ultricies tellus pellentesque vel. Aenean tristique, augue ut commodo mattis, odio turpis suscipit neque, vel tristique felis lectus quis elit. Vivamus luctus sem lorem, at malesuada est sollicitudin ut. Sed dolor velit, accumsan sed eleifend eget, tincidunt non libero. Quisque vitae mollis neque. Suspendisse venenatis eros dolor, ut suscipit tortor consectetur a.", "Cras a posuere metus. Aliquam suscipit erat velit, vel hendrerit elit tempus sit amet. Praesent iaculis, mi fringilla tincidunt vestibulum, purus urna dignissim tellus, ac suscipit leo mi sed nibh. Sed molestie orci nunc, ut pellentesque lectus luctus nec. Pellentesque rhoncus erat urna. Curabitur blandit quam massa, vitae varius justo auctor ut. Duis vehicula ligula ex, et lacinia risus accumsan in. Integer laoreet lorem eu felis tempor fermentum. Duis finibus cursus nulla, eget maximus mauris ornare id. Etiam viverra cursus efficitur. Pellentesque ac nisi urna. Etiam pellentesque rhoncus magna, vel volutpat lacus efficitur nec.", "Sed vitae volutpat felis. Etiam elementum velit ipsum, in dapibus nunc porttitor non. Proin finibus augue in augue aliquam varius. Curabitur lorem justo, imperdiet at ultrices et, blandit posuere turpis. Fusce euismod ut elit a scelerisque. Praesent convallis iaculis faucibus. Mauris non lacus imperdiet, vestibulum orci sed, mollis magna. Pellentesque vitae sagittis velit. Aenean nisl libero, volutpat a sem sit amet, sollicitudin tempor ligula. Ut scelerisque erat vitae nulla venenatis, nec blandit ante auctor. Mauris faucibus maximus justo. Mauris sit amet est nec felis euismod pretium at ut augue. Fusce venenatis egestas aliquam."]

comments = [
    "Crappy product.", "Garbage. Vaccum broke down within two months of light use.", "Bought this vacuum in May 2016 "
    "and it died two days ago and I used it maybe once a month. It did a decent job picking up the dog hair (and I've got a very furry dog).",
    "Very happy with product, shipping was fast!", "It's a pretty good product but the filters get clogged pretty quick",
    "I love my dirt devil, it is light and very easy to use, I have animals and it works great!",
    "Just got this one and it was DOA amazon sent a refund which was great. Must have just received a dud.",
    "I've had one of these in the past. The first one lasted a couple years! Just got this one and it was DOA amazon sent a refund  which was great.", "I didn't last two months before it stopped working.", "low quality. not worth the money", "Fell apart on the second use. The pet brush worked great round 1. totally failed round 2.",
    "This is a waste of money"]


def gen_product_name():
    name = random.sample(adj, 1) + random.sample(noun_1, 1) + random.sample(noun_2, 1)
    print(name)
    return ' '.join(name)


class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.LazyAttribute(lambda n: ' '.join(random.sample(names, 3)))
    email = factory.LazyAttribute(lambda obj: '%s@some.com' % obj.username)
    is_staff = False
    # is_admin = False
    is_active = True
    password = factory.PostGenerationMethodCall('set_password', password)

class ProductFactory(factory.DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.LazyAttribute(lambda n: gen_product_name())
    slug = factory.LazyAttribute(lambda obj: "-".join(obj.name.split()))
    description = random.sample(descr, 1)[0]
    price = factory.LazyAttribute(lambda obj: random.randint(5, 100))

def create_users(m=10):
    if m > 100:
        print('Too many users requested. Need at most 10. Creating users aborted')
        return
    n = 0
    while n < m:
        try:
            UserFactory.create()
            n += 1
        except Exception as e:
            print(e)
            continue

def create_products(m=10):
    if m > 100:
        print('Too many products requested. Need at most 10. Creating products aborted')
        return
    n = 0
    while n < m:
        try:
            ProductFactory.create()
            n += 1
        except Exception as e:
            print(e)
            continue


def spread_comments(m=20):
    if m > 100:
        print('Too many comments requested. Need at most 100. Commenting aborted')
        return
    products = list(Product.objects.all()[:10])
    if len(products) < 2:
        print('Too few products in db. Need at least 1. Commenting aborted')
        return
    users = list(User.objects.all()[:10])
    if len(users) < 2:
        print('Too few users. Need at least 1. Commenting aborted')
        return
    n = 0
    while n < m:
        com = ProductComment()
        com.product = random.sample(products, 1)[0]
        com.user = random.sample(users, 1)[0]
        com.text = random.sample(comments, 1)[0]
        com.author_name = com.user.username
        com.save()
        n += 1
    n = 0
    while n < m:
        com = ProductComment()
        com.product = random.sample(products, 1)[0]
        com.text = random.sample(comments, 1)[0]
        com.author_name = 'Anon ' + random.sample(names, 1)[0]
        com.save()
        n += 1

def spread_likes():
    products = list(Product.objects.all()[:10])
    if len(products) < 6:
        print('Too few products in db. Need at least 5. Likes aborted')
        return
    users = User.objects.all()[:10]
    if len(users) < 2:
        print('Too few users. Need at least 1. Likes aborted')
        return

    n = 0
    for user in users:
        if n > 100:
            print("Max likes (100) reached")
        for product in random.sample(products, len(products)-2):
            if product.votes.exists(user.id):
                continue
            else:
                product.votes.up(user.id)
                n += 1
    else:
        print("{} likes spreaded".format(n))

def seed_db():
    create_users(10)
    create_products(20)
    spread_comments(20)
    spread_likes()

if __name__ == "__main__":
    seed_db()

