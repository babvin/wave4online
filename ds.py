import vmrest
import json
vcip = '10.140.99.89'
ds_names = ['A001US046BCN002','A001US046BHD003','A001US046BHD001','A001US046MGT001']
vcsession = vmrest.get_vc_session(vcip,"umeshv@USP01.XSTREAM360.CLOUD","Benaka@18")
for ds_name in ds_names:
    ds = vmrest.get_ds(vcip, ds_name)