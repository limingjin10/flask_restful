#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: inventory.py
@time: 2018-06-28 00:23
"""

import datetime

from libs.mysql_orm_op import DbInstance
from web_api.databases.bearings import db
from web_api.models.bearings import Inventory

db_instance = DbInstance(db)


def get_inventory_row_by_id(inventory_id):
    """
    通过 id 获取信息
    :param inventory_id:
    :return: None/object
    """
    return db_instance.get_row_by_id(Inventory, inventory_id)


def get_inventory_row(*args, **kwargs):
    """
    获取信息
    :param args:
    :param kwargs:
    :return: None/object
    """
    return db_instance.get_row(Inventory, *args, **kwargs)


def get_inventory_rows(*args, **kwargs):
    """
    获取列表
    :param args:
    :param kwargs:
    :return:
    """
    return db_instance.get_rows(Inventory, *args, **kwargs)


def get_inventory_limit_rows_by_last_id(last_pk, limit_num, *args, **kwargs):
    """
    通过最后一个主键 id 获取最新信息列表
    :param last_pk:
    :param limit_num:
    :param args:
    :param kwargs:
    :return:
    """
    return db_instance.get_limit_rows_by_last_id(Inventory, last_pk, limit_num, *args, **kwargs)


def add_inventory(inventory_data):
    """
    添加信息
    :param inventory_data:
    :return: None/Value of user.id
    :except:
    """
    return db_instance.add(Inventory, inventory_data)


def edit_inventory(inventory_id, inventory_data):
    """
    修改信息
    :param inventory_id:
    :param inventory_data:
    :return: Number of affected rows (Example: 0/1)
    :except:
    """
    return db_instance.edit(Inventory, inventory_id, inventory_data)


def delete_inventory(inventory_id, force=False):
    """
    删除信息
    :param inventory_id:
    :param force:
    :return: Number of affected rows (Example: 0/1)
    :except:
    """
    if force:
        return db_instance.delete(Inventory, inventory_id)
    else:
        data = {
            'status_delete': True,
            'delete_time': datetime.datetime.utcnow()
        }
        return db_instance.edit(Inventory, inventory_id, data)


def get_inventory_pagination(page=1, per_page=10, *args, **kwargs):
    """
    获取列表（分页）
    Usage:
        items: 信息列表
        has_next: 如果本页之后还有超过一个分页，则返回True
        has_prev: 如果本页之前还有超过一个分页，则返回True
        next_num: 返回下一页的页码
        prev_num: 返回上一页的页码
        iter_pages(): 页码列表
        iter_pages(left_edge=2, left_current=2, right_current=5, right_edge=2) 页码列表默认参数
    :param page:
    :param per_page:
    :param args:
    :param kwargs:
    :return:
    """
    rows = db_instance.get_pagination(Inventory, page, per_page, *args, **kwargs)
    return rows


def delete_inventory_table():
    """
    清空表
    :return:
    """
    return db_instance.delete_table(Inventory)


def count_inventory(*args, **kwargs):
    """
    计数
    :param args:
    :param kwargs:
    :return:
    """
    return db_instance.count(Inventory, *args, **kwargs)
