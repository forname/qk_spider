# -*- coding: utf-8 -*-

from . import login_manager
from .models.user import User


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



