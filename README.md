# Datafocus

## 语言/Language
- [中文](#中文)
- [English](#English)

## 中文

### 概览

DataFocus是一个集数据仓库、数据分析、智能问数BI于一体的BI平台，可以解析自然语言到SQL并查询出数据。

### 1. 获取DataFocus Token

如果你还没有DataFocus应用，可以前往[DataFocus官网](https://www.datafocus.ai/)申请一个。
登录DataFocus应用后，点击**系统管理** > **接口鉴权** > **承载令牌** > **新增承载令牌**，创建一个新的Token并复制得到Token值。
![](./_assets/readme_1.png)

### 2. Dify插件完成授权

从插件市场中安装DataFocus插件，并填写**token**和**host**完成授权认证。Token就是上一步中获取到的token值。如果你有DataFocus私有化部署环境，host要配置成环境的host地址。SAAS用户可以直接使用默认SAAS地址。https://cloud001.datafocus.ai

### 3. 使用插件

DataFocus包含两个工具——FocusSQL和FocusGPT。

#### FocusSQL

FocusSQL是一个基于关键词解析的自然语言转SQL插件。
![](./_assets/readme_3.png)

#### FocusGPT

FocusGPT是一个支持多轮对话的智能问数插件，可以使用自然语言直接从数据库中获取结果数据，并返回SQL。

![](./_assets/readme_2.png)

#### 配置说明

FocusSQL和FocusGPT的配置几乎一样，以下是每个配置的功能和使用方式。

| Parameter       | Description                                                  |
| --------------- | ------------------------------------------------------------ |
| 语言环境        | 语言解析环境，仅支持中文和英文                               |
| 查询语句        | 查询语句，插件根据参数输入生成SQL或查询数据                  |
| 数据表名        | 查询的数据表名                                               |
| 数据模型        | 这是一个高级功能，允许用户自定义数据表模型。详见[Model参数](#Model参数) |
| 输出SQL类型     | FocusSQL输出SQL的类型                                        |
| Conversation Id | 会话唯一标识，用于插件识别会话保持会话状态                   |
| 执行行为        | 工具可执行行为，①获取表列表；②对话互动                       |
| 数据源类型      | 连接外部数数据源类型。如果指定了数据源类型，则需要填写下方的数据源连接参数。如果不填写该值，将从DataFocus应用中选取表。 |
| Host地址        | Host地址                                                     |
| 端口            | 端口                                                         |
| 数据库用户      | 数据库用户                                                   |
| 数据库密码      | 数据库密码                                                   |
| 数据库名        | 数据库名                                                     |
| JDBC            | JDBC                                                         |
| Schema          | Schema                                                       |

#### Model参数

数据模型Model需要传入一个JSON字符串，Model结构如下

##### 结构

| 名称                 | 位置 | 类型     | 必选 | 说明                     |
| -------------------- | ---- | -------- | ---- | ------------------------ |
| type                 | body | string   | 是   | 数据库类型               |
| version              | body | string   | 是   | 数据库版本               |
| tables               | body | [object] | 是   | 表结构列表               |
| » tableDisplayName   | body | string   | 否   | 表显示名                 |
| » tableName          | body | string   | 否   | 表原始名                 |
| » columns            | body | [object] | 否   | 表列列表                 |
| »» columnDisplayName | body | string   | 是   | 列显示名                 |
| »» columnName        | body | string   | 是   | 列原始名                 |
| »» dataType          | body | string   | 是   | 列数据类型               |
| »» aggregation       | body | string   | 是   | 列聚合方式               |
| relations            | body | [object] | 是   | 表关联关系列表           |
| » conditions         | body | [object] | 否   | 关联条件                 |
| »» dstColName        | body | string   | 否   | dimension 表关联列原始名 |
| »» srcColName        | body | string   | 否   | fact 表关联列原始名      |
| » dimensionTable     | body | string   | 否   | dimension 表原始名       |
| » factTable          | body | string   | 否   | fact 表原始名            |
| » joinType           | body | string   | 否   | 关联类型                 |

##### 枚举值

###### type 数据库类型

| 值         | 含义             |
| ---------- | ---------------- |
| mysql      | mysql数据库      |
| clickhouse | clickhouse数据库 |
| impala     | impala数据库     |

###### dataType 数据类型

| 值        | 含义     |
| --------- | -------- |
| boolean   | 布尔类型 |
| int       | 整型     |
| bigint    | 长整型   |
| double    | 浮点型   |
| string    | 字符串   |
| timestamp | 时间戳   |
| date      | 日期类型 |
| time      | 时间类型 |

###### aggregation 聚合方式

| 值             | 含义     |
| -------------- | -------- |
| SUM            | 求和     |
| AVERAGE        | 平均值   |
| MIN            | 最小值   |
| MAX            | 最大值   |
| COUNT          | 数量     |
| COUNT_DISTINCT | 去重数量 |
| VARIANCE       | 方差     |
| STD_DEVIATION  | 标准差   |
| NONE           | 无       |

###### joinType 关联方式

| 值         | 含义   |
| ---------- | ------ |
| LEFT JOIN  | 左关联 |
| RIGHT JOIN | 右关联 |
| INNER JOIN | 内关联 |
| FULL JOIN  | 全关联 |

##### 例子

model

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

![](./_assets/wechat-qrcode.png)



## English

### Overview

The DataFocus tool can help you to query database data or generate SQL statements with natural language. The following will introduce how to configure and an example demonstration.

### 1. Apply for DataFocus Token

If you don't have the DataFocus application yet, please apply for one on the [DataFocus Website](https://www.datafocus.ai/).
Log in to your DataFocus application. Click **Admin** > **Interface Authentication** > **Bearer Token** > **New Bearer Token**, to create a new token and get _the token value_.
![](./_assets/readme_1.png)
If you have a DataFocus private deployment environment, you can get Token on your own environment.

### 2. Fill in the configuration in Dify

Install DataFocus from Marketplace and fill **token** and **host** in the authorization page.
Token is the value obtained in the previous step.
If you have a DataFocus private deployment environment, host is your environment host. Otherwise, the SAAS environment address can be used by default. 

### 3. Use the tool

DataFocus includes two tools, FocusSQL and FocusGPT.

#### FocusSQL

FocusSQL is a natural language to SQL plugin based on keyword parsing.
![](./_assets/readme_3.png)

#### FocusGPT

FocusGPT is an intelligent query plugin that supports multiple rounds of conversations, which allow you query data from your database. 
FocusGPT not only can return query SQL but also return query result to you.
![](./_assets/readme_2.png)

#### Configuration

FocusSQL and FocusGPT have similar configuration. Below are the functions and usage instructions of each parameter

| Parameter       | Description                                                  |
| --------------- | ------------------------------------------------------------ |
| Language        | Language environment, only support *Chinese* and *English*   |
| Query Statement | Natural language input by users                              |
| Table Name      | Target data table for query                                  |
| Data Model      | Custom model parameter entry                                 |
| Output SQL Type | Output SQL Type                                              |
| Conversation Id | Unique identifier of the session, which allow tool identify and maintain session state |
| Action          | The behavior of tool execution currently includes two types: obtaining table lists and dialogues |
| Datasource Type | Types of external data sources connected. If datasource type was selected, the connection parameters below need to be filled in |
| Host            | host                                                         |
| Port            | port                                                         |
| DB user         | user                                                         |
| DB Password     | password                                                     |
| Database Name   | database name                                                |
| JDBC            | JDBC                                                         |
| Schema          | Schema name                                                  |

#### Model Parameters

The data model needs to pass in a JSON string, and the structure of the model is as follows

##### Structure

| Name                 | Type     | Required | Description                    |
| -------------------- | -------- | -------- | ------------------------------ |
| type                 | string   | 是       | Database type                  |
| version              | string   | 是       | Database version, eg: 8.0      |
| tables               | [object] | 是       | Table structure list           |
| » tableDisplayName   | string   | 否       | Table display name             |
| » tableName          | string   | 否       | Original table name            |
| » columns            | [object] | 否       | Columns structure list         |
| »» columnDisplayName | string   | 是       | Column display name            |
| »» columnName        | string   | 是       | Original column name           |
| »» dataType          | string   | 是       | Column data type               |
| »» aggregation       | string   | 是       | Column default aggregation     |
| relations            | [object] | 是       | Association relationship list  |
| » conditions         | [object] | 否       | Associated conditions          |
| »» dstColName        | string   | 否       | Dimension original column name |
| »» srcColName        | string   | 否       | Fact original column name      |
| » dimensionTable     | string   | 否       | Dimension original table name  |
| » factTable          | string   | 否       | Fact original table name       |
| » joinType           | string   | 否       | Association type               |

##### 枚举值

###### type

| DataBase   | Value      |
| ---------- | ---------- |
| MySQL      | mysql      |
| ClickHouse | clickhouse |
| Impala     | impala     |

###### dataType 

| DataType     | Value     |
| ------------ | --------- |
| Boolean      | boolean   |
| Integer      | int       |
| Long integer | bigint    |
| Float        | double    |
| String       | string    |
| Timestamp    | timestamp |
| Date type    | date      |
| Time type    | time      |

###### aggregation 聚合方式

| Aggregation            | Value          |
| ---------------------- | -------------- |
| Sum                    | SUM            |
| Mean                   | AVERAGE        |
| Min                    | MIN            |
| Max                    | MAX            |
| Count                  | COUNT          |
| Number of deduplicates | COUNT_DISTINCT |
| Variance               | VARIANCE       |
| Standard deviation     | STD_DEVIATION  |
| None                   | NONE           |

###### joinType 关联方式

| Assocation        | Value      |
| ----------------- | ---------- |
| Left association  | LEFT JOIN  |
| Right association | RIGHT JOIN |
| Internal          | INNER JOIN |
| Fully associative | FULL JOIN  |

##### 例子

model

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