import glintViewer as gv

json = [{u'Result':u'Successful Delete', u'Item':u'Image1'}, {u'Result':u'Unsuccessful Delete', u'Item':u'Image2'}]
headers = [{'header':'Result', 'key':'Result'}, {'header':'Item', 'key':'Item'}]
colum_sizes = [19,6]

gv.prettyPrint(json, headers, colum_sizes)


