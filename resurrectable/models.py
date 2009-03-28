import datetime
from django.db import models

class Resurrectable(object):
    """
    Public methods:
     * delete(self, date_time=datetime.datetime.now(), cascade=True)
     * undelete(self, cascade=True)
    """
    deleted = models.DateTimeField(blank=True, null=True, default=None)

    def _get_children(self):
        return getattr(self.Meta, 'resurrectable_children', [])

    def delete(self, date_time=datetime.datetime.now(), cascade=True):
        if cascade:
            for child in self._get_children():
                child.delete(date_time)
        self.deleted = date_time
        self.save()

    def undelete(self, cascase=True):
        self.deleted = None
        self.save()
        if cascade:
            for child in self._get_children():
                child.undelete()
