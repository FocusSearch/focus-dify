## English
### Overview
DataFocus includes two tools, FocusSQL and FocusGPT. FocusSQL is the Hallucination controllable Text2SQL component，FocusGPT is the fast response ChatBI. 

### There are already so many Text-to-SQL frameworks. Why do we still need another one?
In simple terms, FocusSQL adopts a two-step SQL generation solution, which enables control over the hallucinations of LLM and truly builds the trust of non-technical users in the generated SQL results.

Below is the comparison table between FocusSQL and others:

#### Comparison Analysis Table
Here’s a side-by-side comparison of DataFocus plugin with other LLM-based frameworks:

| **Feature** | **Traditional LLM Frameworks** | **FocusSQL** |
| --- | --- | --- |
| Generation Process | Black box, direct SQL generation | Transparent, two-step (keywords + SQL) |
| Hallucination Risk | High, depends on model quality | Low, controllable (keyword verification) |
| Speed | Slow, relies on large model inference | Fast, deterministic keyword-to-SQL |
| Cost | High, requires advanced models | Low, reduces reliance on large models |
| Non-Technical User Friendliness | Low, hard to verify results | High, easy keyword checking |




The following will introduce how to configure and an example demonstration.

### 1. Apply for DataFocus Token
If you don't have the DataFocus application yet, please apply for one on the [DataFocus Website](https://www.datafocus.ai/en).  
Log in to your DataFocus application. Click **Admin** > **Interface Authentication** > **Bearer Token** > **New Bearer Token**, to create a new token and get _the token value_.  


![](https://cdn.nlark.com/yuque/0/2025/png/28274763/1744714560311-eebf7fed-41f1-46dc-8121-b3401ed97af3.png)

  
If you have a DataFocus private deployment environment, you can get Token on your own environment.

### 2. Fill in the configuration in Dify
Install DataFocus from Marketplace and fill **token** and **host** in the authorization page.Token is the value obtained in the previous step.If you have a DataFocus private deployment environment, host is your environment host. Otherwise, the SAAS environment address can be used by default.

### 3. Use the tool
DataFocus includes two tools, FocusSQL and FocusGPT.

#### FocusSQL
FocusSQL is a natural language to SQL plugin based on keyword parsing.  


![](https://cdn.nlark.com/yuque/0/2025/png/28274763/1744714560721-d4fe3afb-7df1-485a-8e19-d88ecd9a7ddd.png)

##### Output Variable JSON
| **Name** | **Type** | **Description** |
| --- | --- | --- |
| content | string | Generated SQL statements |
| question | string | Generated keywords |
| type | string | Return type |


Output Example

```plain
JSON



1{
2  "content": "select tbl_1882337315366133767.区域 as col_10715907381350065719,sum(tbl_1882337315366133767.销售数量) as col_9787758666777884439 from string tbl_1882337315366133767 group by tbl_1882337315366133767.区域 order by tbl_1882337315366133767.区域",
3  "question": "区域 销售数量的总和",
4  "type": "sql"
5}
```

#### FocusGPT
FocusGPT is an intelligent query plugin that supports multiple rounds of conversations, which allow you query data from your database.  
FocusGPT not only can return query SQL but also return query result to you.  


![](https://cdn.nlark.com/yuque/0/2025/png/28274763/1744714560442-f54ee0cb-561e-43d4-8bce-17645f2b1a4e.png)

##### Output Variable JSON
| **name** | **type** | **Description** |
| --- | --- | --- |
| code | number | Status code |
| columns | [[object]] | Two-dimensional array storing query results |
| count | number | Number of rows returned |
| duration | string | Query execution time, in seconds (s) |
| headers | [object] | Column header information for the two-dimensional array columns |
| » display | string | Display name of the column header |
| » name | string | Original column name of the header |
| » suf | string | Prefix of the column header, indicating aggregation method |
| sql | [object] | SQL corresponding to the query data |
| »select_clause | string | SQL corresponding to the query data |
| title | string | Keywords generated from parsing |


Output Example

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

#### Configuration
FocusSQL and FocusGPT have similar configuration. Below are the functions and usage instructions of each parameter

| **Parameter** | **Description** |
| --- | --- |
| Language | Language environment, only support _Chinese_ and _English_ |
| Query Statement | Natural language input by users |
| Table Name | Target data table for query |
| Data Model | Custom model parameter entry |
| Output SQL Type | Output SQL Type |
| Conversation Id | Unique identifier of the session, which allow tool identify and maintain session state |
| Action | The behavior of tool execution currently includes two types: obtaining table lists and dialogues |
| Datasource Type | Types of external data sources connected. If datasource type was selected, the connection parameters below need to be filled in |
| Host | host |
| Port | port |
| DB user | user |
| DB Password | password |
| Database Name | database name |
| JDBC | JDBC |
| Schema | Schema name |


#### Model Parameters
The data model needs to pass in a JSON string, and the structure of the model is as follows

##### Structure
| **Name** | **Type** | **Required** | **Description** |
| --- | --- | --- | --- |
| type | string | Yes | Database type |
| version | string | Yes | Database version, eg: 8.0 |
| tables | [object] | Yes | Table structure list |
| » tableDisplayName | string | No | Table display name |
| » tableName | string | No | Original table name |
| » columns | [object] | No | Columns structure list |
| »» columnDisplayName | string | Yes | Column display name |
| »» columnName | string | Yes | Original column name |
| »» dataType | string | Yes | Column data type |
| »» aggregation | string | Yes | Column default aggregation |
| relations | [object] | Yes | Association relationship list |
| » conditions | [object] | No | Associated conditions |
| »» dstColName | string | No | Dimension original column name |
| »» srcColName | string | No | Fact original column name |
| » dimensionTable | string | No | Dimension original table name |
| » factTable | string | No | Fact original table name |
| » joinType | string | No | Association type |


##### Parameter values
###### type
| **DataBase** | **Value** |
| --- | --- |
| MySQL | mysql |
| ClickHouse | clickhouse |
| Impala | impala |


###### dataType
| **DataType** | **Value** |
| --- | --- |
| Boolean | boolean |
| Integer | int |
| Long integer | bigint |
| Float | double |
| String | string |
| Timestamp | timestamp |
| Date type | date |
| Time type | time |


###### aggregation
| **Aggregation** | **Value** |
| --- | --- |
| Sum | SUM |
| Mean | AVERAGE |
| Min | MIN |
| Max | MAX |
| Count | COUNT |
| Number of deduplicates | COUNT_DISTINCT |
| Variance | VARIANCE |
| Standard deviation | STD_DEVIATION |
| None | NONE |


###### joinType
| **Assocation** | **Value** |
| --- | --- |
| Left association | LEFT JOIN |
| Right association | RIGHT JOIN |
| Internal | INNER JOIN |
| Fully associative | FULL JOIN |


##### Example
model

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

### Consult
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



