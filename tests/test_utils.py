from ..utils import Nameable, Taggable, Manager


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



