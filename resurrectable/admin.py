class ResurrectableAdmin(object):

    def is_deleted(self, object):
        return object.is_deleted()
    is_deleted.boolean = True
    is_deleted.short_description = "Deleted"

    def not_deleted(self, object):
        return not object.is_deleted()
    not_deleted.boolean = True
    not_deleted.short_description = "Not deleted"
