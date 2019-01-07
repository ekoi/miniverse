select f.featureddataverse_id, name, alias, affiliation from dataverse as dvn, dataversefeatureddataverse as f where f.dataverse_id=1 and f.featureddataverse_id=dvn.id
