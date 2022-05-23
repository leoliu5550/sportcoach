import pickledb
# https://patx.github.io/pickledb/commands.html

db = pickledb.load('example.db', True)
db.set('key', 'value')
db.set('key2', 'value2')
db.set('key3', 'value3')
db.append('key','001')
print(db.totalkeys())

# db.dump()