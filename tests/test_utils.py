from ..utils import Nameable, Taggable, Manager
from copy import copy


def populate_manager(m: Manager, obj_list: List[Any]) -> Manager:
    for obj in obj_list:
        m.add(obj)
    return m


def test_utils_Nameable():
    n = Nameable()
    assert n.name == ""
    n = Nameable(None)
    assert n.name == ""
    n.set_name(None)
    assert n.name == ""
    n = Nameable("name")
    assert n.name == "name"
    n.set_name("new_name")
    assert n.name == "new_name"
    n.set_name(None)
    assert n.name == "new_name"
    n.set_name()
    assert n.name == "new_name"


def test_utils_Taggable():
    empty_list = list()
    tags_list = ["tag1", "tag2", "tag3"]
    t = Taggable()
    assert t.tags == empty_list
    t = Taggable(None)
    assert t.tags == empty_list
    t = Taggable([])
    assert t.tags == empty_list
    assert t.has_tags([]) == False
    assert t.has_tag("") == False
    assert t.has_tag() == False
    assert t.has_tag(None) == False
    t = Taggable(tags_list)
    assert t.tags == tags_list
    assert t.has_tags(tags_list) == True
    assert t.has_tags(["tag1"]) == False
    assert t.has_tags(["tag1", "tag2", "tag3", "tag4"]) == False
    assert t.has_tags([]) == False
    assert t.has_tags() == False
    assert t.has_tags(None) == False
    assert t.has_tag("tag1") == True
    assert t.has_tag("tag4") == False
    

def test_utils_Manager_init_add_objects():
    empty_list = list()
    m = Manager()
    assert m.objects() == empty_list
    m = Manager(None)
    assert m.objects() == empty_list
    assert m.add() == False
    assert m.add(None) == False
    assert m.add("") == False
    assert m.add("string") == True
    assert m.add(10) == True
    assert m.add(10.1) == True
    assert m.add(bool()) == False
    assert m.add(tuple()) == False
    assert m.add(dict()) == False
    assert m.add(list()) == False
    assert m.objects() == ["string", 10, 10.1]


def test_utils_Manager_find_at_random():
    m = m = populate_manager(Manager(), ["string", 10, 10.1])
    
    assert m.random() in obj_list

    for idx,obj in enumerate(obj_list):
        assert m.at(idx) == obj
    assert m.at() == None
    assert m.at(None) == None
    assert m.at(4) == None
    assert m.at(-1) == None

    # falta find


def test_utils_Manager_removes():
    obj_list = ["string", 10, 10.1]
    m = populate_manager(Manager(), obj_list)
    m.remove_all()
    assert m.objects == list()

    m = populate_manager(Manager(), obj_list)
    assert m.remove_at(4) == False and m.objects == obj_list
    assert m.remove_at(-1) == False and m.objects == obj_list
    f_list = obj_list.copy()
    f_list.pop(0)
    assert m.remove_at(0) == True and m.objects == f_list
    assert m.remove_at(2) == False and m.objects == obj_list
    assert m.remove_at(None) == False
    assert m.remove_at() == False

    m = populate_manager(Manager(), obj_list)
    f_list = obj_list.copy()
    f_list.pop(0)
    assert m.remove("string") == True and and m.objects == f_list
    assert m.remove("string") == False and m.objects == obj_list
    assert m.remove() == False
    assert m.remove(None) == False
    