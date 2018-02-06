
def test_get_node_locations(statuscake):
    locs = statuscake.get_node_locations()
    assert len(locs) > 0
    assert isinstance(locs, dict)
    assert any(loc['countryiso'] == u'USA' for loc in locs.values())

def test_contact_groups(statuscake):
    assert not any(g['GroupName'] == 'test' for g in statuscake.get_contact_groups())

    statuscake.insert_contact_group({
        'GroupName': 'test',
    })
    groups = statuscake.get_contact_groups()
    assert len(groups) >= 1
    assert any(g['GroupName'] == 'test' for g in groups)
    test_group = next(g for g in groups if g['GroupName'] == 'test')

    statuscake.delete_contact_group(test_group['ContactID'])
    new_groups = statuscake.get_contact_groups()
    assert len(new_groups) == len(groups) - 1
    assert not any(g['GroupName'] == 'test' for g in new_groups)
