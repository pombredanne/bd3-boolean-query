from discodb import DiscoDB
from bitdeli.model import model


MAX_LEN = 64

@model
def items(profiles):
    keys = set()
    for profile in profiles:
        uid = profile.uid
        if not uid:
            continue
        for event in profile['events']:
            event = event.encode('utf-8')
            yield event, uid
            keys.add('e:' + event)
        for prop_name, prop_values in profile['properties'].iteritems():
            prop_name = prop_name.encode('utf-8') 
            keys.add('p:' + prop_name)
            for v in frozenset(prop_value[:MAX_LEN] for prop_value in prop_values):
                yield '%s:%s' % (prop_name, v.encode('utf-8')), uid
    for key in keys:
        yield ' ', key
