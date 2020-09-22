select date_trunc('minutes',"collector_tstamp") collector_tstamp,count(*) cnt_event from "atomic"."events" where "collector_tstamp" >= '2020-09-20 00:00:00' group by 1
