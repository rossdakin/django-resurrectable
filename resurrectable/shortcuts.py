from django.shortcuts import get_object_or_404

def get_nondeleted_or_404(klass, *args, **kwargs):
    return get_object_or_404(klass, deleted=None, *args, **kwargs)
