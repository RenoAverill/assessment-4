from categories.models import Category, Post
import categories

cat1 = Category(name='outdoors')
cat1.save()
cat2 = Category(name='cars')
cat2.save()
cat3 = Category(name='animals')
cat3.save()
cat4 = Category(name='jobs')
cat4.save()

post1 = Post(item='tent',
             detail='this is my orange tent',
             category=cat1
             )
post1.save()

post2 = Post(item='2008 subaru',
             detail='black, beat up, subi',
             category=cat2
             )
post2.save()

post3 = Post(item='pig',
             detail='this is my fat piggy',
             category=cat3
             )
post3.save()

post4 = Post(item='Software Dev',
             detail='Filling a Code Platoon Dev postition',
             category=cat3
             )
post4.save()
