from django.db import models
from django.utils import timezone # (help: https://docs.djangoproject.com/en/dev/topics/i18n/timezones/)Handles date-time related issues
import datetime # used by datetime.timedelta(days=1)

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __unicode__(self):
        '''Used to return in string format instead of object. When called like
        Question.objects.all()'''
        return (str(self.question_text) +' -- ' +str(self.pub_date))

    def was_published_recently(self):
        '''Returns True if the the pub_date is published within 24 hours or else False.
        usage:
        q = Question.objects.get(id=1)
        q.was_published_recentl()'''
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    

    


class Choice(models.Model):
    '''Usage:
        q = Question(question_text = "What' Up?", pub_date = timezone.now())
        q.choice_set.create(choice_text = "Nothing, learning Django", votes = 0)
        # to display all choices:
        q.choice_set.all()
        # to delete one of the choices
        c = q.choice_set.filter(choice_text__startswith="Nothing")
        c.delete()
    '''
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __unicode__(self):
        '''Will return choice and the votes'''
        return (str(self.choice_text) + str(' -- ') + str(self.votes))

    
