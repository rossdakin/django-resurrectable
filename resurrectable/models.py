import datetime
from django.db import models

class ResurrectableQuerySet(models.query.QuerySet):
    def deleted(self):
        return self.exclude(deleted=None)
    def not_deleted(self):
        return self.filter(deleted=None)

class ResurrectableManager(models.Manager):
    use_for_related_fields = True
    def get_query_set(self):
        return ResurrectableQuerySet(self.model)
    def deleted(self):
        return self.get_query_set().deleted()
    def not_deleted(self):
        return self.get_query_set().not_deleted()

class Resurrectable(models.Model):
    """
    Public methods:
     * is_deleted(self)
     * delete(self, date_time=datetime.datetime.now(), cascade=True)
     * undelete(self, cascade=True)
    """
    deleted = models.DateTimeField(blank=True, null=True, default=None,
                                   editable=False, db_index=True,)

    objects = ResurrectableManager()

    class Meta:
        abstract = True

    def get_resurrectable_children(self):
        return ()

    def is_deleted(self):
        return not self.deleted == None

    def delete(self, cascade=True, date_time=datetime.datetime.now()):
        if cascade and False:
            for child in self.get_resurrectable_children():
                child.delete(date_time)
        self.deleted = date_time
        self.save()

    def undelete(self, cascase=True):
        self.deleted = None
        self.save()
        if cascade and False:
            for child in self.get_resurrectable_children():
                child.undelete()
