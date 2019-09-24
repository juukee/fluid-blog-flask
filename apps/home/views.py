# -*- coding:utf-8 -*-

from flask import (
    Blueprint,
    views,
    render_template,
    request,
    session,
    redirect,
    url_for,
    g,
    jsonify
)
from .models import (
    BlogModel
)
import os
import config
from exts import db, mail
<<<<<<< HEAD
from flask_paginate import Pagination, get_page_parameter

=======
import config
>>>>>>> 6785aa67444291839bbc082906fda32673f26263
home = Blueprint('home', __name__)


@home.route('/')
@home.route('/index')
def index():
    # filename = os.path.join(home.root_path, '../public','index.html')
    # print(filename)
    # with open(filename,'w') as f:
    #     f.write(str(render_template('home/index.html')))
    #     f.close()
    page = request.args.get(get_page_parameter(),type=int,default=1)
    start = (page - 1) * config.PER_PAGE
    end = start + config.PER_PAGE
    total = BlogModel.query.filter().count()
    # print(total)
    pagination = Pagination(page=page,start=start,end=end,total=total)
    # db.create_all()
    # data = BlogModel('你好','Juukee')
    # db.session.add(data)
    # db.session.commit()
    return render_template('home/index.html',pagination=pagination)


@home.route('/archives')
def archives():
    return render_template('home/archives.html')


@home.route('/tags')
def tags():
    return render_template('home/tags.html')


@home.route('/about')
def about():
    return render_template('home/about.html')


@home.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html',), 404
