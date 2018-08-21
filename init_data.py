# This file cannot run standalone 
# Must be called by init_db.sh 
from whip.models import Criteria, Post, Bid

# Criteria for Age profolio 
Criteria(key="Age Profile",value="0-10").save()
Criteria(key="Age Profile",value="10-18").save()
Criteria(key="Age Profile",value="18-30").save()
Criteria(key="Age Profile",value="30-40").save()
Criteria(key="Age Profile",value="40-50").save()
Criteria(key="Age Profile",value="50-60").save()
Criteria(key="Age Profile",value="60-80").save()
Criteria(key="Age Profile",value="80-100").save()
