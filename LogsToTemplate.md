- 以 `- 1117838570 2005.06.03 R02-M1-N0-C:J12-U11 2005-06-03-15.42.50.675872 R02-M1-N0-C:J12-U11 RAS KERNEL INFO instruction cache parity error corrected` 这条数据为例

1. 该条数据在structure文件中格式如下：

    |LineId|Label|Timestamp|Date|Node|Time|NodeRepeat|Type|Component|Level|Content|EventId|EventTemplate|
    |------|------|------|------|------|------|------|------|------|------|------|------|------|
    |1|-|1117838570|2005.06.03|R02-M1-N0-C:J12-U11|2005-06-03-15.42.50.675872|R02-M1-N0-C:J12-U11|RAS|KERNEL|INF|instruction cache parity error corrected|E77|instruction cache parity error corrected|

2. 其中 `EventId` 和 `EventTemplate` 是在 `template` 文件中根据 `Content` 内容进行查找得到，对于本条数据中 `Content` 为 `instruction cache parity error corrected` ，从 `template` 文件中就对应 `E77` 和 `instruction cache parity error corrected` .
    >更一般的的情况为带数字的Content，如 `63543 double-hummer alignment exceptions`  ，则 `template` 文件中表示为 `<*> double-hummer alignment exceptions` 即使用 `<*>` 来表示了数字的内容

