from django.db import models,connection
from django.contrib import admin

# Create your models here.
class loftk_articlesManager(models.Manager):
	def title_count(self,keyword):
		return self.filter(title__icontains=keyword).count()
	
	def getlist(self):
		cursor = connection.cursor()
		cursor.execute("select * from mysiteapp_loftk_articles  as a join mysiteapp_loftk_newtype as t on a.newtype=t.id order by a.id desc")
		
		return cursor.fetchall()
	   
		#return [row[1] for row in cursor.fetchall()]
"""
class Author(models.Model):
	name = models.CharField(max_length=20)
	address = models.CharField(max_length=20)
	enname = models.CharField(max_length=20)
"""
class loftk_articles(models.Model):
	list_display=('newtitle','author','fstcreate')
	#id = models.IntegerField()
	newtitle = models.CharField(max_length=100)
	newcontent = models.TextField()
	author = models.CharField(max_length=100)
	#image = models.CharField(max_length=100)
	fstcreate = models.DateTimeField()
	lastmodify = models.DateTimeField()
	isdel = models.IntegerField()
	newtype = models.IntegerField()

	objects = models.Manager()
	loftk_articles_objects = loftk_articlesManager()
	
	def __unicode__(self):
		return self.newtitle

admin.site.register(loftk_articles)
		
class loftk_newtype(models.Model):
	typename = models.CharField(max_length=100)

	def __unicode__(self):
		return self.typename

admin.site.register(loftk_newtype)

class user(models.Model):
	username = models.CharField(max_length=250)
	password = models.CharField(max_length=200)


class UserAdmin(admin.ModelAdmin):
    list_display = ('username','password')

	
class userrole(models.Model):
	user = models.ForeignKey(user)
	rolename = models.CharField(max_length=250)
	
class role(models.Model):
	userrole = models.ForeignKey(userrole)
	roles = models.CharField(max_length=200)

class Person(models.Model):
	 name = models.CharField('作者姓名', max_length=10)  
	 age = models.IntegerField('作者年龄')  
	
"""
class Book(models.Model):  
	person = models.ForeignKey(Person)  
	title = models.CharField('书籍名称', max_length=10)  
	pubtime = models.DateField('出版时间')  
"""
class Meta:
	app_label = ''
	

