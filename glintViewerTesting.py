import glintViewer as gv

print ''
print 'Testing Delete Image'
json = [{u'Result':u'Successful Delete', u'Item':u'Image1'}]
headers = [{'header':'Result', 'key':'Result'}, {'header':'Item', 'key':'Item'}]
colum_sizes = [19, 6]
gv.prettyPrint(json, headers, colum_sizes)
print ''

print 'Testing Image Copy'
j1 = [{u'thread_id': 4}]
h1 = [{'header': 'Image Operation Thread id', 'key': 'thread_id'}]
c1 = [25]
gv.prettyPrint(j1,h1,c1)
print ''


print 'Testing List Sites'
j2 =  [{u'name': u'Mosue', u'url': u'http://mouse01.heprc.uvic.ca:5000/v2.0', u'authport': u'5000', u'version': u'v2.0', u'pk': u'1', u'type': u'Openstack'}, {u'name': u'Rateroni', u'url': u'http://rat01.heprc.uvic.ca:5000/v2.0', u'authport': u'5000', u'version': u'v2.0', u'pk': u'2', u'type': u'Openstack'}]
h2 = [{'header': 'Site Name', 'key': 'name'}, {'header': 'Site URL', 'key': 'url'}, {'header': 'Cloud Type', 'key': 'type'}] 
c2 = [9, 38, 10]
gv.prettyPrint(j2,h2,c2)
print ''

print 'Testing Get Credential'
j3 = [{u'tenant': u'HEP', u'cred_id': u'rd'}]
h3 = [{'header': 'Credential id', 'key': 'cred_id'}, {'header': 'Tenant Name', 'key': 'tenant'}]
c3 = [13, 11]
gv.prettyPrint(j3,h3,c3)
print ''

print 'Testing Has Credential'
j4 = [{u'result': True, u'error': False}]
h4 = [{'header': 'Result of Operation', 'key': 'result'}]
c4 = [19]
gv.prettyPrint(j4,h4,c4)
print ''

print 'Testing Delete Credential'
j5 = [{u'Result': u'Success removing Credential'}]
h5 = [{'header': 'Result of Operation', 'key': 'Result'}]
c5 = [27]
gv.prettyPrint(j5,h5,c5)
print ''

print 'Testing Add Credential'
j6 = [{u'Result': u'Sites: add Credential'}]
h6 = [{'header': 'Result of Operation', 'key': 'Result'}]
c6 = [21]
gv.prettyPrint(j6,h6,c6)
print ''

print 'Testing Delete Site'
j7 = [{u'Result': u'Successful Delete'}]
h7 = [{'header': 'Result of Operation', 'key': 'Result'}]
c7 = [19]
gv.prettyPrint(j7,h7,c7)
print ''

print 'Testing Create Site'
j8 = [{u'site_id': 2, u'Result': u'Success'}]
h8 = [{'header': 'Result of Operation', 'key': 'Result'}, {'header': 'site id', 'key': 'site_id'}]
c8 = [19, 7]
gv.prettyPrint(j8,h8,c8)
print ''

print 'Testing Get Images'
j9 =  {u'rows': [{u'container_format': u'bare', u'image': u'tinyvm', u'disk_format': u'qcow2', u'sites': [{u'is_public': u'False', u'tenent': u'glinttenant', u'is_owner': u'True', u'name': u'TestSite'}]}, {u'container_format': u'bare', u'image': u'CentOS 7 x86_64 QCOW', u'disk_format': u'qcow2', u'sites': [{u'is_public': u'False', u'tenent': u'glinttenant', u'is_owner': u'True', u'name': u'TestSite'}]}, {u'container_format': u'bare', u'image': u'Cirros 2', u'disk_format': u'qcow2', u'sites': [{u'is_public': u'False', u'tenent': u'glinttenant', u'is_owner': u'True', u'name': u'TestSite'}]}, {u'container_format': u'bare', u'image': u'cirros-0.3.3-x86_64', u'disk_format': u'qcow2', u'sites': [{u'is_public': u'True', u'tenent': u'glinttenant', u'is_owner': u'False', u'name': u'TestSite'}]}, {u'container_format': u'bare', u'image': u'Ubuntu 12.04 Precise', u'disk_format': u'qcow2', u'sites': [{u'is_public': u'True', u'tenent': u'testing', u'is_owner': u'True', u'name': u'Mosue'}]}, {u'container_format': u'bare', u'image': u'mjmc-htc-test-node', u'disk_format': u'qcow2', u'sites': [{u'is_public': u'False', u'tenent': u'testing', u'is_owner': u'True', u'name': u'Mosue'}]}, {u'container_format': u'bare', u'image': u'Ubuntu-14_04-Trusty', u'disk_format': u'qcow2', u'sites': [{u'is_public': u'False', u'tenent': u'testing', u'is_owner': u'True', u'name': u'Mosue'}]}, {u'container_format': u'bare', u'image': u'mjmc-htc/cs-base', u'disk_format': u'qcow2', u'sites': [{u'is_public': u'False', u'tenent': u'testing', u'is_owner': u'True', u'name': u'Mosue'}]}, {u'container_format': u'bare', u'image': u'Fedora-21', u'disk_format': u'qcow2', u'sites': [{u'is_public': u'False', u'tenent': u'testing', u'is_owner': u'True', u'name': u'Mosue'}]}, {u'container_format': u'bare', u'image': u'fedora-image', u'disk_format': u'qcow2', u'sites': [{u'is_public': u'False', u'tenent': u'testing', u'is_owner': u'True', u'name': u'Mosue'}]}, {u'container_format': u'bare', u'image': u'CentOS 7', u'disk_format': u'qcow2', u'sites': [{u'is_public': u'False', u'tenent': u'testing', u'is_owner': u'True', u'name': u'Mosue'}]}, {u'container_format': u'bare', u'image': u'shoal-demo-test', u'disk_format': u'qcow2', u'sites': [{u'is_public': u'False', u'tenent': u'testing', u'is_owner': u'True', u'name': u'Mosue'}]}, {u'container_format': u'bare', u'image': u'mjmc-test-3', u'disk_format': u'qcow2', u'sites': [{u'is_public': u'False', u'tenent': u'testing', u'is_owner': u'True', u'name': u'Mosue'}]}, {u'container_format': u'bare', u'image': u'mjmc-two', u'disk_format': u'qcow2', u'sites': [{u'is_public': u'False', u'tenent': u'testing', u'is_owner': u'True', u'name': u'Mosue'}]}, {u'container_format': u'bare', u'image': u'ucernvm-prod.1.18-13', u'disk_format': u'raw', u'sites': [{u'is_public': u'True', u'tenent': u'testing', u'is_owner': u'False', u'name': u'Mosue'}]}, {u'container_format': u'bare', u'image': u'centos6-bare', u'disk_format': u'qcow2', u'sites': [{u'is_public': u'True', u'tenent': u'testing', u'is_owner': u'False', u'name': u'Mosue'}]}, {u'container_format': u'bare', u'image': u'ubuntu-ec2-sps-x', u'disk_format': u'qcow2', u'sites': [{u'is_public': u'True', u'tenent': u'testing', u'is_owner': u'False', u'name': u'Mosue'}]}, {u'container_format': u'bare', u'image': u'ucernvm-prod.1.18-10', u'disk_format': u'raw', u'sites': [{u'is_public': u'True', u'tenent': u'testing', u'is_owner': u'False', u'name': u'Mosue'}, {u'is_public': u'False', u'tenent': u'testing', u'is_owner': u'True', u'name': u'Mosue'}]}, {u'container_format': u'bare', u'image': u'cernvm-mouse.fix03', u'disk_format': u'qcow2', u'sites': [{u'is_public': u'True', u'tenent': u'testing', u'is_owner': u'False', u'name': u'Mosue'}]}, {u'container_format': u'bare', u'image': u'fedora', u'disk_format': u'qcow2', u'sites': [{u'is_public': u'True', u'tenent': u'testing', u'is_owner': u'False', u'name': u'Mosue'}]}], u'sites': [{u'tenent': u'glinttenant', u'name': u'TestSite'}, {u'tenent': u'testing', u'name': u'Mosue'}]} 
h9 = [{'header': 'Name', 'key': 'image'}]
#h9 = [{'header': 'Name', 'key': 'image'}, {'header': u'TestSite'}, {'header': u'Mosue'}] 
c9 = [20]
#c9 = [20, 8, 5]
gv.prettyPrint(j9['rows'],h9,c9)
print ''

