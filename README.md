## <font style="color:rgb(16, 24, 40);">English</font>
### <font style="color:rgb(16, 24, 40);">Overview</font>
<font style="color:rgb(16, 24, 40);">DataFocus includes two tools, FocusSQL and FocusGPT. FocusSQL is the Hallucination controllable Text2SQL component，FocusGPT is the fast response ChatBI. </font>

# <font style="color:rgb(31, 35, 40);">There are already so many Text-to-SQL frameworks. Why do we still need another one?</font>
<font style="color:rgb(31, 35, 40);">In simple terms, </font><font style="color:rgb(16, 24, 40);">FocusSQL</font><font style="color:rgb(31, 35, 40);"> adopts a two-step SQL generation solution, which enables control over the hallucinations of LLM and truly builds the trust of non-technical users in the generated SQL results.</font>

<font style="color:rgb(31, 35, 40);">Below is the comparison table between </font><font style="color:rgb(16, 24, 40);">FocusSQL</font><font style="color:rgb(31, 35, 40);"> and others:</font>

#### <font style="color:rgb(31, 35, 40);">Comparison Analysis Table</font>
<font style="color:rgb(31, 35, 40);">Here’s a side-by-side comparison of </font><font style="color:rgb(16, 24, 40);">DataFocus plugin</font><font style="color:rgb(31, 35, 40);"> with other LLM-based frameworks:</font>

| **<font style="color:rgb(31, 35, 40);">Feature</font>** | **<font style="color:rgb(31, 35, 40);">Traditional LLM Frameworks</font>** | **<font style="color:rgb(16, 24, 40);">FocusSQL</font>** |
| --- | --- | --- |
| <font style="color:rgb(31, 35, 40);">Generation Process</font> | <font style="color:rgb(31, 35, 40);">Black box, direct SQL generation</font> | <font style="color:rgb(31, 35, 40);">Transparent, two-step (keywords + SQL)</font> |
| <font style="color:rgb(31, 35, 40);">Hallucination Risk</font> | <font style="color:rgb(31, 35, 40);">High, depends on model quality</font> | <font style="color:rgb(31, 35, 40);">Low, controllable (keyword verification)</font> |
| <font style="color:rgb(31, 35, 40);">Speed</font> | <font style="color:rgb(31, 35, 40);">Slow, relies on large model inference</font> | <font style="color:rgb(31, 35, 40);">Fast, deterministic keyword-to-SQL</font> |
| <font style="color:rgb(31, 35, 40);">Cost</font> | <font style="color:rgb(31, 35, 40);">High, requires advanced models</font> | <font style="color:rgb(31, 35, 40);">Low, reduces reliance on large models</font> |
| <font style="color:rgb(31, 35, 40);">Non-Technical User Friendliness</font> | <font style="color:rgb(31, 35, 40);">Low, hard to verify results</font> | <font style="color:rgb(31, 35, 40);">High, easy keyword checking</font> |


<font style="color:rgb(16, 24, 40);"></font>

<font style="color:rgb(16, 24, 40);">The following will introduce how to configure and an example demonstration.</font>

### <font style="color:rgb(16, 24, 40);">1. Apply for DataFocus Token</font>
<font style="color:rgb(16, 24, 40);">If you don't have the DataFocus application yet, please apply for one on the</font><font style="color:rgb(16, 24, 40);"> </font>[<font style="color:rgb(21, 90, 239);">DataFocus Website</font>](https://www.datafocus.ai/en)<font style="color:rgb(16, 24, 40);">.  
</font><font style="color:rgb(16, 24, 40);">Log in to your DataFocus application. Click</font><font style="color:rgb(16, 24, 40);"> </font>**<font style="color:rgb(16, 24, 40);">Admin</font>**<font style="color:rgb(16, 24, 40);"> </font><font style="color:rgb(16, 24, 40);">></font><font style="color:rgb(16, 24, 40);"> </font>**<font style="color:rgb(16, 24, 40);">Interface Authentication</font>**<font style="color:rgb(16, 24, 40);"> </font><font style="color:rgb(16, 24, 40);">></font><font style="color:rgb(16, 24, 40);"> </font>**<font style="color:rgb(16, 24, 40);">Bearer Token</font>**<font style="color:rgb(16, 24, 40);"> </font><font style="color:rgb(16, 24, 40);">></font><font style="color:rgb(16, 24, 40);"> </font>**<font style="color:rgb(16, 24, 40);">New Bearer Token</font>**<font style="color:rgb(16, 24, 40);">, to create a new token and get</font><font style="color:rgb(16, 24, 40);"> </font>_<font style="color:rgb(16, 24, 40);">the token value</font>_<font style="color:rgb(16, 24, 40);">.  
</font>

![](https://cdn.nlark.com/yuque/0/2025/png/28274763/1744714560311-eebf7fed-41f1-46dc-8121-b3401ed97af3.png)

  
If you have a DataFocus private deployment environment, you can get Token on your own environment.

### <font style="color:rgb(16, 24, 40);">2. Fill in the configuration in Dify</font>
<font style="color:rgb(16, 24, 40);">Install DataFocus from Marketplace and fill </font>**<font style="color:rgb(16, 24, 40);">token</font>**<font style="color:rgb(16, 24, 40);"> and </font>**<font style="color:rgb(16, 24, 40);">host</font>**<font style="color:rgb(16, 24, 40);"> in the authorization page.Token is the value obtained in the previous step.If you have a DataFocus private deployment environment, host is your environment host. Otherwise, the SAAS environment address can be used by default.</font>

### <font style="color:rgb(16, 24, 40);">3. Use the tool</font>
<font style="color:rgb(16, 24, 40);">DataFocus includes two tools, FocusSQL and FocusGPT.</font>

#### <font style="color:rgb(16, 24, 40);">FocusSQL</font>
<font style="color:rgb(16, 24, 40);">FocusSQL is a natural language to SQL plugin based on keyword parsing.  
</font>

![](https://cdn.nlark.com/yuque/0/2025/png/28274763/1744714560721-d4fe3afb-7df1-485a-8e19-d88ecd9a7ddd.png)

##### <font style="color:rgb(16, 24, 40);">Output Variable JSON</font>
| **<font style="color:rgb(103, 111, 131);">Name</font>** | **<font style="color:rgb(103, 111, 131);">Type</font>** | **<font style="color:rgb(103, 111, 131);">Description</font>** |
| --- | --- | --- |
| <font style="color:rgb(53, 64, 82);">content</font> | <font style="color:rgb(53, 64, 82);">string</font> | <font style="color:rgb(53, 64, 82);">Generated SQL statements</font> |
| <font style="color:rgb(53, 64, 82);">question</font> | <font style="color:rgb(53, 64, 82);">string</font> | <font style="color:rgb(53, 64, 82);">Generated keywords</font> |
| <font style="color:rgb(53, 64, 82);">type</font> | <font style="color:rgb(53, 64, 82);">string</font> | <font style="color:rgb(53, 64, 82);">Return type</font> |


<font style="color:rgb(16, 24, 40);">Output Example</font>

```plain
JSON



1{
2  "content": "select tbl_1882337315366133767.区域 as col_10715907381350065719,sum(tbl_1882337315366133767.销售数量) as col_9787758666777884439 from string tbl_1882337315366133767 group by tbl_1882337315366133767.区域 order by tbl_1882337315366133767.区域",
3  "question": "区域 销售数量的总和",
4  "type": "sql"
5}
```

#### <font style="color:rgb(16, 24, 40);">FocusGPT</font>
<font style="color:rgb(16, 24, 40);">FocusGPT is an intelligent query plugin that supports multiple rounds of conversations, which allow you query data from your database.  
</font><font style="color:rgb(16, 24, 40);">FocusGPT not only can return query SQL but also return query result to you.  
</font>

![](https://cdn.nlark.com/yuque/0/2025/png/28274763/1744714560442-f54ee0cb-561e-43d4-8bce-17645f2b1a4e.png)

##### <font style="color:rgb(16, 24, 40);">Output Variable JSON</font>
| **<font style="color:rgb(103, 111, 131);">name</font>** | **<font style="color:rgb(103, 111, 131);">type</font>** | **<font style="color:rgb(103, 111, 131);">Description</font>** |
| --- | --- | --- |
| <font style="color:rgb(53, 64, 82);">code</font> | <font style="color:rgb(53, 64, 82);">number</font> | <font style="color:#000000;">Status code</font> |
| <font style="color:rgb(53, 64, 82);">columns</font> | <font style="color:rgb(53, 64, 82);">[[object]]</font> | <font style="color:#000000;">Two-dimensional array storing query results</font> |
| <font style="color:rgb(53, 64, 82);">count</font> | <font style="color:rgb(53, 64, 82);">number</font> | <font style="color:#000000;">Number of rows returned</font> |
| <font style="color:rgb(53, 64, 82);">duration</font> | <font style="color:rgb(53, 64, 82);">string</font> | <font style="color:#000000;">Query execution time, in seconds (s)</font> |
| <font style="color:rgb(53, 64, 82);">headers</font> | <font style="color:rgb(53, 64, 82);">[object]</font> | <font style="color:#000000;">Column header information for the two-dimensional array columns</font> |
| <font style="color:rgb(53, 64, 82);">» display</font> | <font style="color:rgb(53, 64, 82);">string</font> | <font style="color:#000000;">Display name of the column header</font> |
| <font style="color:rgb(53, 64, 82);">» name</font> | <font style="color:rgb(53, 64, 82);">string</font> | <font style="color:#000000;">Original column name of the header</font> |
| <font style="color:rgb(53, 64, 82);">» suf</font> | <font style="color:rgb(53, 64, 82);">string</font> | <font style="color:#000000;">Prefix of the column header, indicating aggregation method</font> |
| <font style="color:rgb(53, 64, 82);">sql</font> | <font style="color:rgb(53, 64, 82);">[object]</font> | <font style="color:#000000;">SQL corresponding to the query data</font> |
| <font style="color:rgb(53, 64, 82);">»select_clause</font> | <font style="color:rgb(53, 64, 82);">string</font> | <font style="color:#000000;">SQL corresponding to the query data</font> |
| <font style="color:rgb(53, 64, 82);">title</font> | <font style="color:rgb(53, 64, 82);">string</font> | <font style="color:#000000;">Keywords generated from parsing</font> |


<font style="color:rgb(16, 24, 40);">Output Example</font>

```plain
JSON



1{
2  "code": 0,
3  "columns": [
4    [
5      "2024-12-01 00:00:00.000",
6      4901
7    ],
8    [
9      "2025-01-01 00:00:00.000",
10      4408
11    ],
12    [
13      "2025-02-01 00:00:00.000",
14      4223
15    ],
16    [
17      "2025-03-01 00:00:00.000",
18      4987
19    ]
20  ],
21  "count": 4,
22  "duration": "0.334571",
23  "headers": [
24    {
25      "display": "订单日期(MONTHLY)",
26      "name": "订单日期",
27      "suf": "MONTHLY"
28    },
29    {
30      "display": "销售数量(SUM)",
31      "name": "销售数量",
32      "suf": "SUM"
33    }
34  ],
35  "sql": {
36    "from_clause": "",
37    "group_by_clause": "",
38    "having_clause": "",
39    "order_by_clause": "",
40    "select_clause": "select date_trunc('month', \"电商销售数据gauss\".\"订单日期\") as col_0,sum(\"电商销售数据gauss\".\"销售数量\") as col_1 from \"电商销售数据gauss\" group by date_trunc('month', \"电商销售数据gauss\".\"订单日期\") order by date_trunc('month', \"电商销售数据gauss\".\"订单日期\")",
41    "where_clause": ""
42  },
43  "title": "每月 销售数量"
44}
```

#### <font style="color:rgb(16, 24, 40);">Configuration</font>
<font style="color:rgb(16, 24, 40);">FocusSQL and FocusGPT have similar configuration. Below are the functions and usage instructions of each parameter</font>

| **<font style="color:rgb(103, 111, 131);">Parameter</font>** | **<font style="color:rgb(103, 111, 131);">Description</font>** |
| --- | --- |
| <font style="color:rgb(53, 64, 82);">Language</font> | <font style="color:rgb(53, 64, 82);">Language environment, only support</font><font style="color:rgb(53, 64, 82);"> </font>_<font style="color:rgb(53, 64, 82);">Chinese</font>_<font style="color:rgb(53, 64, 82);"> </font><font style="color:rgb(53, 64, 82);">and</font><font style="color:rgb(53, 64, 82);"> </font>_<font style="color:rgb(53, 64, 82);">English</font>_ |
| <font style="color:rgb(53, 64, 82);">Query Statement</font> | <font style="color:rgb(53, 64, 82);">Natural language input by users</font> |
| <font style="color:rgb(53, 64, 82);">Table Name</font> | <font style="color:rgb(53, 64, 82);">Target data table for query</font> |
| <font style="color:rgb(53, 64, 82);">Data Model</font> | <font style="color:rgb(53, 64, 82);">Custom model parameter entry</font> |
| <font style="color:rgb(53, 64, 82);">Output SQL Type</font> | <font style="color:rgb(53, 64, 82);">Output SQL Type</font> |
| <font style="color:rgb(53, 64, 82);">Conversation Id</font> | <font style="color:rgb(53, 64, 82);">Unique identifier of the session, which allow tool identify and maintain session state</font> |
| <font style="color:rgb(53, 64, 82);">Action</font> | <font style="color:rgb(53, 64, 82);">The behavior of tool execution currently includes two types: obtaining table lists and dialogues</font> |
| <font style="color:rgb(53, 64, 82);">Datasource Type</font> | <font style="color:rgb(53, 64, 82);">Types of external data sources connected. If datasource type was selected, the connection parameters below need to be filled in</font> |
| <font style="color:rgb(53, 64, 82);">Host</font> | <font style="color:rgb(53, 64, 82);">host</font> |
| <font style="color:rgb(53, 64, 82);">Port</font> | <font style="color:rgb(53, 64, 82);">port</font> |
| <font style="color:rgb(53, 64, 82);">DB user</font> | <font style="color:rgb(53, 64, 82);">user</font> |
| <font style="color:rgb(53, 64, 82);">DB Password</font> | <font style="color:rgb(53, 64, 82);">password</font> |
| <font style="color:rgb(53, 64, 82);">Database Name</font> | <font style="color:rgb(53, 64, 82);">database name</font> |
| <font style="color:rgb(53, 64, 82);">JDBC</font> | <font style="color:rgb(53, 64, 82);">JDBC</font> |
| <font style="color:rgb(53, 64, 82);">Schema</font> | <font style="color:rgb(53, 64, 82);">Schema name</font> |


#### <font style="color:rgb(16, 24, 40);">Model Parameters</font>
<font style="color:rgb(16, 24, 40);">The data model needs to pass in a JSON string, and the structure of the model is as follows</font>

##### <font style="color:rgb(16, 24, 40);">Structure</font>
| **<font style="color:rgb(103, 111, 131);">Name</font>** | **<font style="color:rgb(103, 111, 131);">Type</font>** | **<font style="color:rgb(103, 111, 131);">Required</font>** | **<font style="color:rgb(103, 111, 131);">Description</font>** |
| --- | --- | --- | --- |
| <font style="color:rgb(53, 64, 82);">type</font> | <font style="color:rgb(53, 64, 82);">string</font> | <font style="color:rgb(53, 64, 82);">Yes</font> | <font style="color:rgb(53, 64, 82);">Database type</font> |
| <font style="color:rgb(53, 64, 82);">version</font> | <font style="color:rgb(53, 64, 82);">string</font> | <font style="color:rgb(53, 64, 82);">Yes</font> | <font style="color:rgb(53, 64, 82);">Database version, eg: 8.0</font> |
| <font style="color:rgb(53, 64, 82);">tables</font> | <font style="color:rgb(53, 64, 82);">[object]</font> | <font style="color:rgb(53, 64, 82);">Yes</font> | <font style="color:rgb(53, 64, 82);">Table structure list</font> |
| <font style="color:rgb(53, 64, 82);">» tableDisplayName</font> | <font style="color:rgb(53, 64, 82);">string</font> | <font style="color:rgb(53, 64, 82);">No</font> | <font style="color:rgb(53, 64, 82);">Table display name</font> |
| <font style="color:rgb(53, 64, 82);">» tableName</font> | <font style="color:rgb(53, 64, 82);">string</font> | <font style="color:rgb(53, 64, 82);">No</font> | <font style="color:rgb(53, 64, 82);">Original table name</font> |
| <font style="color:rgb(53, 64, 82);">» columns</font> | <font style="color:rgb(53, 64, 82);">[object]</font> | <font style="color:rgb(53, 64, 82);">No</font> | <font style="color:rgb(53, 64, 82);">Columns structure list</font> |
| <font style="color:rgb(53, 64, 82);">»» columnDisplayName</font> | <font style="color:rgb(53, 64, 82);">string</font> | <font style="color:rgb(53, 64, 82);">Yes</font> | <font style="color:rgb(53, 64, 82);">Column display name</font> |
| <font style="color:rgb(53, 64, 82);">»» columnName</font> | <font style="color:rgb(53, 64, 82);">string</font> | <font style="color:rgb(53, 64, 82);">Yes</font> | <font style="color:rgb(53, 64, 82);">Original column name</font> |
| <font style="color:rgb(53, 64, 82);">»» dataType</font> | <font style="color:rgb(53, 64, 82);">string</font> | <font style="color:rgb(53, 64, 82);">Yes</font> | <font style="color:rgb(53, 64, 82);">Column data type</font> |
| <font style="color:rgb(53, 64, 82);">»» aggregation</font> | <font style="color:rgb(53, 64, 82);">string</font> | <font style="color:rgb(53, 64, 82);">Yes</font> | <font style="color:rgb(53, 64, 82);">Column default aggregation</font> |
| <font style="color:rgb(53, 64, 82);">relations</font> | <font style="color:rgb(53, 64, 82);">[object]</font> | <font style="color:rgb(53, 64, 82);">Yes</font> | <font style="color:rgb(53, 64, 82);">Association relationship list</font> |
| <font style="color:rgb(53, 64, 82);">» conditions</font> | <font style="color:rgb(53, 64, 82);">[object]</font> | <font style="color:rgb(53, 64, 82);">No</font> | <font style="color:rgb(53, 64, 82);">Associated conditions</font> |
| <font style="color:rgb(53, 64, 82);">»» dstColName</font> | <font style="color:rgb(53, 64, 82);">string</font> | <font style="color:rgb(53, 64, 82);">No</font> | <font style="color:rgb(53, 64, 82);">Dimension original column name</font> |
| <font style="color:rgb(53, 64, 82);">»» srcColName</font> | <font style="color:rgb(53, 64, 82);">string</font> | <font style="color:rgb(53, 64, 82);">No</font> | <font style="color:rgb(53, 64, 82);">Fact original column name</font> |
| <font style="color:rgb(53, 64, 82);">» dimensionTable</font> | <font style="color:rgb(53, 64, 82);">string</font> | <font style="color:rgb(53, 64, 82);">No</font> | <font style="color:rgb(53, 64, 82);">Dimension original table name</font> |
| <font style="color:rgb(53, 64, 82);">» factTable</font> | <font style="color:rgb(53, 64, 82);">string</font> | <font style="color:rgb(53, 64, 82);">No</font> | <font style="color:rgb(53, 64, 82);">Fact original table name</font> |
| <font style="color:rgb(53, 64, 82);">» joinType</font> | <font style="color:rgb(53, 64, 82);">string</font> | <font style="color:rgb(53, 64, 82);">No</font> | <font style="color:rgb(53, 64, 82);">Association type</font> |


##### <font style="color:rgb(16, 24, 40);">Parameter values</font>
###### <font style="color:rgb(16, 24, 40);">type</font>
| **<font style="color:rgb(103, 111, 131);">DataBase</font>** | **<font style="color:rgb(103, 111, 131);">Value</font>** |
| --- | --- |
| <font style="color:rgb(53, 64, 82);">MySQL</font> | <font style="color:rgb(53, 64, 82);">mysql</font> |
| <font style="color:rgb(53, 64, 82);">ClickHouse</font> | <font style="color:rgb(53, 64, 82);">clickhouse</font> |
| <font style="color:rgb(53, 64, 82);">Impala</font> | <font style="color:rgb(53, 64, 82);">impala</font> |


###### <font style="color:rgb(16, 24, 40);">dataType</font>
| **<font style="color:rgb(103, 111, 131);">DataType</font>** | **<font style="color:rgb(103, 111, 131);">Value</font>** |
| --- | --- |
| <font style="color:rgb(53, 64, 82);">Boolean</font> | <font style="color:rgb(53, 64, 82);">boolean</font> |
| <font style="color:rgb(53, 64, 82);">Integer</font> | <font style="color:rgb(53, 64, 82);">int</font> |
| <font style="color:rgb(53, 64, 82);">Long integer</font> | <font style="color:rgb(53, 64, 82);">bigint</font> |
| <font style="color:rgb(53, 64, 82);">Float</font> | <font style="color:rgb(53, 64, 82);">double</font> |
| <font style="color:rgb(53, 64, 82);">String</font> | <font style="color:rgb(53, 64, 82);">string</font> |
| <font style="color:rgb(53, 64, 82);">Timestamp</font> | <font style="color:rgb(53, 64, 82);">timestamp</font> |
| <font style="color:rgb(53, 64, 82);">Date type</font> | <font style="color:rgb(53, 64, 82);">date</font> |
| <font style="color:rgb(53, 64, 82);">Time type</font> | <font style="color:rgb(53, 64, 82);">time</font> |


###### <font style="color:rgb(16, 24, 40);">aggregation</font>
| **<font style="color:rgb(103, 111, 131);">Aggregation</font>** | **<font style="color:rgb(103, 111, 131);">Value</font>** |
| --- | --- |
| <font style="color:rgb(53, 64, 82);">Sum</font> | <font style="color:rgb(53, 64, 82);">SUM</font> |
| <font style="color:rgb(53, 64, 82);">Mean</font> | <font style="color:rgb(53, 64, 82);">AVERAGE</font> |
| <font style="color:rgb(53, 64, 82);">Min</font> | <font style="color:rgb(53, 64, 82);">MIN</font> |
| <font style="color:rgb(53, 64, 82);">Max</font> | <font style="color:rgb(53, 64, 82);">MAX</font> |
| <font style="color:rgb(53, 64, 82);">Count</font> | <font style="color:rgb(53, 64, 82);">COUNT</font> |
| <font style="color:rgb(53, 64, 82);">Number of deduplicates</font> | <font style="color:rgb(53, 64, 82);">COUNT_DISTINCT</font> |
| <font style="color:rgb(53, 64, 82);">Variance</font> | <font style="color:rgb(53, 64, 82);">VARIANCE</font> |
| <font style="color:rgb(53, 64, 82);">Standard deviation</font> | <font style="color:rgb(53, 64, 82);">STD_DEVIATION</font> |
| <font style="color:rgb(53, 64, 82);">None</font> | <font style="color:rgb(53, 64, 82);">NONE</font> |


###### <font style="color:rgb(16, 24, 40);">joinType</font>
| **<font style="color:rgb(103, 111, 131);">Assocation</font>** | **<font style="color:rgb(103, 111, 131);">Value</font>** |
| --- | --- |
| <font style="color:rgb(53, 64, 82);">Left association</font> | <font style="color:rgb(53, 64, 82);">LEFT JOIN</font> |
| <font style="color:rgb(53, 64, 82);">Right association</font> | <font style="color:rgb(53, 64, 82);">RIGHT JOIN</font> |
| <font style="color:rgb(53, 64, 82);">Internal</font> | <font style="color:rgb(53, 64, 82);">INNER JOIN</font> |
| <font style="color:rgb(53, 64, 82);">Fully associative</font> | <font style="color:rgb(53, 64, 82);">FULL JOIN</font> |


##### <font style="color:rgb(16, 24, 40);">Example</font>
<font style="color:rgb(16, 24, 40);">model</font>

```plain
JSON



1{
2  "type": "mysql",
3  "version": "8.0",
4  "tables": [
5    {
6      "tableDisplayName": "string",
7      "tableName": "string",
8      "columns": [
9        {
10          "columnDisplayName": null,
11          "columnName": null,
12          "dataType": null,
13          "aggregation": null
14        }
15      ]
16    }
17  ],
18  "relations": [
19    {
20      "conditions": [
21        {
22          "dstColName": null,
23          "srcColName": null
24        }
25      ],
26      "dimensionTable": "string",
27      "factTable": "string",
28      "joinType": "LEFT JOIN"
29    }
30  ]
31}
```

### <font style="color:rgb(16, 24, 40);">Consult</font>
[DataFocus Discord](https://discord.com/invite/AVufPnpaad)

## 中文
---

### 概述
DataFocus 包括两个工具：FocusSQL 和 FocusGPT。FocusSQL 是一个可控制幻觉的 Text2SQL 组件，FocusGPT 是一个快速响应的 ChatBI。

  
已经存在许多 Text-to-SQL 框架，为什么我们还需要另一个？简单来说，FocusSQL 采用两步 SQL 生成解决方案，能够控制大型语言模型（LLM）的幻觉，真正建立非技术用户对生成 SQL 结果的信任。以下是 FocusSQL 与其他框架的比较表：

### 比较分析表
以下是 DataFocus 插件与其他基于 LLM 的Text2SQL框架的比较：

| 功能 | 基于 LLM 框架的组件 | FocusSQL |
| --- | --- | --- |
| 生成过程 | 黑盒，直接生成 SQL | 透明，两步（关键词 + SQL） |
| 幻觉风险 | 高，依赖模型质量 | 低，可控（关键词验证） |
| 速度 | 慢，依赖大型模型推理 | 快，确定性关键词到 SQL |
| 成本 | 高，需要高级模型 | 低，减少对大型模型的依赖 |
| 非技术用户友好性 | 低，难以验证结果 | 好，易于关键词检查 |


以下将介绍如何配置以及示例演示。

### 1. 申请 DataFocus 令牌
如果您还没有 DataFocus 应用程序，请在[ DataFocus 网站](https://www.datafocus.ai/)上申请一个。  
登录您的 DataFocus 应用程序。点击 管理 > 接口认证 > 承载令牌 > 新增 承载令牌，以创建新令牌并获取令牌值。

![](https://cdn.nlark.com/yuque/0/2025/png/28274763/1744714560311-eebf7fed-41f1-46dc-8121-b3401ed97af3.png?x-oss-process=image%2Fformat%2Cwebp)

如果您有 DataFocus 私有部署环境，可以在自己的环境中获取令牌。

### 2. 在 Dify 中填写配置
从 Marketplace 安装 DataFocus，并在授权页面填写令牌和主机地址。令牌是上一步获取的值。如果您有 DataFocus 私有部署环境，主机地址为您的环境主机地址。否则，可以默认使用 SAAS 环境地址。

### 3. 使用工具
DataFocus 包括两个工具：FocusSQL 和 FocusGPT。

#### FocusSQL
FocusSQL 是一个基于关键词解析的自然语言到 SQL 插件。

![](https://cdn.nlark.com/yuque/0/2025/png/28274763/1744716614155-cd8e4fd6-0367-463e-8ad8-a6653a371558.png)

**输出变量 JSON**

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| content | string | 生成的 SQL 语句 |
| question | string | 生成的关键词 |
| type | string | 返回类型 |


**输出示例 JSON**

```json
{
  "content": "select tbl_1882337315366133767.区域 as col_10715907381350065719,sum(tbl_1882337315366133767.销售数量) as col_9787758666777884439 from string tbl_1882337315366133767 group by tbl_1882337315366133767.区域 order by tbl_1882337315366133767.区域",
  "question": "区域 销售数量的总和",
  "type": "sql"
}
```

#### FocusGPT
FocusGPT 是一个支持多轮对话的智能查询插件，允许您从数据库中查询数据。  
FocusGPT 不仅可以返回查询 SQL，还可以返回查询结果。

![](https://cdn.nlark.com/yuque/0/2025/png/28274763/1744716651134-419b3c51-4da2-439a-9289-cc614364cfdc.png)

**输出变量 JSON**

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| code | number | 状态码 |
| columns | [[object]] | 二维数组，存放查询结果 |
| count | number | 返回数据的行数 |
| duration | string | 查询执行耗时，单位秒（s） |
| headers | [object] | 二维数组 columns 对应的列头信息 |
| » display | string | 列头显示名 |
| » name | string | 列头原列名 |
| » suf | string | 列头前缀，标识列的聚合方式 |
| sql | [object] | 查询数据对应的 SQL |
| » select_clause | string | 查询数据对应的 SQL |
| title | string | 解析生成的关键词 |


**输出示例 JSON**

```json
{
  "code": 0,
  "columns": [
    [
      "2024-12-01 00:00:00.000",
      4901
    ],
    [
      "2025-01-01 00:00:00.000",
      4408
    ],
    [
      "2025-02-01 00:00:00.000",
      4223
    ],
    [
      "2025-03-01 00:00:00.000",
      4987
    ]
  ],
  "count": 4,
  "duration": "0.334571",
  "headers": [
    {
      "display": "订单日期(MONTHLY)",
      "name": "订单日期",
      "suf": "MONTHLY"
    },
    {
      "display": "销售数量(SUM)",
      "name": "销售数量",
      "suf": "SUM"
    }
  ],
  "sql": {
    "from_clause": "",
    "group_by_clause": "",
    "having_clause": "",
    "order_by_clause": "",
    "select_clause": "select date_trunc('month', \"电商销售数据gauss\".\"订单日期\") as col_0,sum(\"电商销售数据gauss\".\"销售数量\") as col_1 from \"电商销售数据gauss\" group by date_trunc('month', \"电商销售数据gauss\".\"订单日期\") order by date_trunc('month', \"电商销售数据gauss\".\"订单日期\")",
    "where_clause": ""
  },
  "title": "每月 销售数量"
}
```

### 配置
FocusSQL 和 FocusGPT 的配置类似。以下是每个参数的功能和使用说明：

| 参数 | 描述 |
| --- | --- |
| Language | 语言环境，仅支持中文和英文 |
| Query Statement | 用户输入的自然语言 |
| Table Name | 查询的目标数据表 |
| Data Model | 自定义模型参数入口 |
| Output SQL Type | 输出 SQL 类型 |
| Conversation Id | 会话的唯一标识符，允许工具识别和维护会话状态 |
| Action | 工具执行的行为，目前包括两种类型：获取表列表和对话 |
| Datasource Type | 连接的外部数据源类型。如果选择了数据源类型，需要填写下面的连接参数 |
| Host | 主机地址 |
| Port | 端口 |
| DB user | 数据库用户 |
| DB Password | 数据库密码 |
| Database Name | 数据库名称 |
| JDBC | JDBC |
| Schema | 模式名称 |


### 模型参数
数据模型需要传入 JSON 字符串，模型结构如下：

**结构**

| 名称 | 类型 | 是否必需 | 描述 |
| --- | --- | --- | --- |
| type | string | 是 | 数据库类型 |
| version | string | 是 | 数据库版本，例如：8.0 |
| tables | [object] | 是 | 表结构列表 |
| » tableDisplayName | string | 否 | 表显示名称 |
| » tableName | string | 否 | 原始表名称 |
| » columns | [object] | 否 | 列结构列表 |
| »» columnDisplayName | string | 是 | 列显示名称 |
| »» columnName | string | 是 | 原始列名称 |
| »» dataType | string | 是 | 列数据类型 |
| »» aggregation | string | 是 | 列默认聚合方式 |
| relations | [object] | 是 | 关联关系列表 |
| » conditions | [object] | 否 | 关联条件 |
| »» dstColName | string | 否 | 维度原始列名称 |
| »» srcColName | string | 否 | 事实原始列名称 |
| » dimensionTable | string | 否 | 维度原始表名称 |
| » factTable | string | 否 | 事实原始表名称 |
| » joinType | string | 否 | 关联类型 |


**参数值**

**类型**

| **数据库** | **值** |
| --- | --- |
| MySQL | mysql |
| ClickHouse | clickhouse |
| Impala | impala |


****

**数据类型**

| **数据类型** | **值** |
| --- | --- |
| 布尔值 | boolean |
| 整数 | int |
| 长整数 | bigint |
| 浮点数 | double |
| 字符串 | string |
| 时间戳 | timestamp |
| 日期类型 | date |
| 时间类型 | time |




**聚合方式**

| **聚合方式** | **值** |
| --- | --- |
| 求和 | SUM |
| 平均值 | AVERAGE |
| 最小值 | MIN |
| 最大值 | MAX |
| 计数 | COUNT |
| 去重计数 | COUNT_DISTINCT |
| 方差 | VARIANCE |
| 标准差 | STD_DEVIATION |
| 无 | NONE |


**关联方式**

| **关联方式** | **值** |
| --- | --- |
| 左关联 | LEFT JOIN |
| 右关联 | RIGHT JOIN |
| 内连接 | INNER JOIN |
| 完全关联 | FULL JOIN |


**示例 JSON**

```json
{
  "type": "mysql",
  "version": "8.0",
  "tables": [
    {
      "tableDisplayName": "string",
      "tableName": "string",
      "columns": [
        {
          "columnDisplayName": null,
          "columnName": null,
          "dataType": null,
          "aggregation": null
        }
      ]
    }
  ],
  "relations": [
    {
      "conditions": [
        {
          "dstColName": null,
          "srcColName": null
        }
      ],
      "dimensionTable": "string",
      "factTable": "string",
      "joinType": "LEFT JOIN"
    }
  ]
}
```

### 咨询
![](https://github.com/FocusSearch/focus_mcp_sql/raw/main/wechat-qrcode.png)微信：datafocus2018

---



