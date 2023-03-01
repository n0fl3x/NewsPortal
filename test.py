from random import randint, choice


# categories = ['Sport', 'IT', 'Politics', 'Family', 'Cars', 'Hobby', 'kekW']
# for i in range(len(categories)):
#     iter_name = choice(categories)
#     print(f"""category_{i+1} = Category.objects.create(name = "{iter_name}")""")
#     categories.remove(iter_name)


# for i in range(1,8):
#     print(f"""author_{i} = Author.objects.create(author_user = user_{i})""")


# post_types = ['NWS', 'ART']
# for i in range(1, 121):
#     _type = choice(post_types)
#     print(f"""Post.objects.create(author_of_post = author_{randint(1, 7)},
#     post_type = '{_type}', title = "Some {'news' if _type == 'NWS' else 'article'} #{i}",
#     text = "Some {'news' if _type == 'NWS' else 'article'} #{i} big text.")""")


# for i in range(3, 114):
#     print(f"""Post.objects.get(pk={i}).post_category.add(category_{randint(1, 7)})""")
